### 动态规划

动态规划和分治法相似，都是将大事化小，通过其子问题求出原问题，是一种解决问题的思想。



> 动态规划先解决子问题，再逐步解决大问题。
>
> 对于背包问题，你先解决小背包（子背包）问题，再逐步解决原来的问题。



- **当每个子问题都是离散的，即不依赖于其他子问题时，动态规划才管用**。 





### 背包问题

假设你是个小偷，背着一个可装4磅东西的背包，如何装实现价值最大化呢？

 

商品有：
音响（3000美元）—— 4磅
笔记本电脑（2000美元）—— 3磅
吉他（1500美元）—— 1磅
iphone（2000美元）—— 1磅



每个动态规划算法都从一个网格开始 ，网格的各行为商品，各列为不同容量（1～4磅）的背包，开始填充网格。



### 绘制网格

- 单元格中的值是什么？
- 如何将这个问题划分为子问题？
- 网格的坐标轴是什么？



书中用了如下公式计算单元格的值：

```
cell[i][j] = max(cell[i - 1][j], 当前商品价值 + cell[i - 1][j - 当前商品的重量])
```



![](https://upload-images.jianshu.io/upload_images/5692007-350303fb517cb3ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





![](https://upload-images.jianshu.io/upload_images/5692007-f3cb660619a8c535.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)









启示：

- 动态规划可帮助你在给定约束条件下找到最优解。在背包问题中，你必须在背包容量给定的情况下，偷到价值最高的商品。
- 在问题可分解为彼此独立且离散的子问题时，就可使用动态规划来解决。



### 最长公共子串



![](https://upload-images.jianshu.io/upload_images/5692007-7abe797a5dc8aac9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




![](https://upload-images.jianshu.io/upload_images/5692007-0b7913c23d8273ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




对于最长公共子串问题，答案为网格中最大的数字——它可能并不位于最后的单元格中。 





### 最长公共子序列

![](https://upload-images.jianshu.io/upload_images/5692007-f0c6041bd0de53f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






![](https://upload-images.jianshu.io/upload_images/5692007-56b924d45661fa2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




二者对比

![](https://upload-images.jianshu.io/upload_images/5692007-714baa60a782e124.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






动态规划问题可以从以下角度考虑：

1. 状态
2. 状态间的转移方程
3. 状态的初始化
4. 返回结果

### 练习
请绘制并填充用来计算blue和clues最长公共子串的网格。

|      |  C   |  L   |  U   |  E   |  S   |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  B   |  0   |  0   |  0   |  0   |  0   |
|  L   |  0   |  1   |  0   |  0   |  0   |
|  U   |  0   |  0   |  2   |  0   |  0   |
|  E   |  0   |  0   |  0   |  3   |  0   |


### 思考
- 分治法和动态规划的区别


推荐小灰写的一篇文章
[漫画：什么是动态规划](https://juejin.im/post/5a29d52cf265da43333e4da7)

### 小结

- 需要在给定约束条件下优化某种指标时，动态规划很有用。
- 问题可分解为离散子问题时，可使用动态规划来解决。
- 每种动态规划解决方案都涉及网格。
- 单元格中的值通常就是你要优化的值。
- 每个单元格都是一个子问题，因此你需要考虑如何将问题分解为子问题。
- 没有放之四海皆准的计算动态规划解决方案的公式。