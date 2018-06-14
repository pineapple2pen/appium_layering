# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/5/28 10:14
# @File   : apk_tool.py

import re
import subprocess
import os
import json


class ApkInfo:
    def __init__(self, apk_path):
        """
        通过apk包获取apk信息
        :param apk_path:apk路径 
        """
        self.apkPath = apk_path
        self.aapt_path = self.get_aapt()

    @staticmethod
    def get_aapt():
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt.exe" in files:
                    return os.path.join(path, "aapt.exe")
        else:
            return "ANDROID_HOME not exist"

    def get_apk_size(self):
        """
        得到apk的文件大小
        :return: 
        """
        print(os.path.getsize(self.apkPath))
        size = round(os.path.getsize(self.apkPath) / (1024 * 1000), 2)
        return str(size) + "M"

    def get_apk_base_info(self):
        """
        获取apk包的基本信息
        :return: 
        """
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        package_name = match.group(1)
        version_code = match.group(2)
        version_name = match.group(3)

        # print('packageName:' + package_name)
        # print('versionCode:' + version_code)
        # print('versionName:' + version_name)
        return package_name, version_name, version_code

    def get_apk_name(self):
        """
        获取apk名字
        :return:
        """
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode().split("\n")
        for item in t:
            # print(item)
            # 此处的apk包名我是取得中文名称。具体信息可以在dos下用aapt查看详细信息后，修改正则获取自己想要的name
            match = re.compile("application-label-zh-CN:'([\u4e00-\u9fa5_a-zA-Z0-9-\S]+)'").search(item)
            if match is not None:
                return match.group(1)

    def get_apk_activity(self):
        """
        得到启动类
        :return:
        """
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        # print(err.decode('gbk'))
        match = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
        # print("match=%s" % match)
        if match is not None:
            return match.group(1)


if __name__ == '__main__':
    apk_info = ApkInfo(r"..\suishouji_1059000.apk")
    # apk_info = ApkInfo(r"D:\ChromeDownloads\suishouji_1059000.apk")
    print(apk_info.get_apk_activity())
    print(apk_info.get_apk_base_info())
    print(apk_info.get_apk_name())
    print(apk_info.get_apk_size())
