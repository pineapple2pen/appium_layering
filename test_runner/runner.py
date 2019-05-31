# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2019/5/30 10:01
# @File   : runner.py
from unittest import TestSuite, TestCase, TestLoader
import datetime
from common.config import Config
from server.driver_server import DriverServer


class CaseRunner(object):

    def __init__(self, fail_fast=False):
        self.config = Config()
        self.fail_fast = fail_fast
        self.test_loader = TestLoader()

    @staticmethod
    def _run_operator(config, operator_id):
        print(config.page_operator_dir)
        operator = config.page_operator_dir[operator_id]

        for ope in operator["operator"]:
            page = config.page_dir[operator["page"]]
            func = ope["func"]
            element_id = ope["element_id"]
            other_param_dict = ope["other_param_dict"] if "other_param_dict" in ope.keys() else {}
            other_param_list = ope["other_param_list"] if "other_param_list" in ope.keys() else []
            save_return = ope["saveReturn"] if "saveReturn" in ope.keys() else False
            element = page.get_element(element_id)[config.platform_name.lower()]
            if element != "":
                other_param_list.insert(0, element)
            print(func, other_param_list, other_param_dict)
            res = config.driver_server(func, *other_param_list, **other_param_dict)
            if save_return:
                return res

    def run_test_case(self):
        def test_case(config, case_id):
            def test(self):
                test_case = config.test_case_dir[case_id]
                operator_return = {}
                print("开始运行用例：{}, case id:{}".format(test_case["name"], test_case["id"]))
                # 运行用例
                need_ope = test_case["execute"] + test_case["check_ope"]
                print("开始运行用例步骤")
                for operator in need_ope:
                    print("operator {} start".format(operator["execute_id"]))
                    ope_ret = CaseRunner._run_operator(config, operator["execute_id"])
                    print("operator return {}".format(ope_ret))
                    if operator["save_return"]:
                        operator_return[operator["save_name"]] = ope_ret

                # 执行检查
                print("开始执行检查")
                for check in test_case["check_param"]:
                    print("check expect：{} - {}， actual：{}".format(check["check_func"],
                                                                   check["param"],
                                                                   operator_return[check["check_val"]]
                                                                   ))
                    actual_res = operator_return[check["check_val"]]
                    if type(check["param"]) not in [list, tuple]:
                        actual_res = type(check["param"])(actual_res)
                    check_res = Check.check[check["check_func"]](actual_res, check["param"])
                    print("check result {}".format(check_res))
                    assert check_res

            return test

        cases = self.config.test_case_dir
        all_case = cases.keys()
        test_suite = TestSuite()
        TestSequense = type('TestSequense', (TestCase,), {})

        for c in all_case:
            if cases[c]["run"]:
                test_method_name = "test_{}_{}".format(datetime.datetime.today(), c)
                test_method = test_case(self.config, c)
                setattr(TestSequense, test_method_name, test_method)
        loaded_testcase = self.test_loader.loadTestsFromTestCase(TestSequense)
        test_suite.addTest(loaded_testcase)
        return test_suite


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
    case = CaseRunner()
    case.run_test_case()
