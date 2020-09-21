import sys
from string import ascii_lowercase
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def binary_search(scores, cutline):
    start, end = 0, len(scores)
    while end - start > 0:
        mid = (start + end) // 2
        if scores[mid][0] >= cutline:
            end = mid
        else:
            start = mid+1
    mid = (start + end) // 2
    return [id for score, id in scores[mid:]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    langs = {'cpp': [], 'java': [], 'python': []}
    jobs = {'backend': [], 'frontend': []}
    years = {'junior': [], 'senior': []}
    foods = {'chicken': [], 'pizza': []}
    non_score_info = [langs, jobs, years, foods]
    scores = []
    for person_id, person_info in enumerate(info):
        person_info_list = person_info.split(' ')
        for i, detail in enumerate(person_info_list):
            if i < 4:
                non_score_info[i][detail].append(person_id)
            else:
                scores.append((int(detail), person_id))

    scores.sort()
    answer_list = []
    for require in query:
        require_list = require.split(' and ')
        require, cutline = require_list[3].split(' ')
        require_list[3] = require
        condition_num = len(require_list) - require_list.count('-')
        person_ids = set(range(len(info)))
        for i, detail in enumerate(require_list):
            if detail != '-':
                person_ids &= set(non_score_info[i][detail])
        person_ids &= set(binary_search(scores, int(cutline)))
        # person_ids += [person_id for score, person_id in scores if score >= int(cutline)]

        answer_list.append(len(person_ids))
    print(answer_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
