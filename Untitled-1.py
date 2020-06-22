# # -*- coding: UTF-8 -*-
# T = int(input())
# result = [0]*T
# for index in range(T):
#     nums = int(input())
#     cards = input().split(' ')
#     trans = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
#          '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
#     count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
#              7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
#     for card in cards:
#         count[trans[card]] += 1
#     for c in list(count.keys())[:-4]:
#         times = 1
#         for a in range(5):
#             times *= count[c+a]
#         if times:
#             result[index] += times
#             for a in range(5, 13):
#                 if count[c + a]:
#                     times = 1
#                     for i in range(a+1):
#                         times *= count[c+i]
#                     result[index] += times
#                 else:
#                     break;
# for i in range(T):
#     print(result[i])
#     if i != len(result)-1:
#         print()
def f(nums):
    f_len = 0
    index = 0
    start = 0
    if nums == []:
        return 0
    while fibo(start)<nums[0]:
        start += 1
    while fibo(start)<=nums[-1]:
        # print(start,fibo(start))
        if fibo(start) in nums:
            f_len += 1
        if start == 1:
            start = 2
        start += 1
    return f_len
def fibo(n):
    a = 0
    b = 1
    if n==0:
        return 0
    for _ in range(n-1):
        a,b = b,a+b
    return b
def lenLongestFibSubseq(A):
    n, res = len(A), 0
    a = [[0] * n for i in range(n)]
    for i in range(n):
        lo, hi, v = 0, i - 1, A[i]
        while lo < hi:
            if A[lo] + A[hi] < v:
                lo += 1
            elif A[lo] + A[hi] > v:
                hi -= 1
            else:
                if a[lo][hi]:
                    a[hi][i] = a[lo][hi] + 1
                else:
                    a[hi][i] = 3
                res = max(a[hi][i], res)
                lo += 1
                hi -= 1
    return res
def malv(n,strs):
    dp = []
    for i in range(n+1):
        tmp = [0]*(n+1)
        dp.append(tmp)
    print(dp)
    for i in range(n):
        for j in range(i,n):
            if i==j:
                dp[i][j] = strs[i]
            else:
                if strs[j]>dp[i-1][j-1]:
                    dp[i][j] = strs[j]
                else:
                    dp[i][j] = dp[i][j-1]
    
    return dp

if __name__ == '__main__':
    # inputs = str(input())
    # nums = []
    # strs = inputs.split(',')[0]
    # pivot = inputs.split(',')[1]
    # i = 0
    # while i<len(strs):
    #     if i =='-' or i=='>'
    
    print(malv(3,[1,2,2]))
if __name__ == '__main__':
    n = int(input())
    listA = []
    for i in range(n):
        temp = list(map(int,input().split(" ")))
        listA.append(temp)
    listA.sort( key=lambda x: x[1])
    left = 0
    right = len(listA)-1
    counta = 0
    countb = 0
    while(left<right):
        countb += listA[left][1]
        right -= listA[left][0]
        left +=1

    print(countb)
