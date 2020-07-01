# def IsContinuous(numbers):
#         # write code here
#         numbers = sorted(numbers)
#         zeronum = 0
#         gap = 0
#         for i in numbers:
#             if i==0:
#                 zeronum += 1
#         start  = zeronum
#         while(start+1<len(numbers)):
#             if numbers[start] == numbers[start+1]:
#                 return False
#             gap += numbers[start+1] - numbers[start] - 1
#             start +=1
#         if zeronum >= gap:
#             else: 
#             return False
# print(IsContinuous([0,3,2,6,4]) )
#             return True
class Solution:
    def Print(self, pRoot):
        # write code here
        stack1 = [pRoot]
        stack2 = []
        result = []
        while stack1 or stack2:
            if stack1:
                temp = []
                for node in stack1:
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
                    temp.append(node.val)
                stack1 = []
                result.append(temp)
            if stack2:
                temp = []
                for node in stack2:
                    if node.left:
                        stack1.append(node.left)
                    if node.right:
                        stack1.append(node.right)
                    temp.append(node.val)
                stack2 = []
                result.append(temp.reverse())
        return result