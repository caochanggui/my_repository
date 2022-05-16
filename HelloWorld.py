# -*- encoding: utf-8 -*-

# print "HelloWorld!"
#
# birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine',
#  'Apr':'Diamond', 'May':'Emerald'}
# months = birthStones.keys()
# print months
# l = ["{:0>5d}".format(i) for i in range(100)]
# print l
#
#
# d = {1:2,3:5}
# print d.get(1)


# import paramiko
#
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.238.129',port=22,username='root',password='Huawei12#$')
# stdin,stdout,stderr = ssh.exec_command('qs -ux')
# print stdout.read()
#
#
# class Person():
#     name = "ccg"
#     def mymethod(self):
#         print ("hello",self.name)
# p1 = Person()
# p1.name = "zc"
# p1.mymethod()

# l = eval("0x452//2")
# # print(l)


# l = ["123","456",["189","556"]]
# # from itertools import chain
#
# # a = chain.from_iterable(l)
# # print(list(a))
#
# s = ''.join(a for a in l)
# print(s)
# import PyPDF2
#
# pdfFileObj = open('ccg.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pageObj = pdfReader.getPage(0)
# contxt = pageObj.extractText()
# print(contxt)

# def extendlist(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendlist(10)
# list2 = extendlist(123,[])
# list3 = extendlist('a')
# print(list1)
# print(list2)
# print(list3)
#
# import itertools
# i = 0
# for item in itertools.count(100,2):
#     i += 1
#     if i >10:
#         break
# print(i)
#
# booleans = [1,0,1,0,0,1]
# print(list(itertools.filterfalse(None,booleans)))
#
# numbers = [23,20,44,32,7,12]
# print(list(itertools.filterfalse(lambda x:x<20,numbers)))

# import unittest
# # from MathFunc import *
#
#
# class TestMathFunc(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(3,3)
#         print("test add")
#
#     # @unittest.skip('test skip')
#     def test_multi(self):
#         self.assertEqual(6,6)
#         print("test multi")
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("test setUpClass")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("test tearDownClass")
#
#     def setUp(self) -> None:
#         print("test setUp")
#
#     def tearDown(self) -> None:
#         print("test tearDown")
#
#
# if __name__ == '__main__':
#     unittest.main()
# import random
# random.seed(10)
# print(random.randrange(10,100,10))
# random.seed(10)
# print(random.randrange(10,100,10))

# print(random.seed(10))
# print(random.randint(10,100))
# print(random.seed(10))
# print(random.randint(10,100))

# print(12/2)
#
# dic = {
#     "motorlist":{
#         "motorid":"123"
#     }
# }
# res = dic.get("motorlist")
# print(res)
#
# class Repostory:
#     def __init__(self):
#         self.objs_repo = list()
#
#     def __len__(self):
#         return len(self.objs_repo)/10
#
#     def __bool__(self):
#         return len(self.objs_repo)
#
#     def __setitem__(self, key, value):
#         self.objs_repo.append((key,value))
#
#     def __getitem__(self, index):
#         print(index,len(self.objs_repo))
#         return None if index >=len(self.objs_repo) else self.objs_repo[index]
#
# repo_obj = Repostory()
# repo_obj[0] = "zero"
# # if len(repo_obj):
# #     print(repo_obj)
#
# if repo_obj:
#     print(repo_obj)

# print(sorted([111,1,3], key=str))
#
# print(int(12,345))

# def control_statement_in_finally(param):
#     ret = -1
#     try:
#         ret = 1/param
#     finally:
#         return ret
#
# print(control_statement_in_finally(0))


# import sys
# import re
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open('cc', encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start()+1
#             location = (line_no, column_no)
#             # 这其实是一种很不好的实现，这样写只是为了证明论点
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
# # 以字母顺序打印出结果
# for word in sorted(index, key=str.upper):
#     print(word, index[word])

# index = {}
# index.setdefault("id","123")
# print(index)

# l = [1,2,3,4,5]
# for i in l:
#     l.remove(i)
# print(l)

# viidgws = {
#     "viidgw":"1.1.1.1",
#     "viidgw1":"1.1.1.2",
#     "viidgw2":"1.1.1.3",
#     "va":"1.1.1.3",
#     "dpc":"1.1.1.3",
# }
# gws = [viidgws[viid] for viid in viidgws.keys() if "viidgw" in viid]
# print(gws)

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.238.129',22,"root","Huawei12#$")

stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.readlines())
ssh.close()