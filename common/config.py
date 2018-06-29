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
    device_id = None

    def __init__(self, config_address="../config.ini"):
        self.config_reader = configparser.ConfigParser()
        self.config_reader.read(config_address, encoding="utf-8")

        # desired capabilities
        self.desired_capabilities = {
            "noReset": bool(int(self.config_reader.get("desired capabilities", "noReset"))),
            "noSign": bool(int(self.config_reader.get("desired capabilities", "noSign"))),
            "unicodeKeyboard": bool(int(self.config_reader.get("desired capabilities", "unicodeKeyboard"))),
            "resetKeyboard": bool(int(self.config_reader.get("desired capabilities", "resetKeyboard"))),
        }

    def get_config(self, config_name: str, key: str):
        return self.config_reader.get(config_name, key)

    def get_object(self, obj, obj_name, *args) -> object:
        try:
            return getattr(self, obj_name)

        except AttributeError:
            obj_ins = obj(args)
            setattr(self, obj_name, obj_ins)
            return obj_ins

    def set_attr(self, attr_name, attr):
        setattr(self, attr_name, attr)

    @staticmethod
    def encrypt_pwd(encrypt_str):
        exec_type = encrypt_str[-1]
        if exec_type == "-":
            return "".join([chr(ord(i) + int(encrypt_str[-4:-1])) for i in encrypt_str[0:-4]])
        else:
            return "".join([chr(ord(i) - int(encrypt_str[-4:-1])) for i in encrypt_str[0:-4]])


if __name__ == "__main__":
    pass
