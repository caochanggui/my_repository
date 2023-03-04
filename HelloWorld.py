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

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.238.129',22,"root","Huawei12#$")
#
# stdin, stdout, stderr = ssh.exec_command("ls")
# print(stdout.readlines())
# ssh.close()

# import os
# import sys
# name = sys.argv[1]
# print(name)

# str1 = 'pickle'
# print(str1.center(10,"0"))
#
# s = "PYTHON"
# print("{0:10}111".format(s))

# s = "123aa"
# print(type(s.split('2')))

# import subprocess
# subprocess.run(["notepad.exe", "C:\\Users\\jim\\abc.txt"],shell=True)

# viidgws = {
#     "viidgw":"1.1.1.1",
#     "viidgw1":"1.1.1.2",
#     "viidgw2":"1.1.1.3",
#     "va":"1.1.1.3",
#     "dpc":"1.1.1.3",
# }
#
# del viidgws
# print(viidgws)

# def scope_test():
#     def do_local():
#         spam = "我是局部变量"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "我不是局部变量，也不是全局变量"
#     def do_global():
#         global spam
#         spam = "我是全局变量"
#     spam = "原来的值"
#     do_local()
#     print("局部变量赋值后：",spam)
#     do_nonlocal()
#     print("nonlocal变量赋值后：", spam)
#     do_global()
#     print("全局变量赋值后：", spam)
# scope_test()
# print("全局变量：",spam)

# import subprocess
#
# def run_cmd_wrong(_directory):
#     return subprocess.check_output("notepad.exe {:s}".format(_directory),shell=False)
#
# if __name__ == '__main__':
#     _out = run_cmd_wrong("d:/1.txt && calc.exe")

# class people:
#     name = ''
#     age = 0
#     __wight = 0
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__wight = w
#     def speak(self):
#         print("%s 说： 我%d。"% (self.name,self.age))
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print("%s 说：我%d岁了，我在读%d年级"%(self.name,self.age,self.grade))
# class speaker(people):
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫%s,我是一个演说家，我演讲的主题是%s"%(self.name,self.topic))
# class sample(student,speaker):
#     def __init__(self,n,a,w,g,t):
#         speaker.__init__(self,n,t)
#         student.__init__(self,n,a,w,g)
#
# if __name__ == '__main__':
#     test = sample("Tim",25,80,4,"python")
#     test.speak()
# -*- coding:utf-8 -*-
# @Time   : 2022-02-23
# @Author : carl_DJ

# from PIL import Image
# from itertools import product
# import fitz
#
#
# # 去除pdf的水印
# def remove_pdfwatermark():
#     # 打开源pfd文件
#     pdf_file = fitz.open("flask-docs.pdf")
#
#     # page_no 设置为0
#     page_no = 0
#     # page在pdf文件中遍历
#     for page in pdf_file:
#         # 获取每一页对应的图片pix (pix对象类似于我们上面看到的img对象，可以读取、修改它的 RGB)
#         # page.get_pixmap() 这个操作是不可逆的，即能够实现从 PDF 到图片的转换，但修改图片 RGB 后无法应用到 PDF 上，只能输出为图片
#         pix = page.get_pixmap()
#
#         # 遍历图片中的宽和高，如果像素的rgb值总和大于510，就认为是水印，转换成255，255,255-->即白色
#         for pos in product(range(pix.width), range(pix.height)):
#             if sum(pix.pixel(pos[0], pos[1])) >= 510:
#                 pix.set_pixel(pos[0], pos[1], (255, 255, 255))
#         # 保存去掉水印的截图
#         pix.pil_save(f"./{page_no}.png", dpi=(30000, 30000))
#         # 打印结果
#         print(f'第 {page_no} 页去除完成')
#
#         page_no += 1
#
#
# if __name__ == '__main__':
#     remove_pdfwatermark()

# for item in zip([1,2,3],[4,5,6]):
#     print(item)
#
# for item in zip(*zip([1,2,3],[4,5,6])):
#     print(item)
# from collections import deque
#
#
# def search(lines, pattern, history=3):
#     previous_lines = deque(maxlen=history)
#     for li in lines:
#         if pattern in li:
#             yield li, previous_lines
#     previous_lines.append(li)
#
#
# # Example use on a file
# if __name__ == '__main__':
#     with open(r'config.ini') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-' * 20)
# from collections import deque
#
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# print(q.popleft())
# print(q)
# import heapq
#
# portfolio = [{
#     "name": "IMB",
#     "age": 16,
#     },
#     {
#         "name": "IMB",
#         "age": 15,
#     },
#     {
#         "name": "IMB",
#         "age": 112,
#     },
# ]
# l = heapq.nlargest(2,portfolio,key=lambda x:x["age"])
# print(l)

# from PyPDF4 import PdfFileReader, PdfFileWriter
# from PyPDF4.pdf import ContentStream
# from PyPDF4.generic import TextStringObject, NameObject
# from PyPDF4.utils import b_
#
# def removeWatermark(wm_text, inputFile, outputFile):
#     with open(inputFile, "rb") as f:
#         source = PdfFileReader(f, "rb")
#         output = PdfFileWriter()
#         for page in range(source.getNumPages()):
#             page = source.getPage(page)
#             content_object = page["/Contents"].getObject()
#             content = ContentStream(content_object, source)
#             for operands, operator in content.operations:
#                 if operator == b_("Do"):
#                     text = operands[0]
#                     if isinstance(text, str) and text.startswith(wm_text):
#                         operands[0] = TextStringObject('')
#                         page.__setitem__(NameObject('/Contents'), content)
#                         output.addPage(page)
#
#                         with open(outputFile, "wb") as outputStream:
#                             output.write(outputStream)
#
# wm_text = '尚学堂.百战程序员'
# inputFile = r'Python.pdf'
# outputFile = r"output.pdf"
#
# removeWatermark(wm_text, inputFile, outputFile)
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#             print("end")
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))

# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
# slice(1,5)
# l = list(range(10))
# print(l[slice(1,5)])

# words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the','eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]
# from collections import Counter
#
# word_count = Counter(words)
# print(word_count.most_common(1))
# portfolio = [{
#     "name": "IMB",
#     "age": 16,
#     },
#     {
#         "name": "IMB",
#         "age": 15,
#     },
#     {
#         "name": "IMB",
#         "age": 112,
#     },
# ]
#
# print([folio["name"] for folio in portfolio if folio["age"]==112])

# import unicodedata
#
# print(unicodedata.digit(chr(2)))
# l = [str(i).rjust(5,"0")for i in range(100)]
# l = [format(str(i),'0>5s')for i in range(100)]
# l = '{:>10s}'.format('11')
# def sample():
#     yield 'Is'
#     yield 'Chicago'
#     yield 'Not'
#     yield 'Chicago?'
# # print([i for i in sample()])
# print(list(sample()))
#
#
# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size += len(part)
#         if size > maxsize:
#             yield ''.join(parts)
#             parts = []
#             size = 0
#         yield ''.join(parts)
# # 结合文件操作
# with open('filename', 'w')as f:
#     for part in combine(sample(), 32768):
#         f.write(part)
# l = 1
# print(vars()["l"])
# class Info:
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
# a = Info("Guido", 37)
# name = "Guido"
# age = 37
# del age
# class safesub(dict):
#     def __missing__(self, key):
#         return '{' + key + '}'
# s = '{name} has {n}messages.'
# print(s.format_map(safesub(vars())))
# import sys
# print(sys._getframe(0).f_locals)
# print(vars())
# import os
# print(os.get_terminal_size().columns)
# s = 'Elements are written as "<tag>text</tag>".'
# from html.parser import HTMLParser
# p = HTMLParser()
# print(p.unescape(s))

_formats = {'ymd': '{d.year}-{d.month}-{d.day}', 'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}/{d.month}/{d.year}'}


# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)
#
# d = Date(2012, 12, 21)
# print(format(d))
#
# print('The date is {:ymd}'.format(d))
# print(format(d,'ymd'))
# class Person:
#     def __init__(self, name):
#         self.name = name
#     # Getter function
#     @property
#     def name(self):
#         return self._name
#     # Setter function
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._name = value
#     # Deleter function
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
# p = Person('ccg')
# print(p.name)
#
# class SubPerson(Person):
#     @Person.name.getter
#     def name(self):
#         print('Gettingname')
#         return super().name
#
#     @Person.name.setter
#     def name(self, value):
#         print('Settingname to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)
#
#     @name.deleter
#     def name(self):
#         print('Deletingname')
#         super(SubPerson, SubPerson).name.__delete__(self)
# s = SubPerson('Guido')
# print(s.name)

#Descriptor attributeforan integer type-checked attribute
# class Integer:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError('Expected an int')
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#
# class Point:
#     x = Integer('x')
#     y = Integer('y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(2, 3)
# class lazyproperty:
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value)
#             return value
#
#
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @ lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius ** 2
#
#     @ lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2 * math.pi * self.radiu
# c = Circle(4.0)
# c.area
# c.area

# import math
# class Structure1:
# # Class variable that specifies expectedfields
#     _fields = []
#
#     def __init__(self,*args):
#         if len(args) != len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#             # Set the arguments
#         for name, value in zip(self._fields,args):
#             setattr(self, name, value)
#
# # Example class definitions
# class Stock(Structure1):
#     _fields = ['name','shares', 'price']
# Stock('ACME', 50, 91.1)
# class Structure2:
#     _fields = []
#     def __init__(self, *args, **kwargs):
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Set all of the positional arguments
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#         # Set the remaining keyword arguments
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#         # Check for anyremaining unknown arguments
#         if kwargs:
#             raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
# # Example use
# if __name__ == '__main__':
#     class Stock(Structure2):
#         _fields = ['name','shares', 'price']
#     s1 = Stock('ACME',50,91.1)
#     print(s1.__dict__.update({"ccg" : 34}))
#     print(s1.__dict__)
#     s2 = Stock('ACME',50,price=91.1)
#     s3 = Stock('ACME',shares=50, price=91.1)
#     # s3 = Stock('ACME', shares=50, price=91.1, aa=1)

# import collections
# import bisect
#
# class SortedItems(collections.Sequence):
#     def __init__(self, initial=None):
#         self._items = sorted(initial) if initial is not None else []
#
#     # Required sequencemethods
#     def __getitem__(self, index):
#         return self._items[index]
#
#     def __len__(self):
#         return len(self._items)
#
#     # Method for addinganitem in the rightlocation
#     def add(self, item):
#         bisect.insort(self._items, item)
#
# items = SortedItems([5,1,3])
# print(list(items))
# print(items[0], items[-1])
# items.add(2)
# print(list(items))
# import time
# t = time.localtime()
# t.tm_yday
# from collections import defaultdict
#
# result = defaultdict(int)
# data = [("Type","01"),("Type","02")]
# for (key,value) in data:
#     result[key] += 1
# print(result)

