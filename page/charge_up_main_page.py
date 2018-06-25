# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 15:47
# @File   : charge_up_main_page.py
from page.base_page import BasePage
from appium.webdriver import Remote


class ChargeUpMainPage(BasePage):
    # 记一笔按钮
    BUTTON_RECORD_MONEY_IO = "com.mymoney:id/add_expense_quickly_btn"
    # 本月收入
    INFO_MONTH_INCOME = "com.mymoney:id/first_item_value_tv"
    # 本月支出
    INFO_MONTH_EXPEND = "com.mymoney:id/second_item_value_tv"
    # 本月预算
    INFO_MONTH_BUDGET = "com.mymoney:id/third_item_value_tv"
    # 预算图
    INFO_BUDGET_BUCKET = "com.mymoney:id/budget_status_bv"
    # 当前年份
    INFO_YEAR = "com.mymoney:id/year_tv"
    # 当前月份
    INFO_MONTH = "com.mymoney:id/month_tv"
    # 隐藏/显示 金额
    BUTTON_MONEY_ENCRYPT = "com.mymoney:id/hide_top_all_money_iv"
    # 消息中心按钮
    BUTTON_MSG_CENTER = "com.mymoney:id/message_v"
    # 账本菜单设置
    BUTTON_SETTING = "com.mymoney:id/pop_more_iv"
    # 支出分类页面按钮
    BUTTON_PIE_REPORT = "com.mymoney:id/report_btn"
    # 今日支出收入一栏
    INFO_TODAY_MONEY_IO = "//*[@class='android.widget.RelativeLayout' and @index='0']"




    def __init__(self, remote_car: Remote):
        super().__init__(remote_car)
