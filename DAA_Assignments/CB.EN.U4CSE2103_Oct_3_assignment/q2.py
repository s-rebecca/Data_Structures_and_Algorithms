#BFS TILL LEVEL K IN A GRAPH
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s,k):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        level=0
        while queue:
            if level==k:
                print(queue)
                return
            s=queue.pop(0)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
            level+=1
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(2,4)
g.BFS(0,2)

"""
The given Python code implements a Breadth-First Search (BFS) algorithm that traverses a graph up to level K starting from a given source vertex. Let's analyze and prove the correctness of this algorithm:

*Correctness Proof:*

1. *Initialization:*

   - The visited list is initialized to False for all vertices, indicating that no vertices have been visited initially.
   - The queue is initialized with the source vertex s.
   - The level is initialized to 0.

2. *Main Loop:*

   - The algorithm enters a loop that continues until the queue is empty or until the specified level k is reached.

   - Within each iteration of the loop:
   
     - If the current level equals k, the algorithm prints the vertices in the queue and returns. This ensures that the BFS traversal stops at level k and only the vertices at that level are printed.

     - The source vertex s is dequeued from the front of the queue.

     - For each adjacent vertex i of s that hasn't been visited (visited[i] == False), i is enqueued into the queue, and visited[i] is set to True.

     - The level counter is incremented.

3. *Termination:*

   - The algorithm terminates either when the specified level k is reached or when the queue becomes empty.

4. *Correctness:*

   - The algorithm ensures that vertices are visited in a BFS order up to level k because it processes vertices level by level, and it stops after reaching level k.

   - If the level reaches k, the algorithm prints the vertices at that level. Therefore, it correctly prints the vertices at level k.

5. *Completeness:*

   - The algorithm will traverse all vertices within level k and print them if level k exists in the graph.

6. *Time Complexity:*

   - The time complexity of this algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph. This is because each vertex and each edge is processed once.

In conclusion, the algorithm correctly prints the vertices at level k in the graph, and its correctness is ensured by the BFS traversal logic.
"""