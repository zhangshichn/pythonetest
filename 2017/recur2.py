#!/usr/bin/python3
# -*- coding:utf-8 -*-



#continue循環
#輸出10以內的奇數
n=0
while n<10:
	n+=1
	if n%2==0:
		continue
	print(n)

#break循環
n=0
sum=0
while n<100:
	if sum>100:
		break
	sum=sum+n
	n+=1
'''	if sum>100:
		break
'''
print('n=',n,' sum=',sum)

#打印姓名
list=['Adam','Bart','Cathy']
for x in list:
	print('Hello,',x)


#輸出1-10的和
sum=0
number=[0,1,2,3,4,5,6,7,8,9,10]
for x in number:
	sum=sum+x
print(sum)

#輸出1-100的和
sum=0
for x in range(101):
	sum=sum+x
print(sum)


#輸出100以內奇數的和
n=1
sum=0
while n<100:
	sum=sum+n
	n=n+2
print(sum)

#輸出100以內奇數的和(2)

n=99
sum=0
while n>0:
	sum=sum+n
	n=n-2
print('100以內奇數的和是: ',sum)




