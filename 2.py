import sys

def output(x,nums,n):
    times = 0
    for i in range(n):
        if nums[i]>=x:
            times +=1
            nums[i] -= 1
    return times,nums
if __name__ == "__main__":
    sub=[]
    nums = []
    inputs=[]
    for i in range(2):
        if i==0:
            inputs = list(map(int, input().split()))
        else:
            nums = list(map(int, input().split()))
    for i in range(inputs[1]):
        sub.append(int(input()))
    for i in sub:
        times,nums = output(i,nums,inputs[0])
        print(times)