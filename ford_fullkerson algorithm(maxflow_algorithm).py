parent_tracker=[]
infinite=99999

def find_length(queue):
    count = 0
    for i in queue:
        count+=1
    return count
def find_minimum(a,b):
    if a>b:
        return b
    else:
        return a

def bfs(residual_graph,source,sink,parent_tracker):
    queue=[]
    visited=[]

    for x in range(0,N):
        visited = visited+[0]
    queue = queue+[source]
    visited[source]=True
    parent_tracker[source]=-1

    while not find_length(queue)==0:
        u = queue[0]
        queue =queue[1:]
        for v in range(0,N):
            if visited[v]==False and residual_graph[u][v]>0:
                queue = queue+[v]
                visited[v]=True
                parent_tracker[v]=u

    if visited[sink]==True:

        return True
    else:
        return False


def FordFulkersonAlgorithm(graph,source,sink):
    u=0
    v=0
    residual_graph = graph
    max_flow=0

    while bfs(residual_graph,source,sink,parent_tracker):
        augmented_path=[]
        v=sink
        path_flow=infinite
        while v!=source:
            u = parent_tracker[v]
            augmented_path = augmented_path+[v]
            path_flow = find_minimum(path_flow,residual_graph[u][v])
            v = parent_tracker[v]
        augmented_path=augmented_path+[0]
        print("Augmented path--> ",augmented_path[-1::-1],"     Cost--> ",path_flow)

        v=sink
        while v!=source:
            u=parent_tracker[v]
            residual_graph[u][v]-=path_flow
            residual_graph[v][u]+=path_flow
            v = parent_tracker[v]
        max_flow+=path_flow
    return max_flow



print("Input")
N = int(input("Enter number of nodes in graph"))
edges = int(input("Enter no. of edges in graph"))
is_directed = int(input("Is your graph directed"))
graph=[]
graph = [0 for i in range(N) for j in range(N)]
if not is_directed:
    print("Enter edges and their corresponding weights")
    for i in range(N):
        print("Enter edge between V1 and V2 (Read the graph from left to right)")
        v1 = input("enter node V1")
        v2=input("enter node V2")
        weight = input("Enter corresponding weight")
        graph[v1][v2] = graph[v2][v1] = weight
    for i in range(N):
        for j in range(N):
            print(graph[i][j])
        print()
else:
    print("Enter edges and their corresponding weights")
    for i in range(N):

        v1,v2 = map(int,input("Enter edge between V1 and V2 (Read the graph from left to right)").split())

        print(v1)
        print(v2)
        weight = int(input("Enter corresponding weight"))
        graph[v1][v2] = weight

graph=[[0,16,13,0,0,0],
       [0,0,10,12,0,0],
       [0,4,0,0,14,0],
       [0,0,9,0,0,20],
       [0,0,0,7,0,4],
       [0,0,0,0,0,0]]

for i in range(N):
    for j in range(N):
        print(graph[i][j],end='  ')
    print()

print()
print()
print("Output")
for x in range(0,N):
    parent_tracker = parent_tracker+[0]
final_cost = FordFulkersonAlgorithm(graph,0,N-1)
print()
print("*********************************************************")
print("The maximum possible value is {}".format(final_cost))
print("*********************************************************")
