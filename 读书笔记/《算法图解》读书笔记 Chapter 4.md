## 《算法图解》读书笔记 Chapter4


- 分而治之
- 快速排序
- 归并排序
- 练习一下
- 小结



### 1. 分而治之

**D&C 解决问题的过程步骤**

（1）找出简单的基线条件

（2）不断将问题分解（或者说缩小规模 ），直到符合基线条件



- 给定一个数字数组，将这些数字相加，并返回结果，用循环完成：

```
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
```



用递归函数来完成：

（1）基线条件：数组不包含任何元素或只包一个元素

（2）缩小规模：计算除第一个数字外的其它数字总和，将其与第一个数字相加



```
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
```



- 编写一个递归函数来计算列表包含的元素个数。

```
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

```

> 
>
> 提示：编写涉及数组的递归函数时，基线条件通常是数组为空或只包含一个元素 



### 2. 快速排序

![来源网络](https://upload-images.jianshu.io/upload_images/5692007-4a02e8a501f464f8.gif?imageMogr2/auto-orient/strip)

快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），采用分治思想的一种排序算法，在平均状况下，排序n个项目要Ο(n log n)次比较。在最坏状况下则需要Ο(n^2)次比较。

工作原理：

1. 首先，从数组中选择一个元素作为**基准值**（pivot）。 
2. 找出比基准值小的元素以及比基准值大的元素。 —**分区**（partitioning）
3. 递归调用切分过程

- 用快速排序对数组排序

```
def quicksort(array):
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    if len(array) < 2:
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
```

- 还可用两个索引分别向右向左进行分区
(这是实验楼上有关快速排序的代码)：

```
def qsort(alist, lower, upper):
    print(alist)
    if lower >= upper:
        return

    pivot = alist[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        # swap while left <= right
        alist[left], alist[right] = alist[right], alist[left]
    # swap the smaller with pivot
    alist[lower], alist[right] = alist[right], alist[lower]

    qsort(alist, lower, right - 1)
    qsort(alist, right + 1, upper)

unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
print(qsort(unsortedArray, 0, len(unsortedArray) - 1))
```



### 3. 归并排序
将两个有序数组归并成一个更大的有序数组。
（同样是实验楼上相关代码）

```
class Sort:
    def mergeSort(self, alist):
        if len(alist) <= 1:
            return alist

        mid = len(alist) // 2
        left = self.mergeSort(alist[:mid])
   
        right = self.mergeSort(alist[mid:])
      
        return self.mergeSortedArray(left, right)

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray

unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort = Sort()
print(merge_sort.mergeSort(unsortedArray))
```

### 4. 练习一下
- 给定一个整数数组 nums，找到一个具有最大和的连续字数组（字数组最少包含一个元素），返回其最大和。

```
#当前最大值cursum,循环每个元素时的最大值maxsum.
def maxsubarray(nums):
    if not nums:
        return 0
    cursum = maxsum = nums[0]
    for num in nums[1:]:
        cursum = max(num, cursum + num)
        maxsum = max(maxsum, cursum)
    return maxsum
print(maxsubarray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```

### 5. 小结

- 分而治之是一种解决问题的思路。
- D&C将问题逐步分解。使用D&C处理列表时，基线条件很可能是空数组或只包含一个元素的数组。
- 实现快速排序时，请随机地选择用作基准值的元素。快速排序的平均运行时间为*O*(*n* log *n*)，最糟情况下是 O(n^2)。
- 大O表示法中的常量有时候事关重大，这就是快速排序比合并排序快的原因所在。
- 比较简单查找和二分查找时，常量几乎无关紧要，因为列表很长时，*O*(log *n*)的速度比*O*(*n*)快得多。

