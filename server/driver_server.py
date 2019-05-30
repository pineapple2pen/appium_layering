# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 15:42
# @File   : driver_server.py
import time
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class DriverServer(object):
    # todo封装操作
    def __init__(self, driver: Remote):
        self.driver = driver

    def __call__(self, func_name, *args, **kwargs):
        return self.__getattribute__(func_name)(*args, **kwargs)

    def get_element(self, selector: str, timeout=30):
        """
        获取页面元素
        :param selector:
        :param timeout:
        :return:
        """
        driver = self.driver
        if selector.startswith("//"):
            return WebDriverWait(driver, timeout).until(lambda a: a.find_element_by_xpath(selector))
        elif ":id/" in selector:
            return WebDriverWait(driver, timeout).until(lambda a: a.find_element_by_id(selector))
        else:
            raise Exception("selector error:" + selector)

    def get_elements(self, selector: str, timeout=30):
        """
        获取页面元素list
        :param selector:
        :param timeout:
        :return:
        """
        driver = self.driver
        if selector.startswith("//"):
            return WebDriverWait(driver, timeout).until(lambda a: a.find_elements_by_xpath(selector))
        elif "id:/" in selector:
            return WebDriverWait(driver, timeout).until(lambda a: a.find_elements_by_id(selector))
        else:
            raise Exception("selector error")

    def get_element_by_parent_element(self, parent_sel, child_sel, timeout=30):
        """
        通过父元素选择子元素
        :param parent_sel:
        :param child_sel:
        :param timeout:
        :return:
        """
        parent_ele = self.get_element(parent_sel)
        if child_sel.startswith("//"):
            return WebDriverWait(parent_ele, timeout).until(lambda a: a.find_elements_by_xpath(child_sel))
        elif "id:/" in child_sel:
            return WebDriverWait(parent_ele, timeout).until(lambda a: a.find_elements_by_id(child_sel))

    def element_status(self, ele):
        """
        元素状态
        :param ele:
        :return:
        """
        try:
            self.get_element(ele, timeout=0)
            return True
        except TimeoutException:
            return False

    def click_ele(self, ele):
        """
        点击
        :param ele:
        :return:
        """
        self.get_element(ele).click()
        return self

    def type(self, ele, text):
        """
        输入
        :param ele:
        :param text:
        :return:
        """
        self.get_element(ele).send_keys(text)
        return self

    def slide_screen(self, start_x, start_y, end_x, end_y, slide_time=None):
        """
        滑动屏幕
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param slide_time:
        :return:
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, slide_time)
        return self

    def click_exist(self, ele):
        """
        存在则点击
        :param ele:
        :return:
        """
        if self.element_status(ele):
            self.click_ele(ele)

    def click_gone(self, ele, click_wait=0.5):
        """
        一直点击直到消失
        :param ele:
        :param click_wait: 点击间隔
        :return:
        """
        while self.element_status(ele):
            self.click_ele(ele)
            time.sleep(click_wait)

    def wait_gone(self, ele, timeout=10):
        """
        等待元素消失
        :param ele:
        :param timeout:
        :return: 等待时间
        """
        start_time = time.time()
        end_time = start_time + timeout
        while self.element_status(ele):
            if time.time() > end_time:
                raise TimeoutException
            else:
                time.sleep(0.5)
        return time.time() - start_time
