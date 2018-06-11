- 今天突然想起了一个笑话，话说把大象放进冰箱要几步呢？。。。。
  ...
  ......
  不，不，不！

  我当然不是来讲笑话的，其实我是来讲故事的！

  这是一个源自古印度的神话故事：
  梵天神告诉侍奉他的婆罗门，只要能实现以下目标，世界就会在一个闪电中毁灭，咱们一起来看下吧！![汉诺塔](https://upload-images.jianshu.io/upload_images/5692007-ff58aa1c0fdf261b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  怎么样，想到解决办法了嘛，没想到也没关系，毕竟咱保卫了全世界不是吗！
  下面来解决一下这个问题：

  ![汉诺塔游戏](https://upload-images.jianshu.io/upload_images/5692007-0d407a30c5cbd88a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  其实这是一个可用递归算法解决的问题，
  可将问题分解：
  >第一步：将A柱上的n-1个盘移到B上;
  >第二步：将A上的第n号盘移到C;
  >第三步：将B上的n-1 个盘子移到C上去;

  那么具体怎么用程序解决呢，就涉及到今天的笔记内容了，开始**总结笔记了！**

  >- 递归
  >- 基线条件和递归条件
  >- 栈
  >- 调用栈和递归调用栈
  >- 斐波那契数列和汉诺塔
  >- 小结

  

  > **如果使用循环，程序的性能可能更高；如果使用递归，程序可能更容易理解。如何选择要看什么对你来说更重要。** 

  

  ### 1. 递归

  **每个递归函数都有两部分：基线条件**（base case）**和递归条件**（recursive case）。 

  - **递归条件**指的是函数调用自己。
  - **基线条件**则指的是函数不再调用自己，从而避免形成无限循环,避免产生栈溢出。 

  ```
  def countdown(i):
      print(i)
      # 基线条件
      if i < 1:
          return
      else:
          # 递归条件
          countdown(i-1)
  ```

  

  ### 2. 栈

  >**栈**（stack）又称为**栈**或**堆叠**，是计算机科学中一种特殊的串列形式的抽象资料型别，其特殊之处在于只能允许在连结串列或阵列的一端（top）进行加入数据（push）和输出数据（pop）的运算。另外栈也可以用一维数组或连结串列的形式来完成。

  ![栈](https://upload-images.jianshu.io/upload_images/5692007-bf841c9f28688c90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  - 编程实现：
  ```
  stack = []
  len(stack) # size of stack
  
  # more efficient stack
  import collections
  stack = collections.deque()
  ```
  len(stack) != 0 — 判断stack是否为空
  stack[-1] — 取栈顶元素，不移除
  pop() — 移除栈顶元素并返回该元素
  append(item) — 向栈顶添加元素

  **内建数据类型list实现栈的数据结构：**
  ```
  class Stack:
      def __init__(self):
          # 造一个容器
          self.items = []
  
      # 压栈
      def push(self, item):
          self.items.append(item)
  
      # 出栈
      def pop(self):
          return self.items.pop()
  
      # 清空栈
      def clear(self):
          del self.items[:]
  
      # 当前栈的大小(元素个数)
      def size(self):
          return len(self.items)
  
      # 栈是否为空
      def empty(self):
          return self.size() == 0
  
      # 栈顶元素
      def top(self):
          return self.items[self.size()-1]
  ```

  - 调用栈(call stack)

  


  计算机在内部使用被称为调用栈的栈。 

  **调用另一个函数时，当前函数暂停并处于未完成状态**。 

  - 递归调用栈

  ```
  def fact(x):
    if x == 1:
      return 1
    else:
      return x * fact(x-1)
  ```

  

  > 代价：存储详尽的信息可能占用大量的内存。每个函数调用都要占用一定的内存，如果栈很高，就意味着计算机存储了大量函数调用的信息。在这种情况下，你有两种选择。

  - 重新编写代码，转而使用循环。
  - 使用**尾递归**。另外，并非所有的语言都支持尾递归。
    **思考：尾递归的优化**


  ### 3. 斐波那契数列和汉诺塔
  - 斐波那契数列
  ```
  def fib(n):
      if n<2:
          return n
      else:
          return fib(n-1)+fib(n-2)
  
  for i in range(10):
      print(fib(i),end = ' ')
  ```
  `>>> 0 1 1 2 3 5 8 13 21 34 `

  **思考：用递推法和矩阵法实现斐波那契数列**

  - 汉诺塔游戏
  ```
  i = 1
  def move(n, mfrom, mto) :
    global i
    print ("第{}步:将{}号盘子从{} -> {}".format(i, n, mfrom, mto))
    i += 1
  
  def hanoi(n, A, B, C) :
    if n == 1 :
      move(1, A, C)
    else :
      hanoi(n - 1, A, C, B)
      move(n, A, C)
      hanoi(n - 1, B, A, C)
  
  
  if __name__ =="__main__":
      n = int(input("please input a integer :"))
      hanoi(n, 'A', 'B', 'C')
  ```

  ```
  please input a integer :3
  第1步:将1号盘子从A -> C
  第2步:将2号盘子从A -> B
  第3步:将1号盘子从C -> B
  第4步:将3号盘子从A -> C
  第5步:将1号盘子从B -> A
  第6步:将2号盘子从B -> C
  第7步:将1号盘子从A -> C
  ```
  ### 4. 小结

  - 递归指的是调用自己的函数。
  - 每个递归函数都有两个条件：基线条件和递归条件。
  - 栈有两种操作：压入和弹出。
  - 所有函数调用都进入调用栈。
  - 调用栈可能很长，这将占用大量的内存。