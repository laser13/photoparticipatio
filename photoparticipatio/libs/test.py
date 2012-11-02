# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'


from django.test import TestCase


class ExtendedTestCase(TestCase):

    def assertResponseCode(self, url, code=200):

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, code)

    def assertUrl(self, url200, templates_used=None, url404=None):

        resp = self.client.get(url200)
        self.assertEqual(resp.status_code, 200)

        if templates_used:
            self.assertTemplateUsed(resp, template_name=templates_used)

        if url404:
            resp = self.client.get(url404)
            self.assertEqual(resp.status_code, 404)

    def login(self, username, password):

        self.client.logout()
        self.client.session.clear()
        logined = self.client.login(username=username, password=password)
        self.assertTrue(logined)

    def json_responce(self, resp):
        import json
        return json.loads(resp.content)