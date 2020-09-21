import sys

homerun_list = list()
for i in range(10000):
    homerun_list.append(i)
rounds = 0
text_list = list()

print("Allow the Duplicates? / (y or n)")
dup = sys.stdin.readline().strip()
if dup != 'y' and dup != 'n':
    print("Error!!")
if dup == 'n':
    pop_list = list()
    for index, candidate in enumerate(homerun_list):
        candidate_1000 = candidate // 1000
        candidate_100 = (candidate // 100) % 10
        candidate_10 = (candidate // 10) % 10
        candidate_1 = candidate % 10
        if candidate_1000 == candidate_100 \
                or candidate_1000 == candidate_10 \
                or candidate_1000 == candidate_1 \
                or candidate_100 == candidate_10 \
                or candidate_100 == candidate_1 \
                or candidate_10 == candidate_1:
            pop_list.append(index)
    pop_list.reverse()
    for pop_index in pop_list:
        homerun_list.pop(pop_index)
    print("No Duplicate -> # of possible answers : " + str(len(homerun_list)))

while True:
    rounds += 1
    print("Write the target number(ABCD)")
    target = int(sys.stdin.readline())
    print("Target Number : {}".format(target))

    target_1000 = target // 1000
    target_100 = (target // 100) % 10
    target_10 = (target // 10) % 10
    target_1 = target % 10

    print("Write the number of strikes and balls(?S ?B), Type two integers")
    s, b = map(int, sys.stdin.readline().split())
    print("Result : {}S {}B".format(s, b))

    pop_list = list()
    for index, candidate in enumerate(homerun_list):
        strike_count = 0
        ball_count = 0
        candidate_1000 = candidate // 1000
        candidate_100 = (candidate // 100) % 10
        candidate_10 = (candidate // 10) % 10
        candidate_1 = candidate % 10
        if target_1000 == candidate_1000:
            strike_count += 1
        if target_100 == candidate_100:
            strike_count += 1
        if target_10 == candidate_10:
            strike_count += 1
        if target_1 == candidate_1:
            strike_count += 1
        if target_1000 == candidate_100:
            ball_count += 1
        if target_1000 == candidate_10:
            ball_count += 1
        if target_1000 == candidate_1:
            ball_count += 1
        if target_100 == candidate_1000:
            ball_count += 1
        if target_100 == candidate_10:
            ball_count += 1
        if target_100 == candidate_1:
            ball_count += 1
        if target_10 == candidate_1000:
            ball_count += 1
        if target_10 == candidate_100:
            ball_count += 1
        if target_10 == candidate_1:
            ball_count += 1
        if target_1 == candidate_1000:
            ball_count += 1
        if target_1 == candidate_100:
            ball_count += 1
        if target_1 == candidate_10:
            ball_count += 1
        if strike_count != s or ball_count != b:
            pop_list.append(index)

    pop_list.reverse()
    for pop_index in pop_list:
        homerun_list.pop(pop_index)

    text = str(target_1000) + str(target_100) + str(target_10) + str(target_1) \
           + " : " + str(s) + "S" + str(b) + "B -> # of possible answers : " + str(len(homerun_list))
    text_list.append(text)

    print("Round {}, Game Log".format(rounds))
    for log in text_list:
        print(log)
    if len(homerun_list) <= 30:
        print("possible answers", homerun_list)
    print()
