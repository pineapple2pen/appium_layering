# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/20 9:38
# @File   : base_page.py
from appium.webdriver import Remote
from server.driver_server import DriverServer


class BasePage(object):
    def __init__(self, remote_car: Remote):
        self.remote_car = remote_car
        self.driver = DriverServer(remote_car)
