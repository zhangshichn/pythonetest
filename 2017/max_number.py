#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# @Author:	ZHANG Shi
# @Date:	2017/12/02
# @Version:	1.0


a=[]	
i=0

#輸入10位數字
while i<10:
	while True:		
		try:
			print('請輸入第',i+1,'位數字')
			num=int(input())
			break
		except ValueError:	#如果輸入有誤,提示重新輸入

			print('無效數字,請重新輸入')
	a.append(num)
	i+=1


max1=a[0]
t=1

#數列依次與max1比較
#如果大於max1,則max1變爲次大的數值(max2)
#當前數字a[t],變爲最大數值(max1)
while t<10:
	if a[t] > max1:
		max2 = max1
		max1 = a[t]
	t+=1


print('最大的數是',max1,'次大的數是',max2)
