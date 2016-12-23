#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
from loginFrom import LoginFrom


if __name__ == "__main__":

    root = Tkinter.Tk()

    login_from = LoginFrom(root)
    login_from.create_from()
    # login_from.create_mainFrom()

    root.mainloop()
