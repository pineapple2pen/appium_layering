# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2019/5/30 10:01
# @File   : runner.py
from common.config import Config
from server.driver_server import DriverServer
from base.base_test_class import get_appium_driver


class CaseRunner(object):

    def __init__(self, fail_fast=False):
        self.config = Config()
        self.fail_fast = fail_fast
        self.driver = DriverServer(self.config.driver)

    def _run_operator(self, operator_id):
        print(self.config.page_operator_dir)
        operator = self.config.page_operator_dir[operator_id]

        for ope in operator["operator"]:
            page = self.config.page_dir[operator["page"]]
            func = ope["func"]
            element_id = ope["element_id"]
            other_param_dict = ope["other_param_dict"] if "other_param_dict" in ope.keys() else {}
            other_param_list = ope["other_param_list"] if "other_param_list" in ope.keys() else []
            save_return = ope["saveReturn"] if "saveReturn" in ope.keys() else False
            element = page.get_element(element_id)[self.config.platform_name.lower()]
            if element != "":
                other_param_list.insert(0, element)
            print(func, other_param_list, other_param_dict)
            res = self.driver(func, *other_param_list, **other_param_dict)
            if save_return:
                return res

    def _run_test_case(self, case_id):
        test_case = self.config.test_case_dir[case_id]
        operator_return = {}
        print("开始运行用例：{}, case id:{}".format(test_case["name"], test_case["id"]))
        # 运行用例
        need_ope = test_case["execute"] + test_case["check_ope"]
        for operator in need_ope:
            ope_ret = self._run_operator(operator["execute_id"])
            if operator["save_return"]:
                operator_return[operator[save_name]] = ope_ret

        # 执行检查
        for check in test_case["check_param"]:
            check_res = Check.check[check[check["check_func"]]](
                type(check["param"])(operator_return[check["check_val"]]),
                check["param"])
            if not check_res:
                print("check error, expect：{} - {}， actual：{}".format(check["check_func"],
                                                                      check["check_val"],
                                                                      check["param"]))


class Check:
    check = {
        "gt": lambda a, b: a > b,
        "gte": lambda a, b: a >= b,
        "lt": lambda a, b: a < b,
        "lte": lambda a, b: a < b,
        "eq": lambda a, b: a == b,
        "neq": lambda a, b: a != b,
        "contain": lambda a, b: a in b,
    }


if __name__ == "__main__":
    pass
