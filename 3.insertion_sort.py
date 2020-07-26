# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/25 12:29

"""
程序说明：
    插入排序
    （目标是从小到大排序时）
    最好情况：顺序从小到大排序，O(n)
    最坏情况：逆序从大到小排序，O(n^2)
    平均时间复杂度：O(n^2)
    空间复杂度：O(1)
"""


def insertion_sort(arr):
    for i in range(len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]  # 当前比前一个小，另current对应的arr[pre_index+1]设为pre_index的数
            pre_index -= 1  # 向前移动
        arr[pre_index + 1] = current  # 将移动额值插入到pre_index的后面
    return arr

if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(insertion_sort(lis))