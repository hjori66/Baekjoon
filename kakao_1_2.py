from itertools import combinations


def solution(orders, course):
    order_list_dict = dict()
    for c in course:
        order_list_dict[c] = dict()

    for order in orders:
        for c in course:
            for menu in list(combinations(order, c)):
                menu = list(menu)
                menu.sort()
                menu = ''.join(menu)
                if not menu in order_list_dict[c].keys():
                    order_list_dict[c][menu] = 1
                else:
                    order_list_dict[c][menu] += 1

    menu_list = []
    for c in course:
        max_keys = []
        max_value = 0
        for i, (key, value) in enumerate(order_list_dict[c].items()):
            if i == 0 or max_value == value:
                max_keys.append(key)
            elif max_value < value:
                max_keys = [key]
            if i == 0 or max_value < value:
                max_value = value
        if max_value > 1:
            menu_list += max_keys
    menu_list.sort()
    return menu_list


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

sol = solution(orders, course)
print(sol)
