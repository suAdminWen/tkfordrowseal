#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter


def center_window(root, width, height):
        # 将窗体居屏幕中间
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth -
                                            width) / 2, (screenheight - height) / 2)
    root.geometry(size)