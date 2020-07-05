#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   MysqlHelper.py
@Time    :   2020/06/30 22:39:22
@Author  :   iceld 
@Version :   1.0
@Contact :   dabller888@163.com
@License :   (C)Copyright 2020-2022
@Desc    :   None
'''


# here put the import lib
import MySQLdb as mysql
import json

class mysqlHelper:
    __conn = None
    connected = False

    def __init__(self):
        self.__conn = mysql.connect(
            db='mysql',
            user='root',
            passwd='toor',
            host='localhost',
            port=3306)

    def __def__(self):
        self.__conn.close()

    def fetch_all(self, sql):
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                self.__conn.commit()
                return cursor.fetchall()
        except mysql.Error as e:
            print(e)
            return False

    def update(self, sql):
        print(sql)
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                self.__conn.commit()
                return True
        except mysql.Error as e:
            print(e)
            return False

if __name__ == "__main__":
    sqlHelper = mysqlHelper()
    user = sqlHelper.fetch_all('select * from user')
    print(type(user))
    print(str(user))
