# def output(kill,PID,PPID):
#     result = 0
#     tree = {}
#     for i in range(len(PPID)):
#         if PPID[i]!=0:
#             tree[PPID[i]]=[]
#     for i in range(len(PID)):
#         if PPID[i]!=0:
#             tree[PPID[i]].append(PID[i])
#     if kill in PID:
#         result += 1

#     kill_list = [kill]
#     print(tree)
#     while kill_list!=[]:
#         tmp = []
#         for k in kill_list:
#             if k in tree.keys():
#                 result += len(tree[k])
#                 for i in tree[k]:
#                     tmp.append(i)
#         kill_list = tmp
#     return result
    
# if __name__ == '__main__':
#     PID = list(map(int, input().split(' ')))
#     PPID = list(map(int, input().split(' ')))
#     kill = int(input())
#     result = output(kill,PID,PPID)
#     print(result)

def output(m,b):
    result = b
    while m>0:
        result += m*(result)-(m-1)
        m -= 1
        print(result,m)
    return result
if __name__ == '__main__':
    m = int(input())
    b = int(input())
    result = output(m,b)
    print((18^14))