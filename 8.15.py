def output(_inputs):
    nums = 0
    inputs = []
    _inputs = sorted(_inputs)
    for i in range(0, len(_inputs)):
        if _inputs[i] != 0:
            inputs.append(_inputs[i])
    while len(inputs) > 2:
        nums,inputs = s(nums,inputs)
    return nums
def s(nums,inputs):
    while inputs[0] !=0:
        nums +=1
        for i in range(0, 3):
            inputs[i] -= 1
    newinputs = []
    for i in range(0,len(inputs)):
        if inputs[i] != 0:
            newinputs.append(inputs[i])
    return nums,newinputs

if __name__ == '__main__':
    c = int(input())
    inputs = []
    for i in range(0, c):
        temp = list(map(int, input().split()))
        inputs.append(temp[1:])
    for i in range(0, c):
        print(output(inputs[i]))

# def output(inputs):
#     result = {}
#     for i in inputs:
#         if i in result:
#             result[i] += 1
#         else:
#             result[i] = 1
#     s = ""
#     for i in inputs:
#         if(result[i] > n):
#             continue
#         else:
#             s += str(i)
#     return s


# if __name__ == "__main__":
#     m,n = list(map(int, input().split(' ')))
#     inputs = list(map(int, input().split(' ')))
#     result = output(inputs)
#     print(result)