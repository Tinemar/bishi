
# def output(inputlist):
#     strmap = dict()
#     for i in range(0,len(inputlist)):
#         print(i)
#         strmap[i] = inputlist[i]
#     return result


# if __name__ == "__main__":
#     inputlist = input()
#     result = output(inputlist)
#     print(result)

def commonprefix(m):
    if not m:
        return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1


def output(inputlist):
    if inputlist == []:
        return ''
    length = len(inputlist)
    result = []
    start = 0
    end = 0
    for i, strs in enumerate(inputlist):
        if i+1 < length:
            end = len(commonprefix([strs, inputlist[i+1]]))
        maxstr = max(start, end)
        result.append(strs[0:maxstr+1])
        start = end
        end = 0
    return result
def not_empty(s):
    return s and s.strip()

if __name__ == '__main__':
    inputlist = list(map(str, input().split(',')))
    for i in inputlist:
        if i=='':
            inputlist.remove(i)
    result = output(inputlist)
    resultstr = ''
    for i in result:
        resultstr += str(i)+','
    print(resultstr[:-1])
