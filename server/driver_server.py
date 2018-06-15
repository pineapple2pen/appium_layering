# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 15:42
# @File   : driver_server.py
from appium.webdriver import Remote


class DriverServer:
    # todo封装操作
    def __init__(self, driver: Remote):
        self.driver = driver

    def get_element(self, selector):
        pass



