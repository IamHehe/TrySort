# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/27 0:07

"""
程序说明：
    快速排序
    （目标是从小到大排序时）
    最好情况：O(n log n)
    最坏情况：O(n^2)，正序or逆序排列的情况
    平均时间复杂度：O(n log n)
    空间复杂度：相当于一个二分的递归算法，所以空间复杂度等于递归深度为 O(log n)
    不稳定
    1. 在获得pivot位置时，类似冒泡排序，大的向右，小的像左
    2. 快速排序的最坏运行情况是 O(n^2)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，
    且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。
    所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
    归并还有一个merge的过程，但是快排分完就比较完了
# """

def quickSort(arr, left=0, right=None):
    """
    :param arr: 需要排序的列表
    :param left:  需要排序的左范围index，默认为零
    :param right:  需要排序的右范围index
    :return:
    """
    right = right if right is not None else len(arr)-1  # 当不是空值的时候取值，否则取len(arr)-1，即列表截止位置
    if left < right:  # 当左边小于右边时，
        partitionIndex = partition(arr, left, right)    # 获取基准pivot
        quickSort(arr, left, partitionIndex-1)  # 对左边排序，递归，下同 O(log n)，当全是一边，只有左 或 只有右，这种情况，还是O(n)
        quickSort(arr, partitionIndex+1, right)  # 对右边排序
    return arr  # 可以无返回


def partition(arr, left, right):
    """
    :param arr: 列表
    :param left:  左index
    :param right: 右index
    :return: pivot的位置
    """
    pivot = left  # 默认第一个为基准
    index = pivot+1  # 从第二个开始轮，index表示
    for i in range(index, right+1):   # O (n)
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1  # 只有遇到左边小的情况右移
    swap(arr, pivot, index-1)
    return index-1  # 返回pivot的值


def swap(arr, i, j):
    # 涉及转化位置的复用，所以单独成一个函数
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    # lis = [3, 4, 2, 1, 6, 5]
    lis = [5, 2, 4, 7, 8, 1]
    print(quickSort(lis))
    # print(lis)