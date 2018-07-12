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
        desired_caps["platformVersion"] = app_devices["platformVersion"]
        desired_caps["deviceName"] = app_devices["udid"]
        desired_caps["appPackage"] = app_devices["appPackage"]
        desired_caps["appActivity"] = app_devices["appActivity"]
        desired_caps["noReset"] = app_devices["noReset"]
        desired_caps['noSign'] = app_devices["noSign"]
        desired_caps["unicodeKeyboard"] = app_devices["unicodeKeyboard"]
        desired_caps["resetKeyboard"] = app_devices["resetKeyboard"]
        desired_caps["udid"] = app_devices["udid"]

    return webdriver.Remote("http://localhost:" + str(app_devices["appiumPort"]) + "/wd/hub", desired_caps)


def load_test_case(case_path):
    from common.excel_tool import ExcelTool
    try:
        test_case_excel = ExcelTool("r", case_path)
        # 获取用例sheet
        case_sheet = test_case_excel.work_book_xlsx["用例"]
        # 循环获取用例
        first_case = True
        test_case = []
        case_id = 0
        for row in range(2, case_sheet.max_row + 2):
            case_num = case_sheet.cell(row, 1).value
            if first_case:
                test_case.append([])
                first_case = False
            try:
                if isinstance(test_case[case_id], list):
                    pass
            except IndexError:
                test_case.append([])

            test_step = {
                "page": case_sheet.cell(row, 2).value,
                "step_id": case_sheet.cell(row, 3).value,
                "operator_type": case_sheet.cell(row, 4).value,
                "operator": case_sheet.cell(row, 5).value,
                "param": case_sheet.cell(row, 6).value,
                "check_param": case_sheet.cell(row, 7).value,
                "remark": case_sheet.cell(row, 8).value,
            }
            is_none = list(filter(not_blank, list(test_step.values())))
            if len(is_none) == 0:
                break
            test_step["case_id"] = case_num if case_num not in [None, ""] else str(case_id + 1)
            test_case[case_id].append(test_step)

            next_case_num = case_sheet.cell(row + 1, 1).value
            if next_case_num in [None, ""] or next_case_num == case_num:
                pass
            else:
                case_id += 1

    except Exception as e:
        print(e)
    else:
        return test_case


def not_blank(param: str):
    if param in [None, ""]:
        return False
    else:
        return True


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


if __name__ == "__main__":
    print(load_test_case("../TestCase.xlsx"))
