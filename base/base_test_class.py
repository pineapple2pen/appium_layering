# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 9:54
# @File   : base_test_class.py

from appium import webdriver
import unittest


def get_appium_driver(config):
    desired_caps = {}
    desired_caps.update(**config.desired_capabilities)

    desired_caps["udid"] = config.device_id
    desired_caps["device"] = config.device_id
    desired_caps["deviceName"] = config.device_id
    return webdriver.Remote("http://localhost:" + str(config.appiumPort) + "/wd/hub", desired_caps)

