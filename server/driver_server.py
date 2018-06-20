# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/6/15 15:42
# @File   : driver_server.py
from appium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


class DriverServer:
    # todo封装操作
    def __init__(self, driver: Remote):
        self.driver = driver
        self.touch_action = TouchAction(self.driver)

    def get_element(self, selector: str):
        driver = self.driver
        if "," in selector:
            selector = selector.split(",")
            if selector[0] == "i":
                return driver.find_element_by_id(selector[1])
            elif selector[0] == "cn":
                return driver.find_element_by_class_name(selector[1])
            elif selector[0] == "lt":
                return driver.find_element_by_link_text(selector[1])
            elif selector[0] == "cs":
                return driver.find_element_by_css_selector(selector[1])
            elif selector[0] == "ai":
                return driver.find_element_by_accessibility_id(selector[1])
            elif selector[0] == "n":
                return driver.find_element_by_name(selector[1])
            elif selector[0] == "au":
                return driver.find_element_by_android_uiautomator(selector[1])
        else:
            if selector.startswith("//"):
                return driver.find_element_by_xpath(selector)
            elif "id:/" in selector:
                return driver.find_element_by_id(selector)

    def get_elements(self, selector: str):
        driver = self.driver
        if "," in selector:
            selector = selector.split(",")
            if selector[0] == "i":
                return driver.find_elements_by_id(selector[1])
            elif selector[0] == "cn":
                return driver.find_elements_by_class_name(selector[1])
            elif selector[0] == "lt":
                return driver.find_elements_by_link_text(selector[1])
            elif selector[0] == "cs":
                return driver.find_elements_by_css_selector(selector[1])
            elif selector[0] == "ai":
                return driver.find_elements_by_accessibility_id(selector[1])
            elif selector[0] == "n":
                return driver.find_elements_by_name(selector[1])
            elif selector[0] == "au":
                return driver.find_elements_by_android_uiautomator(selector[1])
        else:
            if selector.startswith("//"):
                return driver.find_elements_by_xpath(selector)
            elif "id:/" in selector:
                return driver.find_elements_by_id(selector)

    def get_element_by_parent_element(self, parent_sel, child_sel):
        parent_ele = self.get_element(parent_sel)
        if "," in child_sel:
            selector = child_sel.split(",")
            if selector[0] == "i":
                return parent_ele.find_elements_by_id(child_sel[1])
            elif selector[0] == "cn":
                return parent_ele.find_elements_by_class_name(child_sel[1])
            elif selector[0] == "lt":
                return parent_ele.find_elements_by_link_text(child_sel[1])
            elif selector[0] == "cs":
                return parent_ele.find_elements_by_css_selector(child_sel[1])
            elif selector[0] == "ai":
                return parent_ele.find_elements_by_accessibility_id(child_sel[1])
            elif selector[0] == "n":
                return parent_ele.find_elements_by_name(child_sel[1])
            elif selector[0] == "au":
                return parent_ele.find_elements_by_android_uiautomator(child_sel[1])
        else:
            if child_sel.startswith("//"):
                return parent_ele.find_elements_by_xpath(child_sel)
            elif "id:/" in child_sel:
                return parent_ele.find_elements_by_id(child_sel)

    def element_status(self, ele):
        try:
            self.get_element(ele)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def click_ele(self, ele):
        self.get_element(ele).click()
        return self

    def type(self, ele, text):
        self.get_element(ele).send_keys(text)
        return self

    def slide_screen(self, start_x, start_y, end_x, end_y, slide_time=None):
        self.driver.swipe(start_x, start_y, end_x, end_y, slide_time)
        return self