# import types
#
# class Node:
#     pass
#
# class NodeVisitor:
#     def visit(self, node):
#         stack = [node]
#         last_result = None
#         while stack:
#             try:
#                 last = stack[-1]
#                 if isinstance(last, types.GeneratorType):
#                     stack.append(last.send(last_result))
#                     last_result = None
#                 elif isinstance(last, Node):
#                     stack.append(self._visit(stack.pop()))
#                 else:
#                     last_result = stack.pop()
#             except StopIteration:
#                 stack.pop()
#         return last_result
#
#
#     def _visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
#
# class UnaryOperator(Node):
#     def __init__(self,operand):
#         self.operand =operand
# class BinaryOperator(Node):
#     def __init__(self,left, right):
#         self.left = left
#         self.right = right
# class Add(BinaryOperator):
#     pass
# class Sub(BinaryOperator):
#     pass
# class Mul(BinaryOperator):
#     pass
#
# class Div(BinaryOperator):
#     pass
#
# class Negate(UnaryOperator):
#     pass
# class Number(Node):
#     def __init__(self, value):
#         self.value = value  # Asample visitor class that evaluates expressions
# class Evaluator(NodeVisitor):
#     def visit_Number(self,node):
#         return node.value
#     def visit_Add(self,node):
#         return self.visit(node.left) + self.visit(node.right)
#     def visit_Sub(self,node):
#         return self.visit(node.left) - self.visit(node.right)
#     def visit_Mul(self,node):
#         return self.visit(node.left) * self.visit(node.right)
#     def visit_Div(self,node):
#         return self.visit(node.left) / self.visit(node.right)
#     def visit_Negate(self,node):
#         return -self.visit(node.operand)
# if __name__ == '__main__':
#     # 1 + 2*(3-4) / 5
#     t1 = Sub(Number(3),Number(4))
#     t2 = Mul(Number(2),t1)
#     t3 = Div(t2, Number(5))
#     t4 = Add(Number(1),t3)
#     # Evaluate it
#     e = Evaluator()
#     print(e.visit(t4)) # Outputs 0.6
# import time
# from functools import wraps
#
# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         # return result
#     return wrapper
# @timethis
# def coundown(n):
#     while(n>0):
#         n = n - 1
# coundown(100000)
# def ccg():
#     print(ccg.__name__)
# print(ccg())

# from functools import wraps, partial
# import logging
# # Utility decorator toattach a function asan attribute of obj
# def attach_wrapper(obj,func=None):
#     if func is None:
#         return partial(attach_wrapper, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
# def logged(level, name=None, message=None):
#     '''Add logging to a function. level is thelogging level, name is thelogger name, and message is the log message. If name and message aren'tspecified, they default to thefunction's module andname. '''
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             log.log(level,logmsg)
#             return func(*args, **kwargs)
#         # Attach setterfunctions
#         @attach_wrapper(wrapper)
#         def set_level(newlevel):
#             nonlocal level
#             level = newlevel
#         @attach_wrapper(wrapper)
#         def set_message(newmsg):
#             nonlocal logmsg
#             logmsg = newmsg
#         return wrapper
#     return decorate
# # Example use
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam!')
#
# logging.basicConfig(level=logging.DEBUG)
# print(add(2,3))
# add.set_message('Add called')
# print(add(2,3))
#
# from functools import wraps, partial
# import logging
#
# def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
#     if func is None:
#         return partial(logged, level=level, name=name, message=message)
#     logname = name if name else func.__module__
#     log = logging.getLogger(logname)
#     logmsg = message if message else func.__name__
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log.log(level, logmsg)
#         return func(*args, **kwargs)
#     return wrapper
# # Example use
# @logged
# def add(x, y):
#     return x + y
# @logged(level=logging.CRITICAL, name='example')
# def spam():
#     print('Spam!')
# add(5,6)
# spam()


# from inspect import signature
# from functools import wraps
# def typeassert(*ty_args, **ty_kwargs):
#     def decorate(func):
#         # If in optimized mode, disable typechecking
#         if not __debug__:
#             return func
#         # Map function argument names to supplied types
#         sig = signature(func)
#         bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             bound_values = sig.bind(*args, **kwargs)
#             # Enforce type assertions across supplied arguments
#             for name, value in bound_values.arguments.items():
#                 if name in bound_types:
#                     if not isinstance(value,bound_types[name]):
#                         raise TypeError('Argument {} mustbe {}'.format(name, bound_types[name]) )
#             return func(*args, **kwargs)
#         return wrapper
#     return decorate
#
# # @typeassert(int, int, z=int)
# # def spam(x, y, z=42):
# #     print(x, y, z)
# # spam(1, 2, 3)
# @typeassert(int,list)
# def bar(x, items=None):
#     if items is None:
#         items = []
#     items.append(x)
#     return items
# bar(2)
# bar(2,3)

# import types
# from functools import wraps
# class Profiled:
#     def __init__(self,func):
#         wraps(func)(self)
#         self.ncalls = 0
#     def __call__(self,*args, **kwargs):
#         self.ncalls +=1
#         return self.__wrapped__(*args, **kwargs)
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self, instance)
# @Profiled
# def add(x, y):
#     return x + y
# class Spam:
#     @Profiled
#     def bar(self, x):
#         print(self, x)
# add(2,3)
# s = Spam()
# s.bar(2)

