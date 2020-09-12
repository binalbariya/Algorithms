def bfs(graph,source):
    queue = []
    visited=[]
    augmented_path=[source]
    total_cost=0
    for x in range(0,5):
        visited.append(0)
    queue.append(source)
    visited[source]=True
    while len(queue)!=0:
        u = queue.pop(0)
        for v in range(0,5):
            if visited[v]==False and graph[u][v]>0:
                queue.append(v)
                visited[v]=True
                total_cost+=graph[u][v]
                augmented_path.append(v)

    print("BFS:",augmented_path)
    return total_cost






graph = [[0, 1, 7, 0, 0],
         [1, 0, 5, 4, 3],
         [7, 5, 0, 0, 6],
         [0, 4, 0, 0, 2],
         [0, 3, 6, 2, 0]]
source=0
total_cost = bfs(graph,source)
print("Total cost: ",total_cost)
