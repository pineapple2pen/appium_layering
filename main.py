# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2019/2/12 10:12
# @File   : main.py
import time
from common.config import Config
from test_runner.runner import CaseRunner
from common.html_test_runner import HtmlTestRunner

if __name__ == "__main__":
    c = Config("./config.ini")
    case = CaseRunner()
    test_suite = case.run_test_case()
    # 用参数化定义测试报告的名字
    test_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    report_path_name = "reports\\check_log_%s.html" % test_time
    report_file = open(report_path_name, "wb")

    test_runner = HtmlTestRunner(
        stream=report_file,
        title="AppiumDemo",
        description="Appium Demo Test Report"
    )
    test_runner.run(test_suite)
    report_file.close()
    c.tear_down()