# class TestDes:
#     def __get__(self, instance, owner):
#         print(instance, owner)
#         return 'TestDes:__get__'
# class TestMain:
#     ccg = TestDes()
#     def __init__(self):
#         self.des = TestDes()
# if __name__ == '__main__':
#     t = TestMain()
#     print(t.ccg)

# funcs = (lambda x:x+n for n in range(5))
# for f in funcs:
#     print(f(0))
from urllib.request import urlopen
# def urltemplate(template):
#     def opener(**kwargs):
#         return urlopen(template.format_map(kwargs))
#     return opener
# yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))


# def opener(template,**kwargs):
#     return urlopen(template.format_map(kwargs))
#
# yahoo = opener('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}',names='IBM,AAPL,FB', fields='sl1c1v')
# for line in yahoo:
#     print(line.decode('utf-8'))
# def apply_async(func, args, *, callback):
#     # Compute the result
#     result = func(*args)
#     # Invoke the callback with the result
#     callback(result)
#
# def print_result(result):
#     print('Got:', result)
# def add(x, y):
#     return x + y
# def make_handler():
#     sequence = 0
#     while True:
#         result = yield
#         sequence += 1
#         print('[{}] Got: {}'.format(sequence,result))
# handler = make_handler()
# next(handler)
# print(apply_async(add, (2,3),callback=handler.send))

# def generator_two():
#     l = ["{:0>5d}".format(i) for i in range(6)]
#     i = 0
#     while True:
#         x = yield
#         i = i + 1
#         print(l[i])
#         if i == len(l)-1:
#             i = 0
# g = generator_two()
# next(g)
# def post_motor():
#     apeid = g.send(1)
#     return apeid
# for i in range(100):
#     post_motor()
# def apply_async(func, args, *, callback):
#     # Compute the result
#     result = func(*args)
#     # Invoke the callback with the result
#     callback(result)
#
# from queue import Queue
# from functools import wraps
# class Async:
#     def __init__(self,func, args):
#         self.func = func
#         self.args = args
# def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#         f = func(*args)
#         result_queue =Queue()
#         result_queue.put(None)
#         while True:
#             result = result_queue.get()
#             try:
#                 a = f.send(result)
#                 apply_async(a.func, a.args,callback=result_queue.put)
#             except StopIteration:
#                 break
#     return wrapper
# def add(x, y):
#     return x + y
# @inlined_async
# def test():
#     r = yield Async(add, (2, 3))
#     print(r)
#     r = yield Async(add, ('hello', 'world'))
#     print(r)
#     for n in range(10):
#         r = yield Async(add, (n, n))
#         print(r)
#     print('Goodbye')
# test()
# import sys
# print(sys._getframe().f_locals)

# import sys
# class ClosureInstance:
#     def __init__(self, locals=None):
#         if locals is None:
#             locals = sys._getframe(1).f_locals
#         # Update instance dictionary with callables
#         self.__dict__.update((key,value) for key, value in locals.items() if callable(value) )
#     # Redirect specialmethods
#     def __len__(self):
#         return self.__dict__['__len__']()
# # Example use
# def Stack():
#     items = []
#     def push(item):
#         items.append(item)
#     def pop():
#         return items.pop()
#     def __len__():
#         return len(items)
#     return ClosureInstance()
# s = Stack()
# s.push(10)
# s.push(20)
# s.push('Hello')
# print(len(s))
# l = ['{:0>20s}'.format(str(l)) for l in range(10)]
# print(l)
# import csv
# from collections import namedtuple
# with open('stocks.csv','r') as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     Row = namedtuple("Row",headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row.b)

# from urllib.request import urlopen
# from xml.etree.ElementTree import parse
# # Download the RSS feedand parse it
# u =urlopen('http://planet.python.org/rss20.xml')
# doc= parse(u)
# # Extract and output tags of interest
# for item in doc.iterfind('channel/item'):
#     title = item.findtext('title')
#     date = item.findtext('pubDate')
#     link = item.findtext('link')
#     print(title)
#     print(date)
#     print(link)
#     print()
# metro_data = [
# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
# ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
# ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
# ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
# ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
# from collections import namedtuple
# LatLong = namedtuple('LatLog', 'lat log')
# Metropolis = namedtuple('Metropolis', 'name cc pop coord')
# metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
# from operator import attrgetter
# name_lat = attrgetter('name', 'coord.lat')
# for city in sorted(metro_areas,key=attrgetter('coord.lat')):
#     print(name_lat(city))
# from operator import mul
# from functools import reduce
# l = reduce(mul,range(1,4))
# print(l)
# from abc import ABC, abstractmethod
# from collections import namedtuple
# Customer = namedtuple('Customer', 'name fidelity')
# class LineItem:
#     def __init__(self, product, quantity, price):
#         self.product = product
#         self.quantity = quantity
#         self.price = price
#     def total(self):
#         return self.price * self.quantity
# class Order: # 上下文
#     def __init__(self, customer, cart, promotion=None):
#         self.customer = customer
#         self.cart = list(cart)
#         self.promotion = promotion
#     def total(self):
#         if not hasattr(self, '__total'):
#             self.__total = sum(item.total() for item in self.cart)
#         return self.__total
#     def due(self):
#         if self.promotion is None:
#             discount = 0
#         else:
#             discount = self.promotion.discount(self)
#         return self.total() - discount
#     def __repr__(self):
#         fmt = '<Order total: {:.2f} due: {:.2f}>'
#         return fmt.format(self.total(), self.due())
# class Promotion(ABC): # 策略：抽象基类
#     @abstractmethod
#     def discount(self, order):
#         """返回折扣金额（正值）"""
#         pass
# class FidelityPromo(Promotion): # 第一个具体策略
#     """为积分为1000或以上的顾客提供5%折扣"""
#     def discount(self, order):
#         return order.total() * .05 if order.customer.fidelity >= 1000 else 0
# class BulkItemPromo(Promotion): # 第二个具体策略
#     """单个商品为20个或以上时提供10%折扣"""
#     def discount(self, order):
#         discount = 0
#         for item in order.cart:
#             if item.quantity >= 20:
#                 discount += item.total() * .1
#         return discount
# class LargeOrderPromo(Promotion): # 第三个具体策略
#     """订单中的不同商品达到10个或以上时提供7%折扣"""
#     def discount(self, order):
#      distinct_items = {item.product for item in order.cart}
#      if len(distinct_items) >= 10:
#          return order.total() * .07
#      return 0
#
# joe = Customer('John Doe', 0)
# ann = Customer('Ann Smith', 1100)
# cart = [LineItem('banana', 4, .5),  LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
# l = Order(ann, cart, FidelityPromo())
# print(l)

