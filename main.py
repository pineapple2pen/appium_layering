# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2019/2/12 10:12
# @File   : main.py
import os


def load_sys_file_path():
    project_path = ".."
    config_file_name = "config.ini"
    apk_name = "suishouji_1059000.apk"
    test_case_name = "TestCase.xlsx"
    file_path_dir = {}
    for path, subdir, files in os.walk(project_path):
        coincide_file = set(files) & {config_file_name, apk_name, test_case_name}
        if len(coincide_file) > 0:
            for file in coincide_file:
                file_path_dir[file.split(".")[1]] = os.path.abspath(path + "\\" + file)
    print(file_path_dir)


if __name__ == "__main__":
    load_sys_file_path()
