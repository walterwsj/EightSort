# 冒泡排序
def bubble_sort(test_list):
    if test_list is None or len(test_list) == 0:
        return -1
    if len(test_list) == 1:
        return test_list
    len_list = len(test_list)
    border = len_list - 1
    tmp_index = 0
    for i in range(len_list):
        is_sorted = True
        for j in range(border):
            if test_list[j] > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]
                is_sorted = False
                tmp_index = j
        if border != tmp_index:
            border = tmp_index
        if is_sorted:
            break
    return test_list


# 快速排序-递归
def get_pivot(unsorted_list, head, tail):
    border = head
    tmp = unsorted_list[head]

    for i in range(head + 1, tail + 1):
        if unsorted_list[i] < tmp:
            border += 1
            unsorted_list[border], unsorted_list[i] = unsorted_list[i], unsorted_list[border]

    if border != head:
        unsorted_list[border], unsorted_list[head] = unsorted_list[head], unsorted_list[border]
    return border


def quick_sort(test_list, left, right):
    if left >= right:
        return
    key = get_pivot(test_list, left, right)
    quick_sort(test_list, left, key - 1)
    quick_sort(test_list, key + 1, right)
    return test_list


def quick_sort_no_recurse(test_list):
    stack = []
    index_dict = {}
    index_dict["left"] = 0
    index_dict["right"] = len(test_list) - 1
    stack.append(index_dict)
    while len(stack):
        tmp = stack.pop()
        key = get_pivot(test_list, tmp["left"], tmp["right"])
        if key-1 > tmp["left"]:
            index_dict["right"] = key - 1
            stack.append(index_dict)
        if key+1 < tmp["right"]:
            index_dict["left"] = key + 1
            stack.append(index_dict)
    return test_list


a = [2, 1, 4, 3, 2]
print(quick_sort_no_recurse(a))
