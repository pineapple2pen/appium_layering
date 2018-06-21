# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/25 11:04
# @File   : config.py

from common.singleton import singleton
import configparser


@singleton
class Config(object):
    config_reader = None
    platform_name = "Android"

    def __init__(self, config_address="../config.ini"):
        self.config_reader = configparser.ConfigParser()
        self.config_reader.read(config_address)

        # desired capabilities
        self.desired_capabilities = {
            "noReset": bool(int(self.config_reader.get("desired capabilities", "noReset"))),
            "noSign": bool(int(self.config_reader.get("desired capabilities", "noSign"))),
            "unicodeKeyboard": bool(int(self.config_reader.get("desired capabilities", "unicodeKeyboard"))),
            "resetKeyboard": bool(int(self.config_reader.get("desired capabilities", "resetKeyboard"))),
        }

if __name__ == "__main__":
    pass
