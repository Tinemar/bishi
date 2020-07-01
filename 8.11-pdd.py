
# def output(nums, n):
#     nums = sorted(nums)
#     sum1 = [0] * n
#     sum2 = [0] * n
#     for i in range(1, n):
#         sum1[i] = sum1[i-1]+nums[i]
#         sum2[i] = sum2[i-1] + nums[i]*nums[i]
#     result = 2e18
#     for i in range(3, n):
#         total1 = sum1[i]-sum1[i-3]
#         e1 = total1/3*total1/3
#         total2 = sum2[i]-sum2[i-3]
#         e2 = total2/3
#         result = min(e2-e1, result)
#     return result+1e-8


# if __name__ == "__main__":
#     n = 0
#     nums = []
#     inputs = []
#     for i in range(2):
#         if i == 0:
#             n = int(input())
#         else:
#             nums = list(map(int, input().split()))
#     result = output(nums, n)
#     result = "%.2f%%" % (result)
#     print(result[:-1])
def output(num1,num2,n,m):
    
    result = [-1] * n
    # for index in range(0,n):
    #     i = 0
    #     j = n-1
    #     while(i<n and j>=0):
    #         temp = num1[i] + num2[j]
    #         if temp == m-1:
    #             result[index] = temp
    #             num1.pop(i)
    #             num2.pop(j)
    #             # i+=1
    #             # j-=1
    #             break
    #         if temp > m-1:
    #             i+=1
    #             j-=1
    #         if temp < m-1:
    for i in num1:
        for j in num2:
            
    return result


if __name__ == "__main__":
    n = m = 0
    inputlist = list(map(int, input().split()))
    n = inputlist[0]#length
    m = inputlist[1]#模
    num1=num2=[]
    for i in range(0,2):
        if i==0:
            num1 = list(map(int, input().split()))
        else:
            num2 = list(map(int, input().split()))
    result = output(num1,num2,n,m)
    print(result)
