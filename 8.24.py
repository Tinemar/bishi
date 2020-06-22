# def output(_inputs):
#     nums = 0
#     inputs = []
#     _inputs = sorted(_inputs)
#     _inputs.reverse()
#     print(_in)
#     for i in range(0, len(_inputs)):
#         if _inputs[i] != 0:
#             inputs.append(_inputs[i])
#     while len(inputs) > 2:
#         nums,inputs = s(nums,inputs)
#     return nums
# def s(nums,inputs):
#     while inputs[0] !=0:
#         nums +=1
#         for i in range(0, 3):
#             inputs[i] -= 1
#     newinputs = []
#     for i in range(0,len(inputs)):
#         if inputs[i] != 0:
#             newinputs.append(inputs[i])
#     return nums,newinputs

# if __name__ == '__main__':
#     c = int(input())
#     inputs = []
#     for i in range(0, c):
#         temp = list(map(int, input().split()))
#         inputs.append(temp[1:])
#     for i in range(0, c):
#         print(output(inputs[i]))


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

# JD
# def output(inputstr):
#     dp = [0]*(len(inputstr))
#     iscap = 0
#     if inputstr[0].isupper():
#         dp[0] = 2
#     else:
#         dp[0] = 1
#     for i in range(1, len(inputstr)):
#         if inputstr[i].islower() and not iscap:
#             dp[i] = dp[i-1]+1
#         if inputstr[i].islower() and iscap:
#             if i+1<len(inputstr):
#                 if inputstr[i+1].islower():
#                     iscap = 0
#                     dp[i] = dp[i-1]+2
#                 else:
#                     dp[i] = dp[i-1]+2
#             else:
#                 dp[i] = dp[i-1]+2
#         if inputstr[i].isupper() and iscap:
#             dp[i] = dp[i-1]+1
#         if inputstr[i].isupper() and not iscap:
#             if i+1<len(inputstr):
#                 if inputstr[i+1].isupper():
#                     iscap = 1
#                     dp[i] = dp[i-1]+2
#                 else:
#                     dp[i] = dp[i-1]+2
#             else:
#                 dp[i] = dp[i-1]+2
#     return dp[len(inputstr)-1]


# if __name__ == "__main__":
#     n = int(input())
#     inputstr = str(input())
#     result = output(inputstr)
#     print(result)
def output(inputs):
    target = nums(inputs)
    chan = 0
    reco = []
    result = 0
    for i in range(0, 5):
        for j in range(0, 5):
            print(i, j)
            if inputs[i][j] == -1:
                continue
            if inputs[i][j] == target:
                reco.append([i, j])
                while i > 0 and i < 5 and j > 0 and j < 5:
                    if inputs[i+1][j] == target:
                        chan += 1
                        i = i+1
                        reco.append([i, j])
                    if inputs[i][j+1] == target:
                        chan += 1
                        j = j+1
                        reco.append([i, j])
                    if inputs[i-1][j] == target:
                        chan += 1
                        i = i - 1
                        reco.append([i, j])
                    if inputs[i][j-1] == target:
                        chan += 1
                        j = j-1
                        reco.append([i, j])
                if chan >= 3:
                    inputs = op(inputs, reco)
    for i in range(0, 5):
        for j in range(0, 5):
            if inputs[i][j] != -1:
                result += 1
    return result


def op(inputs, reco):
    for i in reco:
        inputs[i[0], i[1]] = -1
    for i in range(0, 5):
        for j in range(0, 5):
            if inputs[i][j] == -1:
                inputs[i][0] = -1
                for j in range(j, 0, -1):
                    inputs[i][j] = inputs[i][j-1]
    return inputs


def nums(inputs):
    times = {}
    for i in range(0, len(inputs)):
        for j in range(0, len(inputs[0])):
            if inputs[i][j] in times:
                times[inputs[i][j]] += 1
            else:
                times[inputs[i][j]] = 1
    return max(times, key=times.get)


if __name__ == "__main__":
    inputs = []
    for i in range(0, 5):
        temp = list(map(int, input().split()))
        inputs.append(temp)
    result = output(inputs)
    print(result)
