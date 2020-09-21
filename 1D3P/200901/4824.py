import sys


def is_float(n):
    return n % 1 != 0


while True:
    num_list = list(map(float, sys.stdin.readline().split()))
    num_list.sort()
    if num_list[0] == 0.0:
        break

    L, M, N = num_list
    for i, num in enumerate(num_list):
        if is_float(num):
            L = num
            N = num_list[(i+1)%3]
            M = num_list[(i+2)%3]
            if M > N:
                N, M = M, N

    if 125 > N or 90 > M or 0.25 > L:
        print('not mailable')
    elif N <= 290 and M <= 155 and L <= 7:
        print('letter')
    elif N <= 380 and M <= 300 and L <= 50:
        print('packet')
    elif N + 2*M + 2*L <= 2100:
        print('parcel')
    else:
        print('not mailable')
