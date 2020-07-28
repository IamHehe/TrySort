# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/27 23:02

"""
程序说明：
    堆排序，可以看做是selection srot的优化版
        用堆结构选择最值，替代了循环比较，将O(n)减小为O(log n)
    最好情况：O(n log n)
    最坏情况：O(n log n)
    平均时间复杂度：O(n log n)
    空间复杂度：没有开辟新空间，O(1)
    不稳定

"""


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)  # 原地构造最大堆，不开辟新的数组进行存储
    for i in range(len(arr)-1, 0, -1):  # 如何是求前k个数，则改为range(len(arr)-1,len(arr)-1-k, -1)，输出后几位即可
        swap(arr, 0, i)
        arrLen -= 1  # 长度减1
        heapify(arr, 0)
    return arr


def buildMaxHeap(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)  # 递归，将当前节点与左右节点相比较，并把最大值继续传递，


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    # lis = [5, 2, 4, 7, 8, 1]
    print(heapSort(lis))