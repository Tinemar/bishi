import sys


def output(total_num,sco,index):
    less_than_num = 0
    for s in sco:
        if(s<=sco[index-1]):
            less_than_num += 1
    return (less_than_num-1)/total_num
if __name__ == "__main__":
    inputs = []
    for i in range(3):
        if i==0:
            total_num = int(input())
        if i==1:
            sco_str = input().split()
            sco = []
            for s in sco_str:
                sco.append(int(s))
        if i==2:
            times = int(input())
    for t in range(times):
        index = int(input())
        inputs.append(index)
    for index in inputs:
        result = output(total_num,sco,index)
        result = "%.6f%%"%(result*100)
        print(result[:-1])