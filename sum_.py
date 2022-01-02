# -*- encoding: utf-8 -*-
# @Time    :2021/12/19 13:22
# @Author  :Jim
# @FileName:sum_.py
# @Software:PyCharm


# import openpyxl
# from openpyxl.utils import get_column_letter,column_index_from_string
#
# wb = openpyxl.load_workbook('LB_BAK.xlsx')
# sheet = wb.get_sheet_by_name('机动车')
# row = sheet.max_row
# column = sheet.max_column
# print(row,column)
# sheet['D8'] = "曹长贵"
# wb.save('LB_BAK.xlsx')
# print(get_column_letter(10))
# print(column_index_from_string('AF'))


import re
# with open('user_pwd.txt','r',encoding='utf-8') as file:
#     cont = file.read()
cont = '''172.22.8.207 - - [16/Dec/2014:17:57:35 +0800] "GET /report?DOmjjuS6keWJp+WculSQAgdUkAIPODExMzAwMDJDN0FC HTTP/1.1" 200 0 "-" "XXXXXXX/1.0.16; iPhone/iOS 8.1.2; ; 8DA77E2F91D0"'''
print(cont)
pattern = re.compile(r'GET ([\w\/\?\+ ]+) HTTP')
matchobj = pattern.findall(cont)
# print(matchobj.group())
print(matchobj)


# import threading
# import time
#
# # start = time.strftime("%Y%m%d%H%M%S")
# start = time.time()
# lock = threading.RLock()
# num = 0
# def a():
#     global num
#     while True:
#         if num>10000:
#             break
#         lock.acquire()
#         num = num + 1
#         print(num)
#         lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=a)
#     t.start()
#     t.join()
# print(time.time()-start)



