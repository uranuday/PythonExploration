## 《算法图解》读书笔记 Chapter6

### 1. 图

   图由**节点**（node）和**边**（edge）组成，一个节点可能与众多节点直接相连，这些节点被称为**邻居**。 图用于模拟不同的东西是如何相连的。 

   ![Snipaste_2018-06-03_11-00-13.png](https://upload-images.jianshu.io/upload_images/5692007-584db43231de04a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


   有向图：关系单项，带有箭头。

   无向图：关系双向，不带箭头。

   例如，这两个图是等价的：

   ![Snipaste_2018-06-03_11-33-26.png](https://upload-images.jianshu.io/upload_images/5692007-ac2d0aa948fc4f42.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




### 2. 广度优先搜索（breadth-first search，BFS）

   广度优先搜索让你能够找出两样东西之间的最短距离 ，是一种用于图的查找算法，可解决两类问题：

   - **从节点A出发，有前往节点B的路径吗？**
   - **从节点A出发，前往节点B的哪条路径最短？**

   

   ![Snipaste_2018-06-03_10-48-42.png](https://upload-images.jianshu.io/upload_images/5692007-71ff9b4c076b884c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


​    

  ![Snipaste_2018-06-03_10-50-26.png](https://upload-images.jianshu.io/upload_images/5692007-6fedfded2012cecc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




   - 两个步骤：

   (1) 使用图来建立问题模型。

   (2) 使用广度优先搜索解决问题。

   

### 3. 查找最短路径

   书中给出了一个查找芒果经销商的例子，先在一度关系中搜索，确定其中没有芒果销售商后，才在二度关系中搜索。 

   在这有一个可实现这种目的的数据结构，那就是**队列**。

   一度关系：跟本节点直接相连的节点。

   例如，朋友是一度关系，朋友的朋友是二度关系。 

   ![Snipaste_2018-06-03_11-17-30.png](https://upload-images.jianshu.io/upload_images/5692007-b62e890f06b1fbc8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




   队列（queue）：

   队列只支持两种操作：**入队**和**出队**。 

   队列是一种**先进先出**（First In First Out，FIFO）的数据结构，而栈是一种**后进先出**（Last In First Out，LIFO）的数据结构。 

   创建图

   使用散列表的方式，找到 “你→朋友” 这样的映射关系

   ```
   graph = {}
   graph["you"] = ["alice", "bob", "claire"]
   graph["bob"] = ["anuj", "peggy"]
   graph["alice"] = ["peggy"]
   graph["claire"] = ["thom", "jonny"]
   graph["anuj"] = []
   graph["peggy"] = []
   graph["thom"] = []
   graph["jonny"] = []
   ```

   

### 4. 实现

      1. 找出关系网，创建图
      2. 创建一个队列，用于存储要查的人
      3. 从队列中弹出一个人
      4. 检查这个人是否是芒果销售商
      5. 若是，则退出；若不是，则将这个人所有邻居都加入队列，回到 3 步
      6. 若列表为空，则退出

   ```
   def search(name):
       search_queue = deque()
       # 将你的邻居都加入到这个搜索队列中
       search_queue += graph[name]
       # 用于记录检查过的人
       searched = []
       # 只要队列不为空
       while search_queue:
           # 就取出其中的第一个人
           person = search_queue.popleft()
           # 仅当这个人没检查过时才检查
           if person not in searched:
               if person_is_seller(person):
                   print(person + " is a mango seller!")
                   return True
               else:
                   search_queue += graph[person]
                   # 将这个人标记为检查过
                   searched.append(person)
       return False
   
   
   search("you")
   
   ```

   

### 5. 运行时间

   广度优先搜索的运行时间为*O*(人数 + 边数)，这通常写作*O*(*V* + *E*)，其中*V* 为顶点（vertice）数，*E* 为边数。 

### 6. 小结

   - 广度优先搜索指出是否有从A到B的路径。
   - 如果有，广度优先搜索将找出最短路径。
   - 面临类似于寻找最短路径的问题时，可尝试使用图来建立模型，再使用广度优先搜索来解决问题。
   - 有向图中的边为箭头，箭头的方向指定了关系的方向，例如，rama→adit表示rama欠adit钱。
   - 无向图中的边不带箭头，其中的关系是双向的，例如，ross - rachel表示“ross与rachel约会，而rachel也与ross约会”。
   - 队列是先进先出（FIFO）的。
   - 栈是后进先出（LIFO）的。
   - 你需要按加入顺序检查搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必须是队列。
   - 对于检查过的人，务必不要再去检查，否则可能导致无限循环。

   