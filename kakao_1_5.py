import heapq

play_time = "50:00:50"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]


def time_to_num(HHMMSS):
    h, m, s = HHMMSS.split(':')
    return int(h)*3600 + int(m)*60 + int(s)


def num_to_time(num):
    return str(100 + num//3600)[1:] + ':' + str(100 + (num//60)%60)[1:] + ':' + str(100 + num%60)[1:]


play_num = time_to_num(play_time)
adv_num = time_to_num(adv_time)
log_nums = [tuple(map(time_to_num, log.split('-'))) for log in logs]
log_nums.sort()

possible_start_total = dict()
reversed_log_nums = list()
for i, log_num in enumerate(log_nums):
    start, end = log_num
    adv_end = start + adv_num
    if adv_end > play_num:
        break
    possible_start_total[start] = min(end-start, adv_num)
    while reversed_log_nums:
        end_, start_ = reversed_log_nums[0]
        if max(end_, start_+adv_num) <= start:
            heapq.heappop(reversed_log_nums)
        else:
            break
    for reversed_log_num in reversed_log_nums:
        end_, start_ = reversed_log_num
        possible_start_total[start_] += min(end, end_, start_+adv_num) - start
        possible_start_total[start] += min(min(end, end_) - start, adv_num)
    heapq.heappush(reversed_log_nums, (end, start))

print(possible_start_total)

if not possible_start_total:
    print(num_to_time(play_num - adv_num))
else:
    max_value = 0
    max_key = 0
    for i, (key, value) in enumerate(possible_start_total.items()):
        if i == 0 or max_value < value or (max_value == value and max_key > key):
            max_key, max_value = key, value
    print(num_to_time(max_key))
