# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 10:09
# @File   : start_page.py
from appium.webdriver import Remote


class StartPage:
    SKIP_BUTTON = "com.mymoney:id/splash_skip_tv"

    def __init__(self, driver: Remote):
        self.driver = driver

    def click_skip(self):
        self.driver.find_element_by_id(self.SKIP_BUTTON).click()
