# def output(nums):
#     nums = sorted(nums)
#     result = 0
#     for i in nums:
#         if i<=0:
#             del nums[0]
#     for i in range(len(nums)):
#         if nums[i]!=i+1:
#             result = i+1
#             break
#     return result
# if __name__ == "__main__":
#     n = int(input())
#     nums = list(map(int,input().split()))
#     result = output(nums) 
#     print(result)
