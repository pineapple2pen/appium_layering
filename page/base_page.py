# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/20 9:38
# @File   : base_page.py
from appium.webdriver import Remote
from server.driver_server import DriverServer
from common.config import Config
import os


class BasePage(object):
    def __init__(self, remote_car: Remote):
        self.remote_car = remote_car
        self.driver = DriverServer(remote_car)

    @staticmethod
    def click_back():
        device_id = Config().device_id
        os.system("adb -s %s shell input keyevent 4" % device_id)

    def go_back_main_page(self):
        pass
