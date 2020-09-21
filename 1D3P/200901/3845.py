import sys

while True:
    N, M, L = map(float, sys.stdin.readline().split())
    if N == 0.0 and M == 0.0 and L == 0.0:
        break

    nums = dict()
    nums['row'] = list(map(float, sys.stdin.readline().split()))
    nums['col'] = list(map(float, sys.stdin.readline().split()))
    nums['row'].sort()
    nums['col'].sort()

    lens = dict()
    lens['row'] = 75
    lens['col'] = 100

    clear = dict()
    for key in nums.keys():
        clear[key] = True
        NorM = len(nums[key])
        for i, num in enumerate(nums[key]):
            if (i == 0 and num > L/2) or (i == NorM-1 and lens[key] - num > L/2):
                clear[key] = False
            elif num - nums[key][i-1] > L:
                clear[key] = False

    if clear['row'] and clear['col']:
        print('YES')
    else:
        print('NO')
