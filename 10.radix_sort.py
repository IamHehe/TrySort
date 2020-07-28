# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/28 19:09

"""
程序说明：
    基数排序
    参考：https://www.cnblogs.com/sfencs-hcy/p/10616446.html
    - 基数排序：根据键值的每位数字来分配桶
    - 计数排序：每个桶只存储单一键值；
    - 桶排序：每个桶存储一定范围的数值；
    时间复杂度：O(n*k)
    空间复杂度: O(n+k) k是最大值的位数
"""


def radix_sort(s):
    i = 0  # 记录当前正在排的位数，个位为0
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 最大值的位数
    while i < j:
        bucket_list = [[] for _ in range(10)]  # 初始化桶数组
        for x in s:
            bucket_list[int(x / (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
        # print(bucket_list)
        s.clear()  # 清空列表s，空间复杂度O(1)
        [s.extend(x) for x in bucket_list]  # 列表表达式替换
        i += 1


if __name__ == '__main__':
    lis = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(lis)
    print(lis)
