import sys


def packing_list(weight_lists, index, current_weight, packing_lists):
    if index == len(weight_lists) - 1:
        packing_lists.append(current_weight)
        packing_lists.append(current_weight + weight_lists[index])
    else:
        packing_list(weight_lists, index+1, current_weight, packing_lists)
        packing_list(weight_lists, index+1, current_weight+weight_lists[index], packing_lists)


N, C = map(int, sys.stdin.readline().split())
if N == 1:
    weight = int(sys.stdin.readline())
    if weight > C:
        print(1)
    else:
        print(2)
else:
    weight_list = list(map(int, sys.stdin.readline().split()))
    weight_list.sort()

    weight_list1 = weight_list[:len(weight_list)//2]
    weight_list2 = weight_list[len(weight_list)//2:]

    packing_list1 = list()
    packing_list2 = list()
    packing_list(weight_list1, 0, 0, packing_list1)
    packing_list(weight_list2, 0, 0, packing_list2)
    packing_list1.sort()
    packing_list2.sort()

    pointer = len(packing_list2) - 1
    sum = 0
    for packing_weight1 in packing_list1:
        while pointer >= 0 and packing_weight1 + packing_list2[pointer] > C:
            pointer -= 1
        sum += (pointer+1)
    print(sum)
