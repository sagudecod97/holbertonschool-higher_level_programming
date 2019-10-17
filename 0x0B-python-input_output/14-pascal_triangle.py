#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    lists = []
    count = 1

    for i in range(n):
        if count == 1:
            lists.append([1])
            count += 1
            continue
        elif count == 2:
            lists.append([1,1])
            count += 1
            continue
        else:
            new_list = []
            for j in range(count):
                if j == 0:
                    new_list.append(1)
                elif j == count - 1:
                    new_list.append(1)
                elif j == 1:
                    number = 0
                    for h in range(count - 1):
                        if h < len(lists[count - 2]) - 1:
                            number = lists[count - 2][h] + lists[count - 2][h + 1]
                            new_list.append(number)
                else:
                    continue
            count += 1
            lists.append(new_list)

    return lists
