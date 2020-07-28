# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/28 17:50

"""
程序说明：
    计数排序
    需要额外开辟一个空间来计数
    最好情况：O(n + k) n是输入数组长度，k是最大的数的大小。
    最坏情况：O(n + k)
    平均时间复杂度：O(n + k)
    空间复杂度：没有开辟新空间，O(k)
    稳定，可以想象这样一个过程，我们在从左到右遍历数组arr时，将数对应的object存入到新开辟数组buf中，
        在输出的时候按照存储的顺序进行输出，即保证了稳定性，为了展示这一过程，请见counting_sort_show_stability()方法
"""


def counting_sort(arr, max_num):
    """
    :param arr: 需要排序的列表
    :param max_num: 列表中的最大值
    """
    buf_len = max_num + 1
    buf = [0] * buf_len
    sort_idx = 0
    arr_len = len(arr)
    for i in range(arr_len):
        buf[arr[i]] += 1  # buf新建空间的时候已经初始化值为0，此处不用判断是否为空
    for i in range(buf_len):
        while buf[i] > 0:
            arr[sort_idx] = i
            sort_idx += 1
            buf[i] -= 1
    return arr


def counting_sort_show_stability(arr, max_num):
    """
    换一种写法展示其稳定性
    """
    buf = {i: [] for i in range(max_num+1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(arr)
    for i in range(arr_len):
        num = arr[i]
        buf[num].append(num)  # 按照顺序加入buf的[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(buf[i])
    return arr


if __name__ == "__main__":
    lis = [3, 4, 3, 3, 2, 2, 2, 2, 1, 4, 6, 5, 5, 6, 2, 1, 6, 5]
    print(counting_sort(lis, max(lis)))

    lis = [3, 4, 3, 3, 2, 2, 2, 2, 1, 4, 6, 5, 5, 6, 2, 1, 6, 5]
    print(counting_sort_show_stability(lis, max(lis)))
