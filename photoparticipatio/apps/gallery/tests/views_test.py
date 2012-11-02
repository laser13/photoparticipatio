# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'


from photoparticipatio.libs.test import ExtendedTestCase
from django_any import any_model
from photoparticipatio.apps.gallery.models.album import Album
from photoparticipatio.libs.utils.helpers import var_dump
from django.contrib.auth.models import User


class AlbomShow(ExtendedTestCase):

    """
        Тестируем страницу просмотра альбома
    """

    USER_NAME1 = 'user1'
    USER_NAME2 = 'user2'

    USER_PASS1 = '123'
    USER_PASS2 = '321'

    def setUp(self):

        self.client.session.clear()

        self.user1 = any_model(User, is_active=True, username=self.USER_NAME1)
        self.user2 = any_model(User, is_active=True, username=self.USER_NAME2)

        self.user1.set_password(self.USER_PASS1)
        self.user2.set_password(self.USER_PASS2)

        self.user1.save()
        self.user2.save()

        self.album_public = any_model(Album, id=1, access=Album.ACCESS_PUBLIC, kind=Album.KIND_CUSTOM)
        self.album_private1 = any_model(Album, id=2, access=Album.ACCESS_PRIVATE, kind=Album.KIND_CUSTOM, user=self.user1)
        self.album_private2 = any_model(Album, id=3, access=Album.ACCESS_PRIVATE, kind=Album.KIND_CUSTOM, user=self.user2)

    def test_public_album_show(self):

        """
            Тестируем страницу показа публичного альбома

            Публичный альбом должен быть виден для всех
            Ссылка на несуществующий альбом должна возвращать 404 ошибку
        """

        print '>>> test_public_album_show'

        # Проверка доступа к публичному альбому неавторизованного пользователя
        print u'Проверка доступа к публичному альбому неавторизованного пользователя', "\n"
        url200 = '/gallery/album/{0}/'.format(self.album_public.pk)
        url404 = '/gallery/album/1000/'
        templates = 'gallery/album/show.html'
        self.assertUrl(url200, templates, url404)


        # Проверка доступа к публичному альбому авторизованного пользователя
        print u'Проверка доступа к публичному альбому авторизованного пользователя', "\n"

        self.login(self.USER_NAME1, self.USER_PASS1)

        self.assertUrl(
            url200='/gallery/album/{0}/'.format(self.album_public.pk),
            templates_used='gallery/album/show.html',
            url404='/gallery/album/1000/'
        )

    def test_private_album_show(self):

        """
            Тестируем страницу показа приватного альбома

            Приватный альбом должен быть виден для владельца, всем остальным отдавать 404 ошибку
            Ссылка на несуществующий альбом должна возвращать 404 ошибку
        """

        print '>>> test_private_album_show'

        # Проверка доступа к приватному альбому неавторизованного пользователя
        print u' Проверка доступа к приватному альбому неавторизованного пользователя', "\n"

        url = '/gallery/album/{0}/'.format(self.album_private1.pk)
        self.assertResponseCode(url, 404)

        self.login(self.USER_NAME1, self.USER_PASS1)

        # Проверка доступа к чужому приватному альбому авторизованного пользователя
        print u'Проверка доступа к чужому приватному альбому авторизованного пользователя', "\n"
        url = '/gallery/album/{0}/'.format(self.album_private2.pk)
        self.assertResponseCode(url, 404)

        # Проверка доступа к своему приватному альбому авторизованного пользователя
        print u'Проверка доступа к своему приватному альбому авторизованного пользователя', "\n"
        url200 = '/gallery/album/{0}/'.format(self.album_private1.pk)
        url404 = '/gallery/album/1000/'
        templates = 'gallery/album/show.html'
        self.assertUrl(url200, templates, url404)

class AlbomAdd(ExtendedTestCase):

    """
        Тестируем страницу и функциональность добавления альбома
    """

    USER_NAME1 = 'user1'
    USER_PASS1 = '123'

    def setUp(self):

        self.client.session.clear()

        self.user1 = any_model(User, is_active=True, username=self.USER_NAME1)
        self.user1.set_password(self.USER_PASS1)
        self.user1.save()

    def test_add_page(self):

        """
            Тестируем
        """

        print '>>> test_add_page'

        # Проверяем доступность страницы для неавторизованного пользователя
        print u'Проверяем доступность страницы для неавторизованного пользователя', "\n"
        url302 = '/gallery/album/add/'
        url_target = '/accounts/?next=/gallery/album/add/'
        resp = self.client.get(url302)
        self.assertRedirects(resp, url_target, 302)

        # Проверяем доступность страницы для авторизованного пользователя
        print u'Проверяем доступность страницы для авторизованного пользователя', "\n"

        self.login(self.USER_NAME1, self.USER_PASS1)

        url404 = '/gallery/album/add/'
        self.assertResponseCode(url=url404, code=200)

    def test_create_album(self):

        url = '/gallery/album/save/'

        data = {
            'title': u'Test title 1',
            'access': Album.ACCESS_PUBLIC,
        }

        """
            Проверка доступа для неавторизованного пользователя
            При попытке обратится по данному url неавторизованного пользователя должно перенаправлять на страницу авторизации
        """
        resp = self.client.get(url)
        self.assertRedirects(resp, '/accounts/?next='+url, 302)

        """
            Проверка доступа для авторизованного пользователя
        """
        self.login(self.USER_NAME1, self.USER_PASS1)

        resp = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        json_responce = self.json_responce(resp)
        self.assertEqual(json_responce['status'], 'error')

        data['id'] = 0
        resp = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        json_responce = self.json_responce(resp)

        self.assertTrue(json_responce.has_key('album_id'))
        album_id = json_responce['album_id']
        album = Album.objects.get(pk=album_id)

        self.assertEqual(album.user, self.user1)


        print json_responce
