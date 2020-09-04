graph = {
    'a':{'b':3,'c':4,'d':7},
    'b':{'c':1,'f':5},
    'c':{'f':6,'d':2},
    'd':{'e':3,'g':6},
    'e':{'g':3,'h':4},
    'f':{'e':1,"h":8},
    'g':{'h':2},
    'h':{'g':2}
}

def djikstra(graph,start,goal):
    shortest_distance ={}
    track_precedance={}
    unSeenNodes = graph
    infinity=99999
    track_path=[]

    for node in unSeenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start]=0

    while unSeenNodes:
        min_distance_node = None
        for node in unSeenNodes:
             if min_distance_node is None:
                 min_distance_node =node
             elif shortest_distance[node]<shortest_distance[min_distance_node]:
                 min_distance_node = node
        path_options = graph[min_distance_node].items()
        for child_node,weight in path_options:
            if weight + shortest_distance[min_distance_node]<shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_precedance[child_node] = min_distance_node
        unSeenNodes.pop(min_distance_node)

    currentNode = goal
    while currentNode!=start:
        try:
            track_path.insert(0,currentNode)
            currentNode = track_precedance[currentNode]
        except:
            print("Path is not reachable")
            break
    track_path.insert(0,start)

    if shortest_distance[goal]!=infinity:
        print("Shortest Distance is "+str(shortest_distance[goal]))
        print("And the optimal path is "+str(track_path))

djikstra(graph,'a','h')