# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/25 11:23

"""
程序说明：
    选择排序     （目标是从小到大排序时）
    最好、最坏、平均时间复杂度都是O(n^2)
    空间复杂度：O(1)
"""


def selection_sort(arr):
    """
    普通版
    """
    for i in range(len(arr) -1):
        min_idx = i  # 默认第一个是最小的
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # i不是最小时与第一个交换
    return arr

def seletion_sort_pythonic(arr):
    """
    在python中可以这么写
    """
    for i in range(len(arr) -1):
        min_idx = arr.index(min(arr[i:]))  # 获取最小的元素的序号，如果并列获取第一个  # 内置函数min的复杂度也是O(n)
        if min_idx - i:  # 如果不为0，继续
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # return arr  # 甚至可以不用return 因为直接对应内存空间的元素进行了排序修改。


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(selection_sort(lis))

    lis = [3, 4, 2, 1, 6, 5]
    seletion_sort_pythonic(lis)
    print(lis)

