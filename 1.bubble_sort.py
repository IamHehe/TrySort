# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/25 11:23

"""
程序说明：
    冒泡排序法
     （目标是从小到大排序时）
    最好情况：顺序从小到大排序，O(n)
    最坏情况：逆序从大到小排序，O(n^2)
    平均时间复杂度：O(n^2)
    空间复杂度：O(1)
"""


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(bubbleSort(lis))

