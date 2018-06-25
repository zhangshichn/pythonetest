#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#定義排序函數arrangeList
def arrangeList(alist):

#nlist爲學號列表,glist爲成績列表
    nlist=[]
    glist=[]
    for i in range(len(alist)):
        if i%2 == 0:
            nlist.append(alist[i])

    for i in range(len(alist)):
        if i%2 == 1:
            glist.append(alist[i])

#針對nlist做學號升序排列,學號交換時,glist中對應的成績也做交換
    for i in range(len(nlist)-1):
        m=i
        for j in range(i+1,len(nlist)):
            if nlist[j]< nlist[m]:
                m=j
                nlist[i],nlist[m]=nlist[m],nlist[i]
                glist[i],glist[m]=glist[m],glist[i]

#針對glist,學號相同的成績做升序排列,成績交換時,因爲學號一樣就不用交換了
    for i in range(len(glist) - 1):
        m = i
        for j in range(i + 1, len(glist)):
            if glist[j] > glist[m]:
                m = j
                if nlist[i]== nlist[m]:
                    glist[i], glist[m] = glist[m], glist[i]

#定義rlist,將學號和成績合並,然後輸出
    rlist=[]
    for i in range(len(nlist)):
        rlist.append(nlist[i])
        rlist.append(glist[i])
    print("經過排序的學號和成績爲:",rlist)


alist = [20170123,61,20170233, 97,20170123,72,20170233,65,20170110,97]
arrangeList(alist)


'''
程序運行結果:
經過排序的學號和成績爲: [20170110, 97, 20170123, 72, 20170123, 61, 20170233, 97, 20170233, 65]
'''