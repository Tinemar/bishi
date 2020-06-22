def output(n,inputs):
    result = []
    num_index = []
    cannot_index = []
    index = []
    nums = []
    for i in range(0,len(inputs)):
        #不能交换的index
        if inputs[i] == '/':
            cannot_index.append(i-1,i+1)
            index.append(i)
        #运算符
        elif inputs[i] in ['+','-','*']:
            index.append(i)
        #能交换的数字
        else:
            num_index.append(i)
            nums.append(int(inputs[i]))
    start = 1
    end = 3
    while end<len(inputs) :
        if inputs[end] == '/':
            end += 2
            start = end
            end += 2
        elif inputs[end] == inputs[end-2]:
            end += 2
        if inputs[end] != inputs[end-2]:
            print(start,end)
            nums[(start-1)//2:(end-1)//2] = sorted(nums[(start-1)//2:(end-1)//2])
            start = end
            end += 2
    
    return result

if __name__ == "__main__":
    n = int(input())
    inputs = list(map(str,input().split()))
    result = output(n,inputs)    
    print(result)