# from functools import singledispatch
# from collections import abc
# import numbers
# import html
#
#
# @singledispatch
# def htmlize(obj):
#     content = html.escape(repr(obj))
#     return '<pre>{}</pre>'.format(content)
#
#
# @htmlize.register(str)
# def _(text):
#     content = html.escape(text).replace('\n', '<br>\n')
#     return '<p>{0}</p>'.format(content)
#
#
# @htmlize.register(numbers.Integral)
# def _(n):
#     return '<pre>{0} (0x{0:x})</pre>'.format(n)
#
#
# @htmlize.register(tuple)
# @htmlize.register(abc.MutableSequence)
# def _(seq):
#     inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
#     return '<ul>\n<li>' + inner + '</li>\n</ul>'
# print( htmlize(42))

# registry = []
#
#
# def register(func):
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func
#
#
# @register
# def f1():
#     print('running f1()')
#
#
# print('running main()')
# print('registry ->', registry)
# f1()
# a = (10,20)
# # b = [a,30]
# # a.append(b)
# # print(a)
#
# b = a[:]
# c = a.copy()
# print(a is c)
# t1 = frozenset("ccg")
# # t2 = t1[:]
# t3 = t1.copy()
# print(t1 is t3)

# l = (i for i in range(10))
#
# def A():
#     print(l.__next__())
# for i in range(5):
#     A()
# import itertools
# gen = itertools.count(1,100)
# for i in range(5):
#     print(next(gen))


# import logging
# from functools import partial
#
# def wrapper_property(obj, func=None):
#     if func is None:
#         return partial(wrapper_property, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
# def logger_info(level, name=None, message=None):
#     def decorate(func):
#         logmsg = message if message else func.__name__
#
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#
#         @wrapper_property(wrapper)
#         def set_level(newlevel):
#             nonlocal level
#             level = newlevel
#
#         @wrapper_property(wrapper)
#         def set_message(newmsg):
#             nonlocal logmsg
#             logmsg = newmsg
#
#         return wrapper
#
#     return decorate
#
# @logger_info(logging.WARNING)
# def main(x, y):
#     return x + y

# l = [{"{0:d}".format(range(1000))}]
# l = ["{:0>5d}".format(i) for i in range(1000)]
# print(l)
# def method():
#     res = None
#     total = 0
#     while True:
#         res = yield res
#         if total == 999:
#             total = 0
#         total = total + 1
#         res = res + total
#
#
# coro = method()
# next(coro)
# for i in range(1005):
#     index = (coro.send(0))
#     print(l[index])
# from collections import namedtuple
# Result = namedtuple('Result', 'count average')
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total / count
#     return Result(count, average)
# coro_avg = averager()
# next(coro_avg)
# print(coro_avg.send(10))
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield average
#         total += term
#         count += 1
#         average = total / count
# coro_avg = averager()
# next(coro_avg)
# print(coro_avg.send(10))

# def method(i):
#     if i == 1:
#         print(i)
#     if i == 2:
#         print(i)
#     else:
#         print("end")
# method(2)
# from collections import namedtuple
# Result = namedtuple('Result', 'count average')
#
# # 子生成器
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total / count
#
#     return Result(count, average)
#
# # 委派生成器
# def grouper(results, key):
#     while True:
#         results[key] = yield from averager()
#
# # 客户端代码，即调用方
# def main(data):
#     results = {}
#     for key, values in data.items():
#         group = grouper(results, key)
#         next(group)
#         for value in values:
#             group.send(value)
#         group.send(None)  # 重要！
#     # print(results) # 如果要调试，去掉注释
#     report(results)
#
#
# # 输出报告
# def report(results):
#     for key, result in sorted(results.items()):
#         group, unit = key.split(';')
#     print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))
#
# data = {
#     'girls;kg':
#         [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
#     'girls;m':
#         [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
#     'boys;kg':
#         [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
#     'boys;m':
#         [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
# }
# if __name__ == '__main__':
#     main(data)

