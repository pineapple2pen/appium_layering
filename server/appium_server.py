# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 10:11
# @File   : appium_server.py
import os
import socket
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import time
import platform
import subprocess
import threading


class AppiumServer:

    def __init__(self, kwargs=None):
        """
        根据传递的信息，启动主机上的appium服务，支持多个启动
        该服务源代码来自git开源appium移动测试框架，稍加修改
        :param kwargs:执行信息list
        """
        self.kwargs = kwargs

    def start_server(self):
        """
        启动appium服务
        :return:
        """
        for i in range(0, len(self.kwargs)):
            cmd = "appium --session-override  -p %s -bp %s -U %s" % (
                self.kwargs[i]["port"], self.kwargs[i]["bport"], self.kwargs[i]["devices"])
            print(cmd)

            # windows下启动server
            if platform.system() == "Windows":
                t1 = RunServer(cmd)
                p = Process(target=t1.start())
                p.start()
                print("start check win appium server status")
                while True:
                    if self.win_is_runnnig("http://127.0.0.1:" + self.kwargs[i]["port"] + "/wd/hub" + "/status"):
                        print("start win appium server start success")
                        break
            else:
                appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                          close_fds=True)
                print("start check appium server status")
                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    time.sleep(1)
                    if 'listener started' in appium_line or 'Error: listen' in appium_line:
                        print("start appium server success")
                        break

    @staticmethod
    def win_is_running(url):
        """
        检查 appium server 是否启动成功
        :param url:
        :return:
        """
        response = None
        time.sleep(1)
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        except socket.timeout:
            return False
        finally:
            if response:
                response.close()

    @staticmethod
    def stop_server(devices):
        """
        停止appium服务
        :param devices:
        :return:
        """
        sys_str = platform.system()

        if sys_str == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                # mac
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plist_tmp = plist[1].split("    ")
                plists = plist_tmp[1].split(" ")
                os.popen("kill -9 {0}".format(plists[0]))


class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)
