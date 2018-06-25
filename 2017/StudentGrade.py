#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#定義stu函數,輸入學生的學號和成績
#並返回[學號,成績]列表

def stu(x):
    num = 0
    while True:
        try:
            num =int(input("請輸入第%d位學生的學號:"%(x+1)))
            break
        except ValueError:              #如果學號輸入的是非數字格式,提示重新輸入
            print("學號輸入應爲數字,請重新輸入")


    while True:
        try:
            grade1 =int(input("請輸入學號爲%d的第一科成績:"%num))
            break
        except ValueError:              #如果成績1輸入的是非數字格式,提示重新輸入
            print("成績輸入應爲數字,請重新輸入")

    while True:
        try:
            grade2 = int(input("請輸入學號爲%d的第二科成績:" % num))
            break
        except ValueError:  # 如果成績2輸入的是非數字格式,提示重新輸入
            print("成績輸入應爲數字,請重新輸入")

    while True:
        try:
            grade3 = int(input("請輸入學號爲%d的第三科成績:" % num))
            break
        except ValueError:  # 如果成績3輸入的是非數字格式,提示重新輸入
            print("成績輸入應爲數字,請重新輸入")

    s=[num,grade1,grade2,grade3]
    return(s)



i=0
t=[]    #存儲學生姓名與成績列表


print("將要輸入5位學生的學號和三門科目成績")
while i<5:
    t.append(stu(i))
    i+=1

a=0
amount = 0


while  a<len(t):
    temp = t[a][1]+t[a][2]+t[a][3]
    if temp>amount:
        number=a
        stdnumber=t[a][0]
        amount=temp
    a+=1


print("學號",stdnumber,"總成績",amount,"各項成績",t[number][1],t[number][2],t[number][3],"平均成績",amount/3)

