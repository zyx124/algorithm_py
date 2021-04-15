When using Breadth First Search, **queue** is used to track the nodes. BFS is a method to traverse a graph layer by layer. 



Topological Sorting: 

For each directed edge A -> B, A must be before B in the order list. The first node in the order can be any node in the graph with no nodes direct to it.

```python
from collections import deque

class Solution:
    
    def topSort(self, graph):
        result = []
        node_in_degree = self.find_start(grpah)
        start = [k for k, v in node_in_degree.items() if v == 0]
        
        queue = deque(start)
        while queue:
            node = queue.popleft()
            result.append(node)
            for n in node.neighbours:
                node_in_degree[n] -= 1
                if node_in_degree[n] == 0:
                    queue.append(n)
         return result
    
    def find_start(self, graph):
        node_in_degree = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_in_degree[neighbor] += 1
        return node_in_degree
```

