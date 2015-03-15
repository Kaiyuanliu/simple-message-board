# -*- coding: utf-8 -*-
import sys
from app import app
from flask_testing import LiveServerTestCase
from selenium import webdriver


class FunctionalTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8090
        return app

    @classmethod
    def setUpClass(cls):
        super(FunctionalTest, cls).setUpClass()
        cls.server_url = cls.get_server_url()

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.get_server_url():
            super(FunctionalTest, cls).tearDownClass()

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        self.brower.quit()
