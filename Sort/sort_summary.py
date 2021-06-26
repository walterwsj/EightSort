import copy
import random


# region 交换排序

# 冒泡排序 稳定
def sort_bubble(test_list):
    if test_list is None:
        return -1
    len_list = len(test_list)
    if len_list <= 0:
        return test_list
    border = len_list - 1
    index_tmp = -1
    for _ in range(len_list):
        is_sorted = True
        for j in range(border):
            if test_list[j] > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]
                is_sorted = False
                index_tmp = j
        if border != index_tmp:
            border = index_tmp
        if is_sorted:
            break
    return test_list


# 快速排序
def sort_quick(test_list, start, end):
    if start > end:
        return
    key = get_pivot(test_list, start, end)
    sort_quick(test_list, start, key - 1)
    sort_quick(test_list, key + 1, end)
    return test_list


def get_pivot(unsorted_list, left_index, right_index):
    border, tmp = left_index, unsorted_list[left_index]
    for i in range(left_index, right_index + 1):
        if unsorted_list[i] < tmp:
            border += 1
            unsorted_list[border], unsorted_list[i] = unsorted_list[i], unsorted_list[border]
    if border != left_index:
        unsorted_list[border], unsorted_list[left_index] = unsorted_list[left_index], unsorted_list[border]
    return border


def sort_quick_uo_recurse(test_list):
    index_dic = {'left': 0, 'right': len(test_list) - 1}
    stack = [index_dic]
    while len(stack):
        tmp = stack.pop()
        key = get_pivot(test_list, tmp['left'], tmp['right'])
        if key - 1 > tmp['left']:
            l_part = {'left': tmp['left'], 'right': key - 1}
            stack.append(l_part)
        if key + 1 < tmp['right']:
            r_part = {'left': key + 1, 'right': tmp['right']}
            stack.append(r_part)
    return test_list


# endregion

# region 插入排序

# 插入排序
def sort_insert(test_list):
    len_list = len(test_list)
    for i in range(len_list):
        cur_index = i
        while cur_index >= 1 and test_list[cur_index] < test_list[cur_index - 1]:
            test_list[cur_index], test_list[cur_index - 1] = test_list[cur_index - 1], test_list[cur_index]
            cur_index -= 1
    return test_list


# 希尔排序
def sort_shell(test_list):
    len_list = len(test_list)
    gap = len_list // 2
    while gap:
        for i in range(gap, len_list):
            j = i
            while j > 0 and test_list[j - gap] > test_list[j]:
                test_list[j - gap], test_list[j] = test_list[j], test_list[j - gap]
                j -= gap
        gap //= 2
    return test_list


# endregion

# region 选择排序

# 选择排序
def sort_select(test_list):
    len_list = len(test_list)
    for i in range(len_list):
        min_index = i
        for j in range(i + 1, len_list):
            if test_list[j] < test_list[min_index]:
                min_index = j
        if min_index != i:
            test_list[min_index], test_list[i] = test_list[i], test_list[min_index]
    return test_list


# 堆排序
def heap_build(test_list):
    len_list = len(test_list)
    for i in range(len_list // 2)[::-1]:
        heap_adjust(test_list, i, len_list)


def heap_adjust(test_list, cur_index, border):
    l_leaf = 2 * cur_index + 1
    r_leaf = 2 * cur_index + 2
    tmp_index = cur_index

    if l_leaf < border and test_list[l_leaf] > test_list[tmp_index]:
        tmp_index = l_leaf
    if r_leaf < border and test_list[r_leaf] > test_list[tmp_index]:
        tmp_index = r_leaf
    if tmp_index != cur_index:
        test_list[tmp_index], test_list[cur_index] = test_list[cur_index], test_list[tmp_index]
        heap_adjust(test_list, tmp_index, border)


def sort_heap(test_list):
    len_list = len(test_list)
    heap_build(test_list)
    for i in range(len_list)[::-1]:
        test_list[0], test_list[i] = test_list[i], test_list[0]
        heap_adjust(test_list, 0, i)
    return test_list


# endregion

# region 归并排序
# 归并排序
def merge_core(list_a, list_b):
    res = []
    while len(list_a) and len(list_b):
        if list_a[0] < list_b[0]:
            res.append(list_a.pop(0))
        else:
            res.append(list_b.pop(0))
    if len(list_a):
        res.extend(list_a)
    if len(list_b):
        res.extend(list_b)
    return res


def sort_merge(test_list):
    if len(test_list) <= 1:
        return test_list
    mid_index = len(test_list) // 2
    l_part = sort_merge(test_list[:mid_index])
    r_part = sort_merge(test_list[mid_index:])
    return merge_core(l_part, r_part)


# endregion

# region 基数排序

# 计数排序
def sort_count(test_list):
    max_value = test_list[0]
    min_value = test_list[0]
    for i in test_list:
        if max_value < i:
            max_value = i
        if min_value > i:
            min_value = i
    gap = max_value - min_value
    tmp_list = [0 for _ in range(gap + 1)]

    for i in test_list:
        tmp_list[i - min_value] += 1

    for i in range(1, gap + 1):
        tmp_list[i] += tmp_list[i - 1]

    result_list = [0 for _ in range(len(test_list))]
    for i in range(len(test_list)):
        result_list[tmp_list[test_list[i] - min_value] - 1] = test_list[i]
        tmp_list[test_list[i] - min_value] -= 1
    return result_list


# 桶排序
def sort_bucket(test_list):
    bucket_num = len(test_list)
    min_value = test_list[0]
    max_value = test_list[0]
    for i in test_list:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    gap = max_value - min_value

    buckets = [[] for _ in range(bucket_num)]

    for i in range(bucket_num):
        index = (test_list[i] - min_value) * (bucket_num - 1) // gap
        buckets[index].append(test_list[i])

    for bucket in buckets:
        sorted(bucket)

    return [i for j in buckets for i in j]


# endregion

# region 测试
def sort_test(test):
    bucket_num = len(test)
    max_value = test[0]
    min_value = test[0]
    for i in test:
        if max_value < i:
            max_value = i
        if min_value > i:
            min_value = i
    gap = max_value - min_value

    buckets = [[] for _ in range(bucket_num)]
    for i in range(bucket_num):
        index = (test[i] - min_value) * (bucket_num - 1) // gap
        buckets[index].append(test[i])
    for bucket in buckets:
        sorted(bucket)

    return [j for i in buckets for j in i]


# endregion

if __name__ == '__main__':
    arr_list = [i for i in range(10)]
    random.shuffle(arr_list)
    print(arr_list)
    print(sort_test(arr_list))
