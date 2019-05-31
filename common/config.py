# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/25 11:04
# @File   : config.py

import os
import configparser
import json

from common.singleton import singleton
from page.page import Page
from server.appium_server import AppiumServer
from common.adb_tools import ADBTools
from base.base_test_class import get_appium_driver


@singleton
class Config(object):
    config_reader = None
    platform_name = "Android"
    device_id = None

    def __init__(self, config_address="../config.ini"):
        self.project_path = os.path.split(os.path.abspath(config_address))[0]
        self.config_reader = configparser.ConfigParser()
        self.config_reader.read(config_address, encoding="utf-8")
        self._load_page_and_ope()
        self._load_desired_capabilities()
        self._get_devices()
        self.appiumPort = "4723"
        self._start_appium_server()
        self._init_driver()

    def get_config(self, config_name: str, key: str):
        return self.config_reader.get(config_name, key)

    def get_object(self, obj, obj_name, *args):
        try:
            return getattr(self, obj_name)

        except AttributeError:
            obj_ins = obj(*args)
            setattr(self, obj_name, obj_ins)
            return obj_ins

    def set_attr(self, attr_name, attr):
        setattr(self, attr_name, attr)

    def _get_devices(self):
        udid_list = ADBTools.get_udid_list()
        if len(udid_list) > 0:
            self.device_id = udid_list[0]
        else:
            raise Exception("no devices")

    def _load_desired_capabilities(self):
        self.desired_capabilities = {
            "noReset": self.config_reader.get("desired capabilities", "noReset"),
            "noSign": self.config_reader.get("desired capabilities", "noSign"),
            "unicodeKeyboard": self.config_reader.get("desired capabilities", "unicodeKeyboard"),
            "resetKeyboard": self.config_reader.get("desired capabilities", "resetKeyboard"),
            "platformName": self.config_reader.get("test config", "platform"),
            "appActivity": self.config_reader.get("apk info", "appActivity"),
            "appPackage": self.config_reader.get("apk info", "appPackage"),
        }

    def _load_page_and_ope(self):
        # 加载所有 page 以及页面操作和test_case
        self.page_dir = {}
        for path, _, files in os.walk(self.project_path + "\\page_config"):
            for file in files:
                file_name, file_type = os.path.splitext(file)
                if file_type == ".json":
                    self.page_dir[file_name] = Page.get_page(self, file_name)
            break

        self.page_operator_dir = {}
        for path, _, files in os.walk(self.project_path + "\\operator_config"):
            for file in files:
                self._load_page_operator(path + "\\" + file)
            break

        self.test_case_dir = {}
        for path, _, files in os.walk(self.project_path + "\\test_case"):
            for file in files:
                self._load_test_case(path + "\\" + file)
            break

    def _load_page_operator(self, abspath):
        with open(abspath, "r", encoding="utf-8") as f:
            file_json = json.loads(f.read(), encoding="utf-8")
        for ope in file_json:
            self.page_operator_dir[ope["page"] + "-" + ope["id"]] = ope

    def _load_test_case(self, abspath):
        with open(abspath, "r", encoding="utf-8") as f:
            file_json = json.loads(f.read(), encoding="utf-8")
        for ope in file_json:
            self.test_case_dir[ope["id"]] = ope

    def _start_appium_server(self):
        app_server_param = {
            "devices": self.device_id,
            "port": self.appiumPort
        }
        app_server = AppiumServer(app_server_param)
        app_server.start_server()
        self.app_server = app_server

    def _init_driver(self):
        self.driver = get_appium_driver(self)

    def tear_down(self):
        self.driver.close_app()
        self.driver.quit()
        self.app_server.stop_server(self.appiumPort)



if __name__ == "__main__":
    Config()