# class Pizza:
#     def __init__(self, builder):
#         self.garlic = builder.garlic
#         self.extra_cheese = builder.extra_cheese
#
#     def __str__(self):
#         garlic = 'yes' if self.garlic else 'no'
#         cheese = 'yes' if self.extra_cheese else 'no'
#         info = ('Garlic: {}'.format(garlic), 'Extra cheese: {}'.format(cheese))
#         return '\n'.join(info)
#
#     class PizzaBuilder:
#         def __init__(self):
#             self.extra_cheese = False
#             self.garlic = False
#
#         def add_garlic(self):
#             self.garlic = True

#             return self
#
#         def add_extra_cheese(self):
#             self.extra_cheese = T娗rue
#             return self
#
#         def build(self):
#             return Pizza(self)
#
#
# if __name__ == '__main__':print(dict(queue_.get()))
#     pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
#     print(pizza)
# from collections import namedtuple
# import queue
# Event = namedtuple('Event', 'time proc action')
# Event(time=14, proc=0, action='pick up passenger')
#
# queue_ = queue.PriorityQueue()
# put = queue_.put(Event(time=14, proc=0, action='pick up passenger'))
# print(dict(queue_.get()))
# print(dict(queue_.get()))
# queue_.put(Event(time=14, proc=0, action='pick up passenger'))
# import time
# from tqdm import tqdm
# for i in tqdm(range(1000)):
#     time.sleep(0.1)

# import datetime
# import time
# print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
# import pytz
# import time
# import bisect
# start = time.time()
# x = list(range(10**6))
# i = x.index(991234)
# # i = bisect.bisect_left(x, 991234)
# end = time.time() - start
# print(i,end)

# import itertools
# l = list(range(10))
# print(l)
# i1, i2 = itertools.tee(l,2)
# for i in i1:
#     print(i)


# import threading
# import itertools
# import time
# import sys
#
# class Signal:
#     go = True
#
# def spin(msg, signal):
#     write, flush = sys.stdout.write, sys.stdout.flush
#     for char in itertools.cycle('|/-\\'):
#         status = char + ' ' + msg
#         write(status)
#         flush()
#         write('\x08' * len(status))
#         time.sleep(.1)
#         if not signal.go:
#             break
#     write(' ' * len(status) + '\x08' * len(status))
#
# def slow_function():
#     # 假装等待I/O一段时间
#     time.sleep(3)
#     return 42
#
# def supervisor():
#     signal = Signal()
#     spinner = threading.Thread(target=spin,
#                                args=('thinking!', signal))
#     print('spinner object:', spinner)
#     spinner.start()
#     result = slow_function()
#     signal.go = False
#     spinner.join()
#     return result
#
# def main():
#     result = supervisor()
#     print('Answer:', result)
#
# if __name__ == '__main__':
#     main()
# class Student(object):
#     pass
# s1 = Student()
# def set_age(self, age):
#     self.age = age
# from types import MethodType
# s1.set_age = MethodType(set_age,s1)
# s1.set_age(10)
# print(s1.age)

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self, value):
#         self._width = value
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#     @property
#     def resolution(self):
#         return self._height * self._width
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
# import fileinput
#
# with fileinput.input() as f_input:
#     for line in f_input:
#         print(f_input.filename(),f_input.lineno(), line,end='')

# import sys
# sys.stderr.write('It failed!')
# raise SystemExit(1)
# import os
# sz = os.get_terminal_size()
# print(sz.columns)
# print(sz.lines)
# import shutil
# shutil.copytree('D:\\新建文件夹','F:\\新建文件夹')

# import os
# for relpath, dirs, files in os.walk('D://'):
#     # print(relpath)
#     # print(dirs)
#     print([file for file in files if file.endswith('.py')])
# import sys
# if len(sys.argv) != 3:
#     print(f'Usage: {sys.argv[0]} dir seconds')
#     raise SystemExit(1)
# import argparse
# argparse.ArgumentParser()
# from configparser import ConfigParser
# cfg = ConfigParser()
# cfg.read('config.ini')
# port = cfg.getint('server','port')
# # print(port)
# cfg.set('server','port', "8081")
# port = cfg.getint('server', 'port')
# print(port)
# import sys
# cfg.write(sys.stdout)

# import logging
# def main():
#     # Configure the logging system
#     logging.basicConfig(
#     filename='app.log',
#     level=logging.debug
#     )
# # Variables (to make the calls that follow work)
# hostname = 'www.python.org'
# item = 'spam'
# filename = 'config.ini'
# mode = 'r'
# # Example logging calls (insert into your program)
# logging.critical('Host %s unknown', hostname)
# logging.error("Couldn't find %r", item)
# logging.warning('Feature is deprecated')
# logging.info('Opening file %r, mode=%r', filename, mode)
# logging.debug('Got here')
# if __name__ == '__main__':
#     main()
# num = """
# 4
# 3
# 1,2,3,4,5,6
# 1,2,3
# 1,2,3,4
# """
# num_res = num.split()
# print(num_res)
# num_len = int(num_res[0])
# num_int = num_res[1]
# res_list = []
# i = 0
# max_len = len(max(num_res, key=len).replace(',', ''))
# while i < max_len:
#     for num_data in num_res[2:2 + int(num_int)]:
#         # print(num_data[:int(num_len)+1])
#         # num_data_zi = [num_data[i:i+6] for i in range(0, len(num_data), 6)]
#         # print(list(zip(res_list,num_data_zi)))
#         num_data = num_data.replace(',', '')
#         print(num_data)
#
#         if len(num_data) >= num_len:
#             res_list.append(num_data[i:i + num_len])
#         elif 0 < len(num_data) < num_len:
#             res_list.append(num_data[i:])
#         else:
#             continue
#     i = i + num_len
# print(res_list)
#
# for res in res_list:
#     if res != '':
#         print(''.join(res), end='')

