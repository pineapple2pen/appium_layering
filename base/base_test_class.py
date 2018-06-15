# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 9:54
# @File   : base_test_class.py

from appium import webdriver
import unittest


def get_appium_driver(app_devices):
    desired_caps = {}

    if app_devices["platform"].lower() == "android":
        desired_caps["platformName"] = "Android"
        # desired_caps["platformVersion"] = app_devices["platformVersion"]
        desired_caps["deviceName"] = app_devices["deviceName"]
        desired_caps["appPackage"] = app_devices["appPackage"]
        desired_caps["appActivity"] = app_devices["appActivity"]
        desired_caps["noReset"] = "True"
        desired_caps['noSign'] = "True"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

    return webdriver.Remote("http://localhost:" + str(app_devices["appiumPort"]) + "/wd/hub", desired_caps)


class BaseTestClass(unittest.TestCase):
    def __init__(self, app):
        super().__init__()
        self.driver = get_appium_driver(app)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()
