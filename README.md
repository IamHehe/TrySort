# Doing exercise until keyboard die - Sort algorithms party.
1. Introduction
    1. Language: Python 
    2. 数组题很多情况就是结合排序进行的，比如merge sort，quick sort等，所以要学好排序，并且掌握如何分析最好和最坏的情况。
    3. Array questions are combined with sorting in many cases, such as merge sort and quick sort. Therefore, we should 
    learn sorting well and master how to analyze the big O in the best and worst cases.

2. Discussion
    1. 快速排序是冒泡排序的优化。冒泡是从左往右的交换，快排是直接获取中间值pivot进行交换，同时，以pivot为界限划分左右两个部分，
    分别再次放入快排函数中进行递归操作，时间复杂度O(n)降低至o(log n)。
    2. 希尔排序是插入排序的优化。插入排序是一个一个的比较，希尔排序是先按照一定的步长(gap)将数组划分，使用插入排序对同一个gap中
    的数进行操作，然后减小步长(如gap//=2)，重复操作，最后，gap为1，可以看做对整个数组进行插入排序，但是由于这时的列表已经经过前
    面的排序操作，使得数组中小范围内的数大小分布较为均匀，只需要进行小规模交换，因此可以大大减少平均的对比次数。
    3. 堆排序是选择排序的优化。选择排序相当于每次选择一个最大（小）的数放到队尾（头），每次选择最值都是从左到右比较一遍
    堆排序使用堆的思想，每次原地建堆，返回堆顶，即为返回最值，时间复杂度O(n)降低至o(log n)。大顶堆和小顶堆分别对应升序和降序排序。
    4. 归并排序是典型的分治算法，但是相比后续的快速排序这种通过index原地建堆的算法，略显逊色。
    5. 计数排序、桶排序、基数排序三种利用额外空间记录数组的方式，提高了效率，但是耗费了更多的空间。

3. Reference
- 参考链接：https://www.runoob.com/w3cnote/ten-sorting-algorithm.html