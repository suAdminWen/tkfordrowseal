#!/usr/bin/python
# -*- coding: UTF-8 -*-

from mainFrom import MainFrom
from public import center_window

import Tkinter
import tkMessageBox
import sqlite3
import os

basePath = os.path.dirname(__file__)

connect = sqlite3.connect(os.path.join(basePath, "db.sqlite3"))
cursor = connect.cursor()


class LoginFrom(object):
    def __init__(self, root):
        # 创建登录窗体
        self.root = root
        self.root.title("印章样式在线生成平台")
        self.root.geometry("220x150")  # 设置窗口大小
        # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        self.root.resizable(width=False, height=False)

    def create_from(self):
        # 创建输入框和提交按钮

        center_window(self.root, 220, 150)  # 将登陆窗口居中
        string = Tkinter.StringVar()
        var = Tkinter.IntVar()

        Tkinter.Label(self.root, width=7, text="登录名").grid(
            sticky=Tkinter.E, column=0, pady=13)
        Tkinter.Label(self.root, text="密码").grid(sticky=Tkinter.E, column=0)

        username = Tkinter.Entry(self.root)
        password = Tkinter.Entry(self.root, textvariable=string)

        username.grid(row=0, column=1, columnspan=2)
        password.grid(row=1, column=1, columnspan=2)

        username.focus_set()  # 使文本域获取焦点
        password['show'] = '*'  # 设置密码域输入为隐藏

        checkbutton = Tkinter.Checkbutton(
            self.root, text='记住密码', variable=var, command=lambda: self.remember(var))
        checkbutton.grid(column=1, columnspan=2, sticky=Tkinter.W)
        checkbutton.select()

        Tkinter.Button(self.root, text="注冊", width=5, command=lambda: self.login(username, password)).grid(
            row=4, columnspan=2)
        Tkinter.Button(self.root, text="登录", width=5, command=lambda: self.login(username, password)).grid(
            row=4, column=2)

    def remember(self, var):
        # 用户请求是否记住密码
        isRemember = var.get()  # 获取该次复选按钮的值
        print isRemember
        if isRemember:
            print "用户请求记住密码"
        else:
            print "用户请求不记住密码"

    def login(self, username, password):
        # type: (object, object) -> object
        # 登录判断
        username = username.get()
        password = password.get()
        if username == "" or password == "":
            # 消息弹窗
            tkMessageBox.showinfo(title='提示信息', message="用户名或密码不能为空")
            return
        validation = self.validation(username, password)
        if validation:
            self.root.destroy()  # 销毁当前的登录窗体
            self.create_mainFrom()  # 创建主程序窗体
        else:
            tkMessageBox.showinfo(title='提示信息', message="用户名不存在或密码错误")
            return

    def validation(self, username, password):
        # 登录的帐号密码进行认证
        cursor.execute("""
            select count(*) 
            from admin
            where username=? and password=?
            """, (username, password))
        adminLen = cursor.fetchone()[0]
        if adminLen > 0:
            return 1
        else:
            return 0

    def create_mainFrom(self):
        # 创建主窗体
        root = Tkinter.Tk()
        center_window(root, 600, 420)
        root.title("印章样式在线生成平台")
        root.geometry("600x420")  # 设置窗口大小
        # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        root.resizable(width=False, height=False)
        mainfrom = MainFrom(root)
        mainfrom.init_from()
