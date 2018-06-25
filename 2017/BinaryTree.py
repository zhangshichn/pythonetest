#!/usr/bin/python3
# -*- coding: UTF-8 -*-





#定義創建二叉樹的多個函數
def BinaryTree(r):
    return[r,[],[]]

def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,[t],[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[t],[]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getLeftChild(root):
    return(root[1])

def getRightChild(root):
    return(root[2])



#定義對二叉樹遍歷生成列表的函數preorder
def preorder(tree,list):
    if tree!=[]:
        list.append(tree[0])
        preorder(tree[1],list)
        preorder(tree[2],list)
        return(list)



#定義歸並函數,完成對列表的降序排列
def merge(left,right):
    merged=[]
    i,j=0,0
    left_len,right_len=len(left),len(right)
    while i<left_len and j<right_len:
        if left[i] > right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return(merged)

def mergeSort(list):
    if len(list)<=1:
        return list
    mid = len(list)//2
    left=mergeSort(list[:mid])
    right=mergeSort(list[mid:])
    return merge(left,right)







#創建二叉樹
root=int(input("請輸入二叉樹的根:"))
Tree=BinaryTree(root)

L=int(input("請輸入二叉樹的左子樹:"))
insertLeft(Tree,L)

R=int(input("請輸入二叉樹的右子樹:"))
insertRight(Tree,R)

LL=int(input("請輸入左子樹的左葉:"))
insertLeft(getLeftChild(Tree),LL)

LR=int(input("請輸入左子樹的右葉:"))
insertRight(getLeftChild(Tree),LR)

RL=int(input("請輸入右子樹的左葉:"))
insertLeft(getRightChild(Tree),RL)

RR=int(input("請輸入右子樹的右葉:"))
insertRight(getRightChild(Tree),RR)

print('生成的二叉樹爲:',Tree)


#遍歷二叉樹,生成列表
templist=[]
Treelist=preorder(Tree,templist)
print("遍歷二叉樹生成的列表是:", Treelist)


#列表降序排列,取出最大值
TreeSortList=mergeSort(Treelist)
print("二叉樹中最大值是",TreeSortList[0])


'''
程序運行結果

請輸入二叉樹的根:30
5請輸入二叉樹的左子樹:2
請輸入二叉樹的右子樹:15
請輸入左子樹的左葉:23
請輸入左子樹的右葉:74
請輸入右子樹的左葉:86
請輸入右子樹的右葉:10
生成的二叉樹爲: [30, [52, [23, [], []], [74, [], []]], [15, [86, [], []], [10, [], []]]]
遍歷二叉樹生成的列表是: [30, 52, 23, 74, 15, 86, 10]
二叉樹中最大值是 86

'''