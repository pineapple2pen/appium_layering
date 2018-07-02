# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/22 14:55
# @File   : case_runner.py
from base.base_test_class import load_test_case
from page.start_page import StartPage
from page.charge_up_main_page import ChargeUpMainPage
from common.config import Config
from common.apk_tool import ApkInfo


class CaseRunner:
    d_c = {}

    def __init__(self, **kwargs):
        self.config = Config()
        self.d_c = dict(self.d_c, **self.config.desired_capabilities)
        self.config.device_id = kwargs["device_id"]
        self.d_c["udid"] = kwargs["device_id"]
        self.d_c["platformName"] = self.config.platform_name

    def get_apk_info(self):
        apk_info = ApkInfo(r"D:\appTest\appium_layering\appium_layering\file_dir\suishouji_1059000.apk")
        self.d_c["appActivity"] = apk_info.get_apk_activity()
        self.d_c["appPackage"], self.d_c["appVersionName"], self.d_c["appVersionCode"] = apk_info.get_apk_base_info()

    def get_appium(self):
        pass

    @staticmethod
    def get_page_mapper(driver):
        return {
            "开始等待页面": StartPage(driver),
            "记账主页面": ChargeUpMainPage(driver)
        }

    @staticmethod
    def run_step(step: dict):
        try:
            pass
        except Exception as e:
            step["run_result"] = "失败，失败原因:" + str(e.args)
        else:
            step["run_result"] = "成功"

    def run_case(self):
        test_case = load_test_case("../TestCase.xlsx")
        if isinstance(test_case, list) and len(test_case) > 0:
            for case in test_case:
                print("开始执行用例")
                if isinstance(case, list) and len(case) > 0:
                    for step in case:
                        if isinstance(step, dict):
                            self.run_step(step)


if __name__ == "__main__":
    pass
