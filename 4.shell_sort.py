# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/25 13:21

"""
程序说明：
    希尔排序
    （目标是从小到大排序时）
    最好情况：顺序从小到大排序，O(n log^2 n)
    最坏情况：逆序从大到小排序，O(n^2)
    平均时间复杂度：O(n log n)
    空间复杂度：O(1)
    不稳定
"""


def shellSort(arr):
    # shell排序的性能和选取的步长序列还有关系，因为相比交换，shell排序更加注重的是“比较”
    # 参考：https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F
    # Shell本人推荐的是n//2，即 gap = len(arr)//2
    # 本处使用的步长是n//3
    gap = 1
    while gap < len(arr) // 3:
        gap = gap * 3 + 1
    while gap > 0:
        # 步长为1的时候程序等同于insertion sort，但是效率比直接insertion sort要高
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap //= 3  #
    return arr


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(shellSort(lis))