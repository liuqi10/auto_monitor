#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import win32gui

# hwnd_title = dict()
# print(hwnd_title)

win = win32gui.FindWindow(None,'DialogName')
print(win)
# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
# data = win32gui.EnumWindows(get_all_hwnd,0)
# print("abc:",data)
#
# for h, t in hwnd_title.items():
#     if t is not "":
#         print(h, t)

import win32clipboard

# import win32gui
# #获取句柄对应的应用程序
# app = win32gui.FindWindow("WISROOM")
# print(app)


