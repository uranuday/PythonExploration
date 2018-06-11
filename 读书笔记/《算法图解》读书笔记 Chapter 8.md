## 《算法图解》 读书笔记 Chapter8

### 贪婪算法

> 识别 NP 完全问题
>
> 学习近似算法，快速找到 NP 完全问题的近似解
>
> 学习贪婪策略

### 1.  教室调度问题

    *   选出最早结束的课
    
    *   选出上一堂课结束才开始的课
    
    贪婪算法的优点——简单易行，**每步都选择局部最优解**，最终得到的就是全局最优解。

**练习**

![](https://upload-images.jianshu.io/upload_images/5692007-2addb1d538615cd8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


*   选择可装入卡车剩余空间内的最大箱子，并重复这个过程，直到不能再装入箱子为止。不能得到最优解。

*   不断地挑选可在余下的时间内完成的价值最大的活动，直到余下的时间不够完成任何 活动为止。不能得到最优解。

### 2.  集合

    集合类似于列表，只是不能包含重复的元素。
    
    运算：并集，交集，差集。

### 3.  集合覆盖问题

    *   近似算法
    
        判断近似算法优劣的标准如下：
    
        *   速度有多快；
    
        *   得到的近似解与最优解的接近程度。

​ ​ 在本章中，给出了这样一个例子:

> 假设你办了个广播节目，要让全美50个州的听众都收听得到。为此，你需要决定在哪些广播台播出。在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。

给出解决方案：

(1) 选出这样一个广播台，即它覆盖了最多的未覆盖州。

(2) 重复第一步，直到覆盖了所有的州。

在这个例子中，贪婪算法的运行时间为*O*(*n*^2)，其中*n*为广播台数量。

```
# 创建一个集合，包含要覆盖的州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 可供选择的广播台清单，散列表来表示
# 键为广播台的名称，值为广播台覆盖的州
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 用一个集合来存储最终选择的广播台
final_stations = set()

# 不断地循环，直到states_needed为空
while states_needed:
    # 从中选择覆盖了最多的未覆盖州的广播台，
    # 将这个广播台存储在 best_station中。
    best_station = None
    # 包含该广播台覆盖的所有未覆盖的州
    states_covered = set()
    for station, states in stations.items():
        # 计算交集,它包含当前广播台覆盖的一系列还未覆盖的州
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    # 还需更新states_needed。由于该广播台覆盖了一些州，因此不用再覆盖这些州
    states_needed -= states_covered
    # for循环结束后将best_station添加到最终的广播台列表中。
    final_stations.add(best_station)

print(final_stations)
```

### 4.  NP 完全问题

    *   旅行商问题和集合覆盖问题有一些共同之处：你需要计算所有的解，并从中选出最小/最短的那个。这两个问题都属于NP完全问题。
    
    *   元素较少时算法的运行速度非常快，但随着元素数量的增加，速度会变得非常慢。
    
    *   涉及“所有组合”的问题通常是NP完全问题。
    
    *   不能将问题分成小问题，必须考虑各种可能的情况。这可能是NP完全问题。
    
    *   如果问题涉及序列（如旅行商问题中的城市序列）且难以解决，它可能就是NP完全问题。
    
    *   如果问题涉及集合（如广播台集合）且难以解决，它可能就是NP完全问题。
    
    *   如果问题可转换为集合覆盖问题或旅行商问题，那它肯定是NP完全问题。

### 5.  小结

    - 贪婪算法寻找局部最优解，企图以这种方式获得全局最优解。
    
    - 对于NP完全问题，还没有找到快速解决方案。
    
    - 面临NP完全问题时，最佳的做法是使用近似算法。
    
    - 贪婪算法易于实现、运行速度快，是不错的近似算法。