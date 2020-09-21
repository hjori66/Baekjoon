import sys

N = int(sys.stdin.readline())
alpha_to_sum = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
leading_zero = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    length = len(word)
    leading_zero[word[0]] = 0
    while length > 0:
        length -= 1
        alpha = word[0]
        word = word[1:]
        sum = alpha_to_sum[alpha]
        alpha_to_sum[alpha] = sum + 10 ** length

zero_candidate = 'Z'
for alpha in leading_zero.keys():
    if leading_zero[alpha]:
        if zero_candidate == 'Z':
            zero_candidate = alpha
        elif alpha_to_sum[zero_candidate] > alpha_to_sum[alpha]:
            zero_candidate = alpha

sum = 0
number = 9
alpha_to_sum.pop(zero_candidate)
for key, value in sorted(alpha_to_sum.items(), reverse=True, key=lambda item: item[1]):
    sum += value * number
    number -= 1
print(sum)
