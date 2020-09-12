def dfs(graph,start):
    visited = []
    stack=[]
    augmented_path=[start]
    total_cost=0
    for i in range(0,5):
        visited.append(0)
    stack=[0]
    visited[0]=True
    node = stack.pop(len(stack)-1)
    print("Node encountered:",node)
    while True:
        for v in range(0,5):
            if visited[v]==False and graph[node][v]>0:
                augmented_path.append(v)
                total_cost += graph[node][v]

                visited[v]=True
                stack.append(v)
        if len(stack)==0:
            break
        else:
            node = stack.pop(len(stack)-1)
            print("Node encountered:",node)
    return total_cost





graph =[[0, 1, 7, 0, 0],
     [1, 0, 5, 4, 3],
     [7, 5, 0, 0, 6],
     [0, 4, 0, 0, 2],
     [0, 3, 6, 2, 0]]
start = 0
total_cost = dfs(graph,0)
print("Total cost",total_cost)
