import sys
# def output(nums):
#     if len(nums)==0 or len(nums)==1:
#         return 0
#     sub = abs(nums[0]-nums[1])
#     results = [0]
#     for i in range(len(nums)-1):
#         if i==0:
#             temp = abs(nums[i+1]-nums[i])
#         else:
#             temp = abs(nums[i+1]-nums[i])
#         if temp<sub:
#             sub = temp
#             results = []
#             results.append(i)
#         if temp == sub:
#             results.append(i)
#     print(str(nums[results[0]])+' '+str(nums[results[0]+1]))

# if __name__=="__main__":
#     nums = []
#     length = 0
#     for i in range(2):
#         if i==0:
#             length = input()
#         if i==1:
#             nums = list(map(int,input().split()))
#     output(nums)

# def search(l,number,begin,end):
#     if begin==end:
#         return begin
#     while begin<end:
#         mid=(begin+end) // 2
#         if mid==begin or mid==end:
#             if number>l[begin]:
#                 return end
#             else:
#                 return begin
#         if number<l[mid]:
#             return search(l,number,begin,mid)
#         else:
#             return search(l,number,mid,end)
# def output(nums,length):
#     result = 0
#     if length == 0:
#         return 0
#     if length == 1:
#         return 1
#     l = []
#     l.append(nums[0])
#     maxlen = [1 for i in range(len(nums))]
#     for i in range(1,length):
#         if nums[i]<=l[-1]:
#             if nums[i]<l[0]:
#                 l[0] = nums[i]
#             else:
#                 index=search(l,nums[i],0,len(l)-1)
#                 l[index]=nums[i]
#         else:
#             l.append(nums[i])
#     result = len(l)
#     return result

# if __name__=="__main__":
#     n = int(input())
#     nums = []
#     for i in range(n):
#         nums.append(int(input()))
#     result = output(nums,n)
#     print(result)

def output(nums,length):
    if length == 0:
        return 0
    if length == 1:
        return 1
    nums = sorted(nums)
    result = 0
    while len(nums)!=0:
        for i in range(1,len(nums)):
            if nums[0]>=nums[i]*0.9:
                result +=1
            else:
            	break
        nums.pop(0)
    return result
if __name__=="__main__":
    length = 0
    nums = []
    for i in range(2):
        if i==0:
            length = int(input())
        if i==1:
            nums = list(map(int,input().split()))
    result = output(nums,length)
    print(result)