
def output(n,num):
    if len(num)<11:
        print('NO')
        return
    else:
        if num[0] == '8':
            print('YES')
            return
        else:
            i = 0
            while i < len(num):
                if num[i] != '8':
                    i+=1
                else:
                    num = num[i:]
                    print(num)
                    break
            if i == len(num):
                print('NO')
                return
            if len(num)>=11:
                print('YES')
                return
            else:
                print('NO')
                return
                
if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        tmp = []
        tmp.append(str(input()))
        tmp.append(str(input()))
        nums.append(tmp)
    for num in nums:
        output(num[0],num[1])

# def output(n,nums):
#     dp = [0]*100
#     total = sum(nums)
#     for i in range(n):
#         for j in range(total//2,nums[i]-1,-1):
#             if dp[j]<dp[j-nums[i]]+nums[i]:
#                 dp[j] = dp[j-nums[i]] + nums[i]
#     d = total-dp[total//2]*2
#     print(dp[total//2],dp[total//2]+d)
# if __name__ == '__main__':
#     n = int(input())
#     inputs = []
#     for i in range(n):
#         tmp = []
#         tmp.append(int(input()))
#         tmp.append(list(map(int, input().split(" "))))
#         inputs.append(tmp)
#     for i in inputs:
#         output(i[0],i[1])

# def output(n,k,nums):
#     nums = sorted(nums)
#     while k>0:
#         if not nums:
#             print(0)
#         else:
#             if nums[0] >=0:
#                 print(nums[0])
#             for i in range(len(nums)-1,-1,-1):
#                 if nums[i]!=0:
#                     nums[i] -= nums[0]
#                     if nums[i] <= 0:
#                         nums = nums[i+1:]
#                         break
#         k -= 1
# if __name__=='__main__':
#     tmp = list(map(int, input().split(" ")))
#     n = tmp[0]
#     k = tmp[1]
#     nums = list(map(int, input().split(" ")))
#     output(n,k,nums)

# def output(n,a,b):
#     result = 0
#     for i in a:
#         for j in b:
#             tmp = i+j
#             result = result^tmp
#     print(result)
# if __name__=='__main__':
#     n = int(input())
#     a = list(map(int, input().split(" ")))
#     b = list(map(int, input().split(" ")))
#     output(n,a,b)
#2

# def output(nums):
#     nums = sorted(nums)
#     l = 0
#     r = len(nums)-1
#     result = nums[r]*2
#     while l<=r:
#         if result>nums[l]+nums[r]:
#             result = nums[l]+nums[r]
#         l += 1
#         r -= 1
#     print(result)
# if __name__=='__main__':
#     n = int(input())
#     nums = []
#     for i in range(n):
#         tmp = list(map(int, input().split(" ")))
#         for i in range(tmp[0]):
#             nums.append(tmp[1])
#     output(nums)

import java.io.*;
class test  
{
	public static void main (String[] args) throws java.lang.Exception
	{
        ArrayList<String> l1 = new ArrayList<String>();
        ArrayList<Integer> l2 = new ArrayList<Integer>();
        l1.add("1");
        l2.add(1);
        System.out.println(l1.get(0).getClass());
        System.out.println(l2.get(0).getClass());
        System.out.println(l2.getClass()==l2.getClass());
	}
}