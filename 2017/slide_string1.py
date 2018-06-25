#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Authur:	ZHANG Shi
# @Date:	2017/11/25
# @Version	1.0


#實現刪除輸入字符串前後空格的功能,如果是空字符串,返回一個空格



def trim(s):

#f爲正向非空位置,e爲逆向非空位置
	i=0
	f=0
	e=-1

#計算字符串長度
	for r in s:
		i+=1

#正向計算不爲空的位置
	for r in s:
		if s[f] == ' ':
			f+=1
			
		else:
			break

#逆向計算不爲空的位置
	for r in s:
		if s[e] == ' ':
			e-=1
		else:
			break

#判斷字符串是否全部爲空,返回一個空格
	if( (f == i) and (e == -i+1)):
		return(' ')

#判斷字符串尾部是否有空格,返回trim後的字符串
	elif (e==-1):
		return(s[f:])
#剩餘的情況,飯後兩端空格都trim後的字符串
	else:
		return(s[f:e+1])
		

	
		
#測試
s=input('請輸入字符串:')
s=trim(s)
print('<%s>'%s)



#驗證
if trim('hello  ') != 'hello':
    print('测试失败!')

elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
