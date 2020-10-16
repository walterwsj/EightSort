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
        if key - 1 > tmp["left"]:
            index_dict["right"] = key - 1
            stack.append(index_dict)
        if key + 1 < tmp["right"]:
            index_dict["left"] = key + 1
            stack.append(index_dict)
    return test_list


# 桶排序
def bucket_sort(test_list):
    bucket_num = len(test_list)
    min_value = test_list[0]
    max_value = test_list[0]
    for i in test_list:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    gap = max_value - min_value

    buckets = [[] for i in range(bucket_num)]
    for i in range(bucket_num):
        bucket_index = int((test_list[i] - min_value) * (bucket_num - 1) / gap)
        buckets[bucket_index].append(test_list[i])

    for bucket in buckets:
        bucket = bubble_sort(bucket)

    return [i for j in buckets for i in j]


# 计数排序
def count_sort(test_list):
    min_value = test_list[0]
    max_value = test_list[0]
    for i in test_list:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    gap = max_value - min_value + 1
    count_list = [0 for i in range(gap)]

    for i in range(len(test_list)):
        count_list[test_list[i] - min_value] += 1

    for j in range(1, len(count_list)):
        count_list[j] += count_list[j - 1]

    result_list = [0 for i in range(len(test_list))]

    for i in range(len(test_list))[::-1]:
        result_list[count_list[test_list[i] - min_value] - 1] = test_list[i]
        count_list[test_list[i] - min_value] -= 1

    return result_list


# 选择排序
def select_sort(test_list):
    for i in range(len(test_list)):
        tmp_min = i
        for j in range(i + 1, len(test_list)):
            if test_list[j] < test_list[tmp_min]:
                tmp_min = j
        if tmp_min != i:
            test_list[i], test_list[tmp_min] = test_list[tmp_min], test_list[i]
    return test_list


# 堆排序
def build_head(test_list):
    for i in range(int(len(test_list) / 2))[::-1]:
        adjust_head(test_list, i, len(test_list))


def adjust_head(test_list, current_index, border):
    l_leaf = 2 * current_index + 1
    r_leaf = 2 * current_index + 2
    tmp = current_index

    if l_leaf < border and test_list[tmp] < test_list[l_leaf]:
        tmp = l_leaf
    if r_leaf < border and test_list[tmp] < test_list[r_leaf]:
        tmp = r_leaf
    if tmp != current_index:
        test_list[tmp], test_list[current_index] = test_list[current_index], test_list[tmp]
        adjust_head(test_list, tmp, border)


def heap_sort(test_list):
    build_head(test_list)
    for i in range(len(test_list))[::-1]:
        test_list[i], test_list[0] = test_list[0], test_list[i]
        adjust_head(test_list, 0, i)
    return test_list


# 插入排序
def insert_sort(test_list):
    for i in range(1, len(test_list)):
        former = i - 1
        tmp = test_list[i]
        while former >= 0 and tmp < test_list[former]:
            test_list[former + 1] = test_list[former]
            former -= 1
        if former + 1 != i:
            test_list[former + 1] = tmp
    return test_list


# 希尔排序
def shell_sort(test_list):
    step = len(test_list)
    while step:
        for i in range(step, len(test_list)):
            former = i - step
            tmp = test_list[i]
            while former >= 0 and tmp < test_list[former]:
                test_list[former + step] = test_list[former]
                former -= step
            if former + step != i:
                test_list[former + step] = tmp
        step = step // 2
    return test_list


# 归并排序
def merge_core(l_part, r_part):
    result = []
    while len(l_part) and len(r_part):
        if l_part[0] < r_part[0]:
            result.append(l_part.pop(0))
        else:
            result.append(r_part.pop(0))
    if len(l_part):
        result.extend(l_part)
    if len(r_part):
        result.extend(r_part)
    return result


def merge_sort(test_list):
    if len(test_list) == 1:
        return test_list
    mid = int(len(test_list)/2)
    l_part = merge_sort(test_list[:mid])
    r_part = merge_sort(test_list[mid:])
    return merge_core(l_part, r_part)


a = [2, 1, 4, 3, 2]
print(merge_sort(a))
