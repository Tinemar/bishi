#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
#******************************开始写代码******************************


def solution(prices, budget):
    if prices == []:
        return -1
    prices = sorted(prices)
    if prices[0]>budget:
        return -1
    prices.reverse()
    res = 0
    index = 0
    minres = 0
    for i in prices:
        if budget%i==0:
            minres = budget//i
            break
    while budget >=0 and index<len(prices):
        if budget==0:
            return res
        if budget>=prices[index]:
            res += 1
            budget -= prices[index]
        else:
            if index != len(prices)-1:
                index += 1
            else:
                print(minres,res,budget)
                if minres>0 and minres<res:
                    res = minres
                else:
                    res = -1
                index += 1
    return res
    #******************************结束写代码******************************

if __name__=="__main__":
    _prices_cnt = 0
    _prices_cnt = int(input())
    _prices_i = 0
    _prices = []
    while _prices_i < _prices_cnt:
        _prices_item = int(input())
        _prices.append(_prices_item)
        _prices_i += 1

    _budget = int(input())

    res = solution(_prices, _budget)

    print(str(res) + "\n")

# #!/bin/python
# # -*- coding: utf8 -*-
# import sys
# import os
# import re

# # 请完成下面这个函数，实现题目要求的功能
# # 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# #******************************开始写代码******************************

# class Node(object):
#     def __init__(self,data = -1,left = None,right = None):
#         self.data = data
#         self.left = left
#         self.right = right
# class Tree(object):
#     def __init__(self):
#         self.root = Node()
    
# def solution(input):
#     if input=='':
#         return ''
#     res = ''
#     stack = []
#     l = []
#     depth = {}
#     while index < (len(input):
#         tmp_depth = 0
#         while index
#         if input[index]=='(':
            
#             stack.append(index)
#         if input[index]==')':
#             l.append([stack.pop(),index])
#         print(l)
#         index += 1
#     return res
#     #******************************结束写代码******************************


# try:
#     _input = str(input())
# except:
#     _input = None


# res = solution(_input)

# print(res + "\n")
