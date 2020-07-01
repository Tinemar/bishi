# 字符串中最长连续数字字串
def LongestNumSubstring(string):
    if not string or string == '':
        return 0
    index = 0
    length = 0
    result = [0, 0]
    while index < len(string)-1:
        length = 0
        # 扫到了数字才记录index，长度+1
        while string[index].isdigit():
            length += 1
            index += 1
        # 记录了数字，那么更新全局长度和index，遇到更长的就替换
        if length != 0 and result[1] < length:
            result[1] = length
            result[0] = index-length
        index += 1
    return string[result[0]:result[0]+result[1]]


def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    from collections import defaultdict
    lookup = defaultdict(int)
    for i in t:
        lookup[i] += 1
    start = 0
    end = 0
    count = len(t)
    minlen = len(s)+1
    result = ""
    while end < len(s):
        if lookup[s[end]] > 0:
            count -= 1
        lookup[s[end]] -= 1
        end += 1
        while count == 0:
            if minlen > end-start:
                minlen = end-start
                result = s[start:end]
            if lookup[s[start]] == 0:
                count += 1
            lookup[s[start]] += 1
            start += 1
    return result


print(minWindow('ADOBECODECNABNC', 'ABC'))


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    from collections import defaultdict
    look = defaultdict(int)
    start = 0
    end = 0
    maxlen = 0
    while end < len(s):
        look[s[end]] += 1
        while look[s[end]] != 1:
            look[s[start]] -= 1
            start += 1
        if maxlen < end-start+1:
            maxlen = end-start+1
        end += 1
    return maxlen, start, end


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    from collections import defaultdict
    look = defaultdict(int)
    for i in s1:
        look[i] += 1
    start = 0
    end = 0
    count = len(s1)
    while end < len(s2):
        if look[s2[end]] > 0:
            count -= 1
        look[s2[end]] -= 1
        end += 1
        while count == 0:
            if look[s2[start]] == 0:
                if end-start == 1:
                    return True
                count += 1
            else:
                start += 1

        return False


print(checkInclusion('ab', 'aba'))
# 最长公共子序列LCS


def LCS(s, t):
    dp = []
    for i in range(len(s)+1):
        temp = [0]*(len(t)+1)
        dp.append(temp)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s)][len(t)]
# 最连续长公共子串LCS
def LCS2(s,t):
    dp = []
    for i in range(len(s)+1):
        temp = [0]*(len(t)+1)
        dp.append(temp)
    maxlen = 0
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                if maxlen<=dp[i][j]:
                    maxlen = dp[i][j]
            else:
                dp[i][j] = 0
    return maxlen
print(LCS2('ABACBDAB', 'BDCABA'))
