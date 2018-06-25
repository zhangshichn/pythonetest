#!/usr/bin/python3
# -*- coding:UTF-8 -*-




#計算輸入數字的乘積
def product(x,*y):
	s=1*x
	for i in y:
		s=s*i
	print(x,*y,'的積是:',s)

product(5)
product(5,6)
product(5,6,7)
product(5,6,7,9)


'''
#命名關鍵字參數

def person(name,age,**kv):
	if 'city' in kv:
		pass
	else:
		print('No city value')
	if 'job' in kv:
		pass
	else:
		print('No job value')

	print('name:',name,'age:',age,'others:',kv)

extra1 = {'city':'BJ'}
extra2 = {'job':'Engineer'}
extra3 = {'city':'BJ','job':'Engineer'}
person('Alice',30)
person('Bob',25,**extra1)
person('Chris',18,**extra2)
person('Doris',44,**extra3)
person('Frank',30,zipcode='100101',passport='3344')







#關鍵字參數
def person(name,age,**kv):
	print('name:',name,'age:',age,'others',kv)

person('Alice',25)
person('Bob',30,city='BJ',Gender='M')


extra = {'city':'SH','Gender':'F'}
person('Chris',18,**extra)






#輸入可變參數

def cal(*number):
	sum = 0
	for i in number:
		sum = sum+i*i
	print(sum)


cal(1,2,3)
cal(1,2,3,7)


list=[1,3,5,7]
cal(*list)

'''
