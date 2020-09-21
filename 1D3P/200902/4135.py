import sys, math

N = int(sys.stdin.readline())
for i in range(N):
    num_list = list(map(float, sys.stdin.readline().split()))
    K = int(num_list[0])
    num_list = num_list[1:]
    # num_list.sort()

    sum = 0
    for j, num in enumerate(num_list):
        if j == 0 or j == K-1:
            sum += num
        if j < K-1:
            num2 = num_list[j+1]
            sum += math.sqrt((num+num2)**2 - (num-num2)**2)
    print("{0:.3f}".format(sum))
