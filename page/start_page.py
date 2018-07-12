# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 10:09
# @File   : start_page.py
from appium.webdriver import Remote
from page.base_page import BasePage


class StartPage(BasePage):
    SKIP_BUTTON = "com.mymoney:id/splash_skip_tv"

    def __init__(self, remote_car: Remote):
        super().__init__(remote_car)

        # 将操作注册至操作字典内
        operator_dict = super().operator_dict
        operator_dict["点击跳过"] = self.click_skip

    def click_skip(self):
        if self.driver.element_status(self.SKIP_BUTTON):
            self.driver.click_ele(self.SKIP_BUTTON)

    def get_advertising(self):
        pass
