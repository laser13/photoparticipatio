# -*- coding: UTF-8 -*-


from photoparticipatio.libs.test import ExtendedTestCase
from django_any import any_model
from photoparticipatio.apps.gallery.models.album import Album
from django.contrib.auth.models import User


class GalleryViewsAlbomShowTestCase(ExtendedTestCase):

    USER_NAME1 = 'user1'
    USER_NAME2 = 'user2'

    USER_PASS1 = '123'
    USER_PASS2 = '321'

    def setUp(self):

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

        # Проверка доступа к публичному альбому неавторизованного пользователя

        url200 = '/gallery/album/{0}/'.format(self.album_public.pk)
        url404 = '/gallery/album/1000/'
        templates = 'gallery/album/show.html'
        self.assertUrl(url200, templates, url404)


        # Проверка доступа к публичному альбому авторизованного пользователя

        logined = self.client.login(username=self.USER_NAME1, password=self.USER_PASS1)
        self.assertTrue(logined)

        url200 = '/gallery/album/{0}/'.format(self.album_public.pk)
        url404 = '/gallery/album/1000/'
        templates = 'gallery/album/show.html'
        self.assertUrl(url200, templates, url404)

    def test_private_album_show(self):

        # Проверка доступа к приватному альбому неавторизованного пользователя

        url = '/gallery/album/{0}/'.format(self.album_private1.pk)
        self.assertResponseCode(url, 404)


        logined = self.client.login(username=self.USER_NAME1, password=self.USER_PASS1)
        self.assertTrue(logined)

        # Проверка доступа к чужому приватному альбому авторизованного пользователя
        url = '/gallery/album/{0}/'.format(self.album_private2.pk)
        self.assertResponseCode(url, 404)


        # Проверка доступа к своему приватному альбому авторизованного пользователя
        url200 = '/gallery/album/{0}/'.format(self.album_private1.pk)
        url404 = '/gallery/album/1000/'
        templates = 'gallery/album/show.html'
        self.assertUrl(url200, templates, url404)