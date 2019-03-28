# -*- coding: utf-8 -*-

import autoit
import time


class PyQtEZLibrary:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        pass

    @staticmethod
    def smart_wait_window(title):
        while True:
            time.sleep(0.7)
            if autoit.win_active(title):
                break

    @staticmethod
    def longin(user, password):
        autoit.win_activate("用户登陆")
        autoit.control_click("用户登陆", "Qt5QWindowIcon7")
        autoit.control_send("用户登陆", "Qt5QWindowIcon7", "{BS}{BS}{BS}{BS}{BS}{BS}{BS}{BS}")
        time.sleep(0.1)
        autoit.control_send("用户登陆", "Qt5QWindowIcon7", user)
        time.sleep(0.1)
        autoit.control_send("用户登陆", "Qt5QWindowIcon1", password)
        time.sleep(0.1)
        autoit.control_click("用户登陆", "Qt5QWindowIcon2")

    @staticmethod
    def switch_window(title):
        while True:
            time.sleep(1)
            if autoit.win_active(title):
                break
        time.sleep(2)
        autoit.win_set_on_top(title)
        time.sleep(6)
        autoit.win_set_on_top(title, 0)


if __name__ == '__main__':
    pyqtez = PyQtEZLibrary()

