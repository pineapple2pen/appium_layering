# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/28 16:46
# @File   : adb_tools.py
import os
import subprocess
import re


class ADBTools:
    @staticmethod
    def call_adb(command):
        command_result = ''
        command_text = 'adb %s' % command
        # print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line:
                break
            command_result += line
        results.close()
        return command_result

    @staticmethod
    def kill_adb():
        """
        关闭adb.exe
        :return:
        """
        if platform.system() == "Windows":
            os.system(os.path.abspath("./common/other_file/kill5037.bat"))
        else:
            os.popen("killall adb")
        os.system("adb start-server")

    @staticmethod
    def get_udid_list():
        p = subprocess.Popen("adb devices",
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        output, err = p.communicate()

        devices = re.findall("\n([\w\S]+)\s+device", output.decode())

        if len(devices) == 0:
            print()
            return "未匹配到设备"
        else:
            return devices

    @classmethod
    def get_state(cls):
        """
        获取状态
        :return:
        """
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    @classmethod
    def reboot(cls, option):
        """
        重启设备
        :param option:
        :return:
        """
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        cls.call_adb(command)

    @classmethod
    def push(cls, local, remote):
        """
        将电脑文件拷贝到手机里面
        :param local: 文件路径
        :param remote:
        :return:
        """
        result = cls.call_adb("push %s %s" % (local, remote))
        return result

    @classmethod
    def pull(cls, remote, local):
        """
        拉数据到本地
        :param remote:
        :param local:
        :return:
        """
        result = cls.call_adb("pull %s %s" % (remote, local))
        return result

    @classmethod
    def sync(cls, directory, **kwargs):
        """
        同步更新
        :param directory:
        :param kwargs:
        :return:
        """
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = cls.call_adb(command)
            return result

    @classmethod
    def open_app(cls, package_name, activity):
        """
        打开指定app
        :param package_name:
        :param activity:
        :return:
        """
        result = cls.call_adb("shell am start -n %s/%s" % (package_name, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    @classmethod
    def get_app_pid(cls, pkg_name):
        """
        根据包名得到进程id
        :param pkg_name:
        :return:
        """
        string = cls.call_adb("shell ps | grep " + pkg_name)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        return result[4]


