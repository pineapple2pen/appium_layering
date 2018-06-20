# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 15:47
# @File   : charge_up_main_page.py
from page.base_page import BasePage
from appium.webdriver import Remote


class ChargeUpMainPage(BasePage):
    BUTTON_RECORD_MONEY_IO = "com.mymoney:id/add_expense_quickly_btn"

    def __init__(self, remote_car: Remote):
        super().__init__(remote_car)
