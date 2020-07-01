class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start = 0
        if s == ""or len(s) == 1:
            return 0
        for i in s:
            if i == ')':
                start += 1
            else:
                break
        end = start
        if start >= len(s) - 1:
            return 0
        stack = []
        result = []
        while end < len(s):
            if s[end] == '(':
                stack.append(end)
            else:
                if len(stack) > 0:
                    l = stack.pop()
                    result.append(l)
                    result.append(end)
            end += 1
        result = sorted(result)
        print(result)
        if result == []:
            return 0
        else:
            return result[-1] - result[0] + 1
s = Solution()
print(s.longestValidParentheses())