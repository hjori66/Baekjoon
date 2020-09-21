import sys

test_num = 0
while True:
    test_num += 1
    target = sys.stdin.readline().rstrip()
    if target == '.':
        break
    real_target = target.replace('_', '')

    total = 0
    while True:
        line = sys.stdin.readline()
        if line[0] == '0':
            break

        word_list = line.split()
        for word in word_list[1:]:
            if len(target) <= len(word):
                word = list(word)
                if len(real_target) == 0:
                    checker = True
                else:
                    checker = False
                for i in range(len(word) - len(target) + 1):
                    subword = list(word[i:i+len(target)])
                    for j, alphabet in enumerate(real_target):
                        if alphabet in subword:
                            subword.remove(alphabet)
                            if j == len(real_target) - 1:
                                checker = True
                        else:
                            break
                if checker:
                    total += 1
    print("Test {}: {}".format(test_num, total))
