# -*- coding: utf-8 -*-
import unittest
from app import app
from flask_testing import LiveServerTestCase
from selenium import webdriver


class FunctionalTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8493
        return app

    @classmethod
    def setUpClass(cls):
        super(FunctionalTest, cls).setUpClass()
        cls.server_url = cls.get_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.get_server_url:
            super(FunctionalTest, cls).tearDownClass()

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        self.brower.quit()

    @property
    def get_server_url(self):
        return 'http://localhost:%s' % self.port


    def test_can_create_a_message(self):
        self.brower.get(self.server_url)
        self.assertIn('Simple Message Board', self.brower.title)



if __name__ == '__main__':
    unittest.main()
