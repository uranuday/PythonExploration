## 《算法图解》读书笔记 Chapter2



今天在百度文库看到了一个有关选择排序的文章，觉得挺有意思，于是就截了半个图：
![image.png](https://upload-images.jianshu.io/upload_images/5692007-5ec4d74d7c570545.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

不得不说，生活中的算法真是无处不在啊，第二章笔记来记录下

>- 数组
>- 链表
>- 排序算法—选择排序
>- 练习
>- 小结



### 1. 内存工作原理

存数据—请求存储空间—分配存储地址

存储数据的两种基本方式—数组&&链表



### 2.数组和链表

|      | 数组                             | 链表                                                         |
| ---- | -------------------------------- | ------------------------------------------------------------ |
| 特点 | 待办事项在内存中相连  （栈中）   | 元素可存储在内存中任何地方，每个元素都存储了下一个元素的地址（堆中） |
| 优点 | 随机读取元素时，效率高           | 顺序访问时，效率高                                           |
| 缺点 | 添加新元素慢，不能动态的分配内存 | 跳跃读取时，效率低                                           |

>数组的元素都是连在一起的，就像一节节的车厢 。
>如果是坐座位，可以把数组和链表看作是：一起坐和分开坐的区别 。 



- 常见数组和链表操作的运行时间：

|      | 数组 | 链表 |
| ---- | ---- | ---- |
| 读取 | O(1) | O(n) |
| 插入 | O(n) | O(1) |
| 删除 | O(n) | O(1) |



### 3. 选择排序

> **选择排序**（Selection sort）是一种简单直观的[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。 

```
# 找出数组中的最小元素
def findSmallest(arr):
  # 存储最小的值
  smallest = arr[0]
  # 存储最小元素的索引
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# 排序算法
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # 找出数组中最小的元素，并将其加入到新的数组中
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr
```

**思考**:
> - 二元选择排序
> - 等值情况

### 4. 练习
- 给出一个整数数组和一个目标值(target)，假设数组有且仅有两个数相加等于目标值，找到这两个数，并返回他们的索引下标。
```
def find_index(arr, target):
    dic = {}
    for i, n in enumerate(arr):
        dic[n] = i
    for i, n in enumerate(arr):
        if target - n in dic and dic[target - n] != i:
            return [i, dic[target - n]]
    return "not find"

if __name__ == '__main__':
    # 测试数组
    test_arr = [7,0,6,12,20,30,40]
    # 测试
    print(find_index(test_arr,7))
    print(find_index(test_arr,13))
    print(find_index(test_arr,32))
    print(find_index(test_arr,100))
```

### 5. 小结

- 计算机内存犹如一大堆抽屉。
- 需要存储多个元素时，可使用数组或链表。
- 数组的元素都在一起。
- 链表的元素是分开的，其中每个元素都存储了下一个元素的地址。
- 数组的读取速度很快。
- 链表的插入和删除速度很快。
- 在同一个数组中，所有元素的类型都必须相同（都为int、double等）。