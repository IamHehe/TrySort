# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/26 12:31

"""
程序说明：
    归并排序
    （目标是从小到大排序时）
    最好情况：顺序从小到大排序，O(n log n)
    最坏情况：逆序从大到小排序，O(n log n)
    平均时间复杂度：O(n log n)
    空间复杂度：O(n)
    稳定

"""

# 自上向下分，递归
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]  # 分
    return merge(merge_sort(left), merge_sort(right))  # 治：递归而下  # 共有log n +1 层即时间复杂度为# O(n * log n)


def merge(left, right):
        res = []  # 这里相当于开辟了同等大小的空间，使得空间复杂度为O(n)
        while left and right:  # O(n)
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left:  # O(n)
            res.append(left.pop(0))
        while right:  # O(n)
            res.append(right.pop(0))
        return res


# 归并排序，新增自下至上的迭代，通过扩展步长weight进行
# 参考：https://www.pythonheidong.com/blog/article/453039/
def BottomUp_merge_sort(a):
    n = len(a)
    b = a[:]  # 深拷贝一个a
    width = 1  # 步长
    while width < n:  # 步长小于列表长度
        start = 0  # 起始位置
        while start < n:
            mid = min(n, start + width)  # n只有在最后start+width超过整个句子的长度的时候才会被选取
            end = min(n, start + (2 * width))
            BottomUp_Merge(a, b, start, mid, end)
            start += 2 * width
        a = b[:]
        width *= 2  # 2 4 8  16 这样的方式获取
    return a

def BottomUp_Merge(a, b, start, mid, end):
    i = start
    j = mid
    for k in range(start, end):
        if i < mid and (j >= end or a[i] <= a[j]):  # j>=end 即后面的不尽兴操作，直接复制
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(merge_sort(lis))

    lis = [3, 4, 2, 1, 6, 5]
    lis = BottomUp_merge_sort(lis)
    print(lis)