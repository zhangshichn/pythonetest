#/usr/bin/python3
#coding=utf-8

import sys
print("----------Python Import Module---------")
print('命令行参数为:')
for i in sys.argv:
	print(i)
print('\n python 路径为', sys.path)
#导入模块

print()


print('------Function has been Imported from Module --------')
from sys import argv,path
print('Path:',path)
#从模块中导入函数
