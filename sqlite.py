#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
basePath=os.path.dirname(__file__)

class UseSqlite:

    def __init__(self):
        # 关于数据库的操作
        self.sqlite = sqlite3.connect(os.path.join(basePath, "db.sqlite3"))
        self.cursor = self.sqlite.cursor()

    def creat_table(self):
        # 创建管理员表
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin (
            id integer primary key,
            username varchar(10) UNIQUE,
            password varchar(16)
            )
            """)

    def create_admin(self, username, password):
        # 创建管理员
        self.cursor.execute("""
            select count(*) from admin
            """)
        hasadmin = self.cursor.fetchone()[0]
        print hasadmin
        try:
        	# sqlite 占位符：问号和命名占位符（命名样式）
            self.cursor.execute("""
                insert into admin values (?, ?, ?)
                """, (hasadmin+1, username, password))
            self.sqlite.commit()
        except Exception as err:
            print err
            self.sqlite.rollback()  # 数据库回滚


if __name__ == "__main__":
	# 初次使用创建表结构和用户
    userdata = UseSqlite()
    userdata.creat_table()
    userdata.create_admin("wen", "123456")