# mydict = {
#     "source-id": "1",
#     "camera-name": "2",
# }
#
# pdpc_kafka_reflect = {
#     "source-id": "source_id",
#     "camera-name": "camera_name",
#     "file-id": "file_id",
# }
#
# pdpc_push = {
#     "source_id": "8",
#     "camera_name": "7",
# }
#
# VEHICLE_SOURCEID_REFLET = {"1": "8", "2": "5"}
# VEHICLE_CAMERANAME_REFLET = {"1": "3", "2": "7"}
#
#
# def mydict_to_pdpc_push(pdpc_kafka_reflect,VEHICLE_SOURCEID_REFLET,VEHICLE_CAMERANAME_REFLET,**kwargs):
#     pdpc_kafka_reflect = pdpc_kafka_reflect
#     VEHICLE_SOURCEID_REFLET = VEHICLE_SOURCEID_REFLET
#     VEHICLE_CAMERANAME_REFLET = VEHICLE_CAMERANAME_REFLET
#
#     for k, v in list(kwargs.items()):
#         if k in list(pdpc_kafka_reflect.keys()):
#             if k == "source-id":
#                 kwargs[pdpc_kafka_reflect[k]] = VEHICLE_SOURCEID_REFLET[interval_kwargs(k, **mydict)]
#             elif k == "camera-name":
#                 kwargs[pdpc_kafka_reflect[k]] = VEHICLE_CAMERANAME_REFLET[interval_kwargs(k, **mydict)]
#             else:
#                 kwargs[pdpc_kafka_reflect[k]] = interval_kwargs(k, **mydict)
#     return kwargs
#
#
# def compare(mydict_r, pdpc_push):
#     for k, v in mydict_r.items():
#         if k in pdpc_push.keys() and v != pdpc_push[k]:
#             print(f'字段{k}传入值再做转换后{v},实际推送值为{pdpc_push[k]}')
#         else:
#             print(f'字段{k}校验成功')
#
#
# def interval_kwargs(str_, **kwargs):
#     if str_ in list(kwargs.keys()):
#         res = kwargs.get(str_)
#         del kwargs[str_]
#     return res
#
# if __name__ == '__main__':
#     mydict_r = mydict_to_pdpc_push(pdpc_kafka_reflect,VEHICLE_SOURCEID_REFLET,VEHICLE_CAMERANAME_REFLET,**mydict)
#     compare(mydict_r,pdpc_push)


# num = """
# 4
# 100 100 120 130
# 40 30 60 50
# """
# num = num.split('\n')
# numbers = int(num[1])
# stu_highs =[int(num_) for num_ in num[2].split()]
# stu_weights = [int(num_) for num_ in num[3].split()]
# i = 0
# dict = {}
# list = []
# min_stu_high = ''
# while i < numbers-1:
#     if stu_highs[i] < stu_highs[i+1]:
#         min_stu_high = stu_highs[i]
#         dict[min_stu_high] = i+1
#         dict[stu_highs[i+1]] = i+2
#     elif stu_highs[i] == stu_highs[i+1]:
#         if stu_weights[i] > stu_weights[i+1]:
#             dict[stu_highs[i]] = i+2
#             dict[stu_highs[i+1]] = i+1
#         elif stu_weights[i] == stu_weights[i+1]:
#             dict[stu_highs[i]] = i+1
#             dict[stu_highs[i+1]] = i+2
#         elif stu_weights[i] < stu_weights[i+1]:
#             dict[stu_highs[i+1]] = i+1
#             dict[stu_highs[i]] = i+2
#     elif stu_highs(i) > stu_highs(i+1):
#         dict[stu_highs(i)] = i+2
#         dict[stu_highs(i+1)] = i+1
#     i = i+1
# for i in range(numbers):
#     print(dict[i], end='')


# def f(m, l1, l2):
#     l3 =[i+1 for i in range(len(l1))]
#     arr1 = list(zip(l1,l2,l3))
#     print(arr1)
#     arr2 = sorted(arr1,key=lambda x:(x[0],x[1]))
#     print(arr2)
#     l4 = [0,0,0,0]
#     for i in range(len(l1)):
#         l4[arr2[i][2]-1] = i+1
#     print(l4)
#
#
# num = """
# 4
# 120 110 120 90
# 45 60 45 45
# """
# num = num.split('\n')
# m = int(num[1])
# l1 =[int(num_) for num_ in num[2].split()]
# l2 = [int(num_) for num_ in num[3].split()]
#
# f(m,l1,l2)
#
# import sys
# l = "232332323"
# i = 0
# while i < len(l):
#
#     if len(l[i:]) >= 8:
#         print(l[i:8+i])
#     elif len(l[i:]) < 8:
#         print('{:0<8s}'.format(l[i:]))
#     i = i+8
# s = '0xaa'
# print(hex(170))
# print(int(s,16))
# import math
# res = []
# num = 100
# for i in range(2,num):
#     flag = 0
#     for j in range(2,int(math.sqrt(i))+1):
#         if i % j == 0:
#             flag = 1
#     if flag == 0:
#         res.append(i)
# print(res)
#
#
# num = 180
#
# def getprime(n):
#     i = 2
#     while i * i <= n and n >= i:
#         while n % i == 0:
#             n = n // i
#             print(i, end=" ")
#         i = i + 1
#     if n - 1:
#         print(n, end=" ")
# getprime(num)

