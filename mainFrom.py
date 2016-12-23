#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import tkFileDialog
import tkMessageBox
import ttk

from public import center_window


class MainFrom(object):
    """应用窗体"""

    def __init__(self, master):
        self.master = master

    def init_from(self):
        self.create_menu()
        self.create_canvas()
        self.creat_input()

    def create_menu(self):
        # 创建菜单
        menu = Tkinter.Menu(self.master)

        # "文件" 二级菜单
        filemenu = Tkinter.Menu(menu, tearoff=0)
        filemenu.add_command(label="新建", command=self.create_canvas)
        filemenu.add_command(label="打开", command=self.open_file)
        filemenu.add_command(label="保存", command=self.hello)
        filemenu.add_separator()  # 分割线
        filemenu.add_command(label="退出", command=self.master.quit)
        menu.add_cascade(label="文件", menu=filemenu)

        # "帮助" 菜单
        helpmenu = Tkinter.Menu(menu, tearoff=0)
        helpmenu.add_command(label="关于", command=self.about)
        menu.add_cascade(label="帮助", menu=helpmenu)

        self.master.config(menu=menu)

    def create_canvas(self):
        canvas = Tkinter.Canvas(self.master, bg='blue', height=200, width=200)
        coord = 10, 50, 240, 210
        # arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
        # canvas.grid(row=0, column=3, rowspan=5)

        # canvas.pack(side=Tkinter.LEFT)

    def creat_input(self):
        v = Tkinter.StringVar()
        Tkinter.Label(self.master, text="环绕文字").grid(
            sticky=Tkinter.E, row=0, column=0, pady=4, padx=3)
        Tkinter.Label(self.master, text="文字间距").grid(
            sticky=Tkinter.E, row=2, column=0, pady=4, padx=3)

        font1 = Tkinter.Entry(self.master, width=30)
        font1.grid(row=0, column=1, sticky=Tkinter.W)
        spacing = Tkinter.Spinbox(
            self.master, from_=0, to=10, width=5, increment=0.1, textvariable=v)
        v.set(5.0)
        spacing.grid(row=2, column=1, sticky=Tkinter.W)

        Tkinter.Label(self.master, text="中心图符").grid(
            sticky=Tkinter.E, row=3, column=0, pady=4, padx=3)
        center = ttk.Combobox(self.master, values=("五角星", "国徽"), width=7)
        center.grid(row=3, column=1, sticky=Tkinter.W)
        center.current(0)

        # butt = Tkinter.Button(self.master, text="press", command=self.hello)
        # butt.grid(row=2, column=4)

    def hello(self):
        la1 = Tkinter.Label(self.master, text="First")
        la2 = Tkinter.Label(self.master, text="Second")
        la1.pack()
        la2.pack()

        e1 = Tkinter.Entry(self.master)
        e2 = Tkinter.Entry(self.master)

        e1.pack()
        e2.pack()

    def open_file(self):
        # fd = FileDialog.LoadFileDialog(self.master)
        filename = tkFileDialog.askopenfilename(initialdir="C:")
        # filename = fd.go()

    def about(self):
        tkMessageBox.showinfo(title='关于', message="印章样式在线生成平台\n QQ 1205352402")


if __name__ == "__main__":
    root = Tkinter.Tk()
    center_window(root, 600, 420)
    root.title("印章样式在线生成平台")
    root.geometry("600x420")  # 设置窗口大小
    # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
    root.resizable(width=False, height=False)
    mainfrom = MainFrom(root)
    mainfrom.init_from()
    root.mainloop()
