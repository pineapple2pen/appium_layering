# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2019/5/29 11:34
# @File   : page.py
import json
import os


class Page:
    name = None
    elements = None
    eles = []

    def __init__(self, page_json):
        if isinstance(page_json, str):
            page_json = json.loads(page_json, encoding="utf-8")
        if isinstance(page_json, dict):
            self.name = page_json["name"]
            self.elements = page_json["elements"]
            self._element_format()

    def _element_format(self):
        if isinstance(self.elements, list):
            for ele in self.elements:
                self.eles.append(ele["id"])
                setattr(self, ele["id"], ele)

    def get_element(self, ele_id):
        if ele_id in self.eles:
            return getattr(self, ele_id)
        else:
            raise Exception("unknown element id")

    @staticmethod
    def get_page(config, page_name):
        file_path = config.project_path + "\\page_config\\" + page_name + ".json"
        if os.path.isfile(file_path):
            with open(file_path, "r+", encoding="utf-8") as f:
                return Page(f.read())
        else:
            raise Exception("page not exists")


if __name__ == "__main__":
    pass
    # page = Page.get_page(Config(), "startPage")
    # print(page.eles)
