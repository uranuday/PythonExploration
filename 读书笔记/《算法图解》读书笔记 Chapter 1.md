# 《算法图解》读书笔记 Chapter1

![image.png](https://upload-images.jianshu.io/upload_images/5692007-a77f87d59425b877.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> - 二分查找
> - 大 O 表示法
> - 练习
> - 小结

据说这是一本像小说一样有趣的算法入门书，我也来读哈，顺便做下记录。
知乎上有这样一个问题：
![问题](https://upload-images.jianshu.io/upload_images/5692007-2e21c99dbc8b6e9d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
回答还是比较精彩的，其中有一回答为**二分找肉法**，咱们来看哈：

![二分找肉](https://upload-images.jianshu.io/upload_images/5692007-32bf7c4c9ee12409.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
那么二分法在生活中有哪些应用？突然想起了求方程的近似值，修电路？水管？猜数字游戏？。。。

好了，好了，第一章笔记走起！
- 先来一个简单查找，从列表中逐个比较：

```
def search(target_list,item):
    for i in target_list:
        if i == item:
            return i
    return None
```


### 1. 二分查找（Binary Search)
也称折半查找、对数查找 ，在线性数组中找特定值的算法，每个步骤去掉一半不符合的数据。注意是【有序数组】哈。
![步骤](https://upload-images.jianshu.io/upload_images/5692007-d7cd20a26d56b307.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
数组元素不相同情况下：

```
def binary_search(list, item):  
    # low 和 high 表示列表中查找的范围.  
    low = 0  
    high = len(list) - 1  
    # 只要范围没有缩小到只包含一个元素，就检查中间的元素
    while low <= high:
        # low + high 若为奇数，则向下取整  
        mid = (low + high) // 2  
        guess = list[mid]  
        # 若查找到指定项，则返回下标.  
        if item == guess:  
            return mid  
        # 当前数值过大时，降低上限值.  
        elif guess > item:  
            high = mid - 1  
        # 当前数值过小时，提高下限值.  
        else:  
            low = mid + 1  
    # 查找项不存在返回None  
    return None  
```

思考：

> 用递归如何实现
> 用二分查找法找边界值
> 用二分查找法找区域



### 2. 大 O 表示法

注：`log` 指的都是 `以2为底的log`. 

`大O表示法`是一种特殊的表示法，指出了算法的速度有多快，通常情况下`大O表示法`指的是最糟情况下的运行时间。**大O表示法让你能够比较操作数，它指出了算法运行时间的增速**。 

常见的大O运行时间：



| 大 O 运行时间 | 算法名称                         |
| :------------ | :------------------------------- |
| O(logn)       | 如二分查找，（对数时间）         |
| O(n)          | 如简单查找，（线性时间）         |
| O(n*logn)     | 如快速排序，速度较快的排序算法   |
| O(n^2)        | 如选择排序，速度较慢的排序算法， |
| O(n!)         | 动态规划，如旅行商问题解决方案   |



**线性时间**

要猜测的次数与列表长度相同的, 则称为线性时间

**对数时间**

二分查找的运行时间就是对数时间



![image.png](https://upload-images.jianshu.io/upload_images/5692007-afd945e6a2787c58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




注：


- 它指出的是最差情况下的运行时间
- 算法的运行时间以不同的速度增加
- 算法的速度并非指的时间，而是操作数的增速；
- 算法速度，随着输入的增加, 其运行时间将以什么样的速度增加；


### 3.练习
- 使用大O表示法给出下述各种情形的运行时间。



![练习](https://upload-images.jianshu.io/upload_images/5692007-ddb98054ae773006.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


 1.3：根据字母姓氏进行二分查找，O(log n)。
 1.4：简单查找，O(n)。
 1.5：属于简单查找，O(n)。
 1.6：O(n)。

- 如有一个连续相同数的列表，怎么用二分解决：列表 [1,2,2,2,3]，要找出数组中第一次出现元素 2 所在的位置，（这里是第1个值）该怎么处理？

一位群友的解法：
_**思路:找到相等的数后，判断 `index - 1` 的数是否是要找的数，如果是，则继续二分。**_(注：处理全为同一个数时，找到下标为 0 的数时，`index - 1`报错的情况）
```
def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (int)((low+high)/2)
        guess = list[mid]
        if guess == item:
            if mid == 0:
                return mid
            if list[mid - 1] == item:
                high = mid -1
            else:
                return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None
```

### 4. 小结

>- 二分查找的速度比简单查找要快许多，数据越大，差距就越明显。
>- O(log n)比O(n)快。需要搜索的元素越多，前者比后者就快得越多。
>- 算法运行时间并不以秒为单位。
>- 算法运行时间是从其增速的角度来度量的。
>- 算法运行时间用大O表示法表示。
