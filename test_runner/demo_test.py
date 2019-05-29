# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 10:31
# @File   : demo_test.py

from base.base_test_class import get_appium_driver
from page.start_page import StartPage
from common.apk_tool import ApkInfo
from server.appium_server import AppiumServer


class DemoTest:
    def __init__(self):
        # appium_server = AppiumServer()

        apk_info = ApkInfo(r"..\file_dir\suishouji_1059000.apk")
        app = {
            "platform": "Android",
            "deviceName": "Android",
            "appActivity": apk_info.get_apk_activity(),
            "appiumPort": "4723",
            "appPackage": apk_info.get_apk_base_info()[0],
            "platformName": "Android",
            "platformVersion": "8.1",
            "udid": "",
        }
        self.driver = get_appium_driver(app)
        self.start_page = StartPage(self.driver)

    def run(self):
        self.start_page.click_skip()


if __name__ == "__main__":
    DemoTest().run()


