#!/usr/bin/python3
#coding=utf-8

import random
'''
a=random.random()

if a<0.4:
	print('a<0.4, a=',a)
# a小于0.4，打印a

elif (int(a*10)>=4 & int(a*10)<=6):
	print('0,4<=a<=0.6, a*10=',a*10)
#a大于等于0.4并且小于等于0.6，打印a*10
else:
	print('Else, a*100=',a*100)
#其他情况，打印a*100


print('a'= a) #打印a


#猜数字游戏，0-9中随机一个数字
number=11
guess=-1
#初始化随机数和输入数字

number=random.random()*10
number=int(number)
#print(number)

print("let's play this game!")
while guess != number:
	guess=int(input("Please input number between 0-9: "))
	if guess<number:
		print("lower")
	elif guess>number:
		print("highter")

	else:
		print("bingo")


print("game over")

#整除
number = 0 #初始化
number = int(input("请输入一个整数："))
if number%2 == 0:
	if number%3 == 0:
		print(number,'可以被2和3整除')
	else:
		print(number,'可以被2整除')
elif number%3 == 0:
	print(number,'可以被3整除')
else:
	print(number,'不可以被2或者3整除')


#对比两个随机数
x=random.choice(range(100))
y=random.choice(range(200))

if x>y:
	print('x=',x,'y=',y)
elif x==y:
	print('x+y=',x+y,'x=',x,'y=',y)
else:
	print('y=', y,'x=',x)

'''

"""对上面例子的一个扩展"""

print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print(" ")
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2)*5
            print("相当于人类：",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
#input("点击 enter 键退出")
