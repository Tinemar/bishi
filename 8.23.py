

# def output(n, k, inputstr):
#     result = ''
#     if n==0:
#         return result
#     if len(inputstr) > 0:
#         result += inputstr
#         k -= 1
#     while(k > 0):
#         result = checkAndMerge(result, inputstr)
#         k -= 1
#     return result


# def checkAndMerge(result,inputstr):
#     index1 = len(result)
#     index2 = 0
#     split = 0
#     while(index1>=0 and index2<=len(inputstr)):
#         if result[index1:] == inputstr[:index2] and len(result[index1:])<len(inputstr):
#             split = index2
#         index1-=1
#         index2+=1
#     return result+inputstr[split:]


# if __name__ == "__main__":
#     n = k = 0
#     inputs = list(map(int, input().split()))
#     n = inputs[0]
#     k = inputs[1]
#     inputstr = str(input())
#     result = output(n, k, inputstr)
#     print(result)
#     # print(('abba','abba'))
# def output(n, inputs):
#     sum = 0
#     for i in range(0, n):
#         sum += inputs[i]
#     dp = []
#     for i in range(0, n+1):
#         temp = []
#         for j in range(0,(sum//2)+1):
#             temp.append(0)
#         dp.append(temp)
#     for i in range(1, n+1):
#         for j in range(1, (sum//2)+1):
#             if j >= inputs[i-1]:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-inputs[i-1]]+inputs[i-1])
#             else:
#                 dp[i][j] = dp[i-1][j]
#     return sum-2*dp[n][sum//2]


# if __name__ == "__main__":
#     n = int(input())
#     inputs = list(map(int, input().split()))
#     result = output(n, inputs)
#     print(result)
# def output(n,s,inputs):
#     inputs = sorted(inputs)
#     result = 0
#     while(s>=inputs[0]):
#         result += 1
#         s -= inputs[0]
#         del inputs[0]
#     return result
# if __name__ == "__main__":
#     inputs = list(map(int, input().split()))
#     n = inputs[0]
#     s = inputs[1]
#     inputs = list(map(int, input().split()))
#     result = output(n,s,inputs)
#     print(result)


import numpy as np
 
weight=[2,2,6,5,4]
value=[3,6,5,4,6]
weight_most=10
def bag_0_1(weight,value,weight_most):#return max value
    num = len(weight)
    weight.insert(0,0)#前0件要用
    value.insert(0,0)#前0件要用
    bag=np.zeros((num+1,weight_most+1),dtype=np.int32)#下标从零开始
    for i in range(1,num+1):
        for j in range(1,weight_most+1):
            if weight[i]<=j:
                bag[i][j]=max(bag[i-1][j-weight[i]]+value[i],bag[i-1][j])
            else:
                bag[i][j]=bag[i-1][j]
    # print(bag)
    return bag[-1,-1]
 
result=bag_0_1(weight,value,weight_most)
print(result)
