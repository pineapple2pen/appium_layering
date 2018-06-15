# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 10:09
# @File   : start_page.py
from appium.webdriver import Remote


class StartPage:
    def __init__(self, driver: Remote):
        self.driver = driver


