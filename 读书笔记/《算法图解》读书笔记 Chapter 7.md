

### 狄克斯特拉算法

在上一章中用广度优先搜索，找出了段数最少的路径，但如果加上时间，会发现有最快的路径。

如何找出最快的路径呢，可使用另一种算法——**狄克斯特拉算法**（Dijkstra's algorithm）。 

![Snipaste_2018-06-04_08-56-08.png](https://upload-images.jianshu.io/upload_images/5692007-42c76d25c5c113c2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




### 1. 算法步骤

找出加权图中前往X的最短路径。

狄克斯特拉算法的四个步骤：

(1) 找出在最短时间内前往的节点。

(2) 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销。

(3) 重复这个过程，直到对图中的每个节点都这样做了。

(4) 计算最终路径。

### 2. 适用



![Snipaste_2018-06-04_10-08-54.png](https://upload-images.jianshu.io/upload_images/5692007-3bd48b2981eba217.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- 广度优先搜索来查找两点之间的最短路径，那时“最短路径”的意思是段数最少。在狄克斯特拉算法中，给每段都分配了一个数字或权重，因此狄克斯特拉算法找出的是总权重最小的路径。 

- 要计算非加权图中的最短路径，可使用**广度优先搜索**。要计算加权图中的最短路径，可使用**狄克斯特拉算法**。

- 在无向图中，每条边都是一个环。狄克斯特拉算法只适用于**有向无环图**（directed acyclic graph，DAG）。    
- 不能将狄克斯特拉算法用于包含负权边的图。在包含负权边的图中，要找出最短路径，可使用另一种算法——贝尔曼福德算法（Bellman-Ford algorithm）。    



## 3. 实现

```
# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
# 这个while循环在所有节点都被处理过后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果经当前节点前往该邻居更近
        if costs[n] > new_cost:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为处理过
    processed.append(node)
    # 找出接下来要处理的节点，并循环
    node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 遍历所有的节点
    for node in costs:
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            # 就将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
```





