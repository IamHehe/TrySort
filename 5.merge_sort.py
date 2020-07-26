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


if __name__ == "__main__":
    lis = [3, 4, 2, 1, 6, 5]
    print(merge_sort(lis))