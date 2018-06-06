# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/25 14:39
# @File   : adb_tool.py
#
# VSS - Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）
#
# RSS - Resident Set Size 实际使用物理内存（包含共享库占用的内存）
#
# PSS - Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存）
#
# USS - Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）
#
# 一般来说内存占用大小有如下规律：VSS >= RSS >= PSS >= USS


def devices():
    return "adb devices"


def get_package_list():
    return 'adb shell "pm list package"'


def find_package(package):
    return 'adb shell "pm list package|grep "%s""' % package


def get_package_memo(package):
    return 'adb shell "ps |grep %s"' % package


def get_mobile_total_ram():
    return 'adb shell "dumpsys meminfo -s|grep "Total RAM""'


def get_mobile_app_ram():
    return 'adb shell "dumpsys meminfo -s|grep "com.tencent.mm""'



