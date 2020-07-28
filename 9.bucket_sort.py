# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/28 18:37

"""
程序说明：
    桶排序
    1）在额外空间充足的情况下，尽量增大桶的数量
    2）使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
      个人理解，如果都是整数还可以用计数排序来计数统计然后排序，但是如果是一个连续空间内的排序，即统计的是一个浮点类型的数组成
      的数组，那么，就无法开辟一个对应的空间使其一一对应的存储。此时，我们需要新建一个带有存储范围的空间，来存储一定范围内的元素
"""


def bucket_sort(arr, max_num):
    """
    换一种写法展示其稳定性
    """
    buf = {i: [] for i in range(int(max_num)+1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(arr)
    for i in range(arr_len):
        num = arr[i]
        buf[int(num)].append(num)  # 将相应范围内的数据加入到[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))  # 这里还需要对一个范围内的数据进行排序，然后再进行输出
    return arr


if __name__ == "__main__":
    lis = [3.1, 4.2, 3.3, 3.5, 2.2, 2.7, 2.9, 2.1, 1.55, 4.456, 6.12, 5.2, 5.33, 6.0, 2.12]
    print(bucket_sort(lis, max(lis)))