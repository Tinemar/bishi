from collections import defaultdict
import math
import os
import random
import re
import sys


def dfs(node, dicts, res):
    if dicts[node]:
        res.extend(dicts[node])
        for n in dicts[node]:
            dfs(n, dicts, res)
    else:
        return


def costsOfNodes(lines):
    dicts = {}
    for line in lines:
        for i, k in enumerate(line.split(',')):
            if i == 0:
                if k not in dicts:
                    dicts[k] = []
                key = k
            else:
                if k in dicts:
                    dicts[k].append(key)
                else:
                    dicts[k] = [key]
    output = []
    res = []
    for key in dicts.keys():
        dfs(key, dicts, res)
        dicts[key] = list(set(res))
        output.append(key + "," + str(len(dicts[k]) + 1))
    output = sorted(output, key=lambda x: x[0])
    return output


print(costsOfNodes(['X,Y']))


# def divide(dividend,divisor):
#     if dividend == 0:
#         outputurn "0"
#     result = ""
#     res = []
#     left, right = divmod(dividend, divisor)
#     res.append(str(left))
#     if right == 0:
#         outputurn result.join(res)

#     else:
#         res.append(".")
#     index = {right: len(res)}
#     while right:
#         right *= 10
#         left, right = divmod(right, divisor)
#         res.append(str(left))
#         if right in index:
#             res.insert(index[right], "(")
#             res.append(")")
#             break
#         index[right] = len(res)
#     outputurn result.join(res)