s = """
['27']
['8', '46828']
['24', '47153']
['3', '93735']
['13', '72600']
['4', '44422']
['8', '73704']
['12', '52139']
['19', '47649']
['21', '10445']
['15', '63369']
['20', '48412']
['17', '57017']
['18', '9379']
['16', '51964']
['19', '70049']
['0', '72000']
['25', '38544']
['18', '21967']
['24', '90219']
['2', '17950']
['3', '51355']
['14', '32107']
['25', '81332']
['23', '95607']
['10', '69407']
['12', '53131']
['19', '87351']"""

# import sys
# d = {}
# # for line in sys.stdin:
# #     a = line.split()
# #     print(a)
# lines = s.split('\n')
# for a in lines:
#     if len(a) == 1:
#         continue
#     if a[0] in d.keys():
#         d[a[0]] = int(d.get(a[0])) + int(a[1])
#     else:
#         d[a[0]] = a[1]
# for k, v in d.items():
#     print(f'{k} {v}')
# n = "123455"
# print(n[::-1])
# l = {'9': 0, '8': 0, '7': 0, '6': 0, '3': 0}
# print(l['3'])
# bin_a = list(bin(int(i)).replace('0b','') for i in ['5'])
# print(bin_a[0])
# import collections
# d = collections.defaultdict(list)
# print(d)
# m = 5
# N = 50
# dp = [[0]*(m+1) for _ in range(N+1)]
# print(dp)
# from collections import defaultdict
# classdic = defaultdict(int)
# print(classdic)
# print(classdic[100])

ym = '255.254.255.0'
# ym1 = list(map(int, ym.split('.')))
# ym2 = ym.split('.')
# ym2 = ''.join(['{:08b}'.format(i) for i in ym1])
# print(ym2)
# if ym2.find('0') == -1 or ym2.find('1') == -1 or ym2.find('0') != ym2.rfind('1') + 1:
#     print(False)
# ip1 = '10.70.44.68'
# ip1 = list(map(int, ip1.split('.')))
# print(ip1)
# if ip1[0] == 10 or (ip1[0] == 172 and 16 <= ip1[1] <= 31) or (ip1[0] == 192 and ip1[0] == 168):
#     print(True)
# import sys
# content = [3,10,81,0]
# for line in content:
#     # a = line.split('\n')
#
#     # print(int(a[0]) + int(a[1]))
#     n = int(line)
#     count = 0
#     if n !=0:
#         while int(n/3) >0 :
#             count += int(n/3)
#             n = int(n/3)+int(n%3)
#             if n+1==3:
#                 count+=1
#
#         print(count)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def bulid_tree(self, preorder, inorder) -> TreeNode:
#         if not preorder or not inorder:
#             return None
#         if len(preorder) != len(inorder):
#             return None
#         root = preorder[0]
#         rootNode = TreeNode(root)
#         pos = inorder.index(root)
#         inorder_left = inorder[:pos]
#         inorder_right = inorder[pos+1:]
#         preorder_left = preorder[1:pos+1]
#         preorder_right = preorder[pos+1:]
#         node_left = self.bulid_tree(preorder_left, inorder_left)
#         node_right = self.bulid_tree(preorder_right, inorder_right)
#         rootNode.left = node_left
#         rootNode.right = node_right
#         return rootNode
# tree = Solution().bulid_tree
# res = tree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
# print(res)
# numbers = [3,4,5,1,2]
# a = numbers[2:]
# b = numbers[:2]
# new = []
# [new.append(_) for _ in a]
# new.extend(b)
# print(new)
# from collections import deque
# class Solution:
#     def maxTaskAssign(self, tasks, workers, pills: int, strength: int) -> int:
#         tasks.sort()
#         workers.sort()
#         s = 0
#         e = min(len(tasks), len(workers)) + 1
#         while s + 1 < e:
#             m = (s + e) // 2
#             # print("try", m)
#             # Match workers[-m:] to tasks[:m]
#             i2 = 0
#             p = pills
#             fail = False
#             valid_tasks = deque()
#             for j in range(len(workers) - m, len(workers)):  # 一半工人数量~
#                 w = workers[j]
#                 while i2 < m and tasks[i2] <= w + strength:  # 遍历前一半任务，如果任务小于工人能力+药丸
#                     valid_tasks.append(tasks[i2])
#                     i2 += 1
#                 if not valid_tasks:
#                     fail = True
#                     break
#                 if valid_tasks[0] <= w:
#                     # No need for pill
#                     valid_tasks.popleft()
#                 else:
#                     if not p:
#                         fail = True
#                         break
#                     p -= 1
#                     valid_tasks.pop()
#             if fail:
#                 e = m
#             else:
#                 s = m
#         return s
# import re
# with open('cc.txt','r') as f:
#     body = f.read()
# res = re.search('"Data": "(.*?)"',body)
#
# l = list(range(5))
# l2 = list(range(5))
#
#
#
# # if __name__ == '__main__':
#     # s = Solution()
#     # res = s.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1)
#     # print(res)
# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         seen = 0
#         for ch in s:
#             x = ord(ch) - ord("a")
#             if seen & (1 << x):
#                 return ch
#             seen |= (1 << x)
# result = Solution().repeatedCharacter(s="abccbaacz")
# print(result)

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)
s = Solution()
s.copyRandomList(head=[Node(7,None),Node(13,0)])