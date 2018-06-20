# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/20 15:21
# @File   : keycode_enum.py
import enum


class KeyCodeEnum(enum.Enum):
    # 拨号键
    KEYCODE_CALL = 5
    # 挂机键
    KEYCODE_ENDCALL = 6
    # 按键Home
    KEYCODE_HOME = 3
    # 菜单键
    KEYCODE_MENU = 82
    # 返回键
    KEYCODE_BACK = 4
    # 搜索键
    KEYCODE_SEARCH = 84
    # 拍照键
    KEYCODE_CAMERA = 27
    # 拍照对焦键
    KEYCODE_FOCUS = 80
    # 电源键
    KEYCODE_POWER = 26
    # 通知键
    KEYCODE_NOTIFICATION = 83
    # 话筒静音键
    KEYCODE_MUTE = 91
    # 扬声器静音键
    KEYCODE_VOLUME_MUTE = 164
    # 音量增加键
    KEYCODE_VOLUME_UP = 24
    # 音量减小键
    KEYCODE_VOLUME_DOWN = 25
