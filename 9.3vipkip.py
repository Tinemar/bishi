# def output(n):
#     count = 0
#     while n:
#         n = n&(n-1)
#         count += 1
#     return count
# if __name__ == "__main__":
#     n = int(input())
#     result = output(n)
#     print(result)


def output(k,inputs):
    result = []
    if len(inputs)<=k:
        total = 0
        for i in inputs:
            total += i
        result.append(total/len(inputs))
    start = 0
    end = k
    for start in range(0,len(inputs)-k+1):
        total = 0
        for i in inputs[start:start+k]:
            total += i
        result.append(total/len(inputs[start:start+k]))

    return result


if __name__ == "__main__":
    inputs = list(map(int, input().split(' ')))
    k = int(input())
    result = output(k, inputs)
    for i in result:
        print("%.2f " % i, end='')
