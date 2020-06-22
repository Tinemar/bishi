
import itertools

def output(N, nums):
    full_nums = [n for n in range(1, N + 1)]
    full = list(itertools.permutations(full_nums,N))
    result = 0
    for num in full:
        i = 0
        while i <= len(num) - 1:
            if i == len(num) - 1:
                result += 1
                print(num)
                break
            if nums[i] == 0 and num[i] < num[i + 1]:
                i += 1
            elif nums[i] == 1 and num[i] > num[i + 1]:
                i += 1
            else:
                break

    return result

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split(' ')))
    result = output(N, nums)
    print(result)
