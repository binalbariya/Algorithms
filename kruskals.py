V=5
infinity=99999
# G = [[0, 9, 75, 0, 0],
#      [9, 0, 95, 19, 42],
#      [75, 95, 0, 51, 66],
#      [0, 19, 51, 0, 31],
#      [0, 42, 66, 31, 0]]

G = [[0, 1, 7, 0, 0],
     [1, 0, 5, 4, 3],
     [7, 5, 0, 0, 6],
     [0, 4, 0, 0, 2],
     [0, 3, 6, 2, 0]]
# graph = {0: set([1,2]),
#          1: set([0,2,3,4]),
#          2: set([0,1,4]),
#          3: set([1,4]),
#          4: set([1,2,3])}
#

# class AdjNode:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
#
# class Graph:
#     def __init__(self, num):
#         self.V = num
#         self.graph = [None] * self.V
#         self.head=None
#
#     # Add edge
#     def add_edge(self, s, d):
#         node = AdjNode(d)
#         node.next = self.graph[s]
#         self.graph[s] = node
#
#
#         node = AdjNode(s)
#         node.next = self.graph[d]
#         self.graph[d] = node
#         self.head = node
#
#     def remove_edge(self,i,j):
#         nextt = self.graph[j].next
#
#         self.graph[i].next=nextt
#         nextt2 = self.graph[i].next
#         self.graph[j].next = nextt2
#
#         print("HALAAAAAAAAAAA BOLLLLL")
#         self.print_agraph()
#
#
#
#     def print_agraph(self):
#         for i in range(self.V):
#             print("Vertex " + str(i) + ":", end="")
#             temp = self.graph[i]
#             while temp:
#                 print(" -> {}".format(temp.data), end="")
#                 temp = temp.next
#             print(" \n")
#
#     # def detectCycle(self,head,i,j):
#     #     self.add_edge(i,j)
#     #     slow_p = head
#     #     fast_p = head
#     #     while (slow_p and fast_p and fast_p.next):
#     #         slow_p = slow_p.next
#     #         fast_p = fast_p.next.next
#     #         if slow_p == fast_p:
#     #             self.remove_edge(i,j)
#     #             return True
#     #         self.remove_edge(i,j)
#     #         return False
#
#     def isCyclicUtil(self, v, visited, recStack):
#
#         # Mark current node as visited and
#         # adds to recursion stack
#         visited[v] = True
#         recStack[v] = True
#
#         # Recur for all neighbours
#         # if any neighbour is visited and in
#         # recStack then graph is cyclic
#         for neighbour in self.graph[v]:
#             if visited[neighbour] == False:
#                 if self.isCyclicUtil(neighbour, visited, recStack) == True:
#                     return True
#             elif recStack[neighbour] == True:
#                 return True
#
#
#     def isCyclic(self):
#         visited = [False] * self.V
#         recStack = [False] * self.V
#         for node in range(self.V):
#             if visited[node] == False:
#                 if self.isCyclicUtil(node, visited, recStack) == True:
#                     return True
#         return False


from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)

    def removeEdge(self,u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def isCyclicUtil(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False
    # Returns true if graph is cyclic else false
    def isCyclic(self,x,y):
        self.addEdge(x,y)

        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if visited[i] == False:  # Don't recur for u if it is already visited
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    self.removeEdge(x,y)
                    return True
        self.removeEdge(x,y)
        return False

graph = Graph(V)

selected = [0,0,0,0,0]
number_of_edges = 0
selected[0]=True
total_cost = 0
temp=0
dictt={0:[None],1:[None],2:[None],3:[None],4:[None]}
while (number_of_edges<V-1):
    minimum = infinity
    x=0
    y=0

    for i in range(V):

            for j in range(V):

                if (G[i][j]):
                    if minimum>G[i][j]:
                        minimum = G[i][j]
                        x=i
                        y=j
    if graph.isCyclic(x,y)==False:
        print(str(x)+"-->"+str(y)+":     "+str(G[x][y]))
        graph.addEdge(x,y)

        print("**************************************")
        print("**************************************")
        total_cost +=G[x][y]
        #G[x][y] = 0

        # if dictt[x] is [None]:
        #     dictt[x]=y
        # else:
        #     dictt[x].append(y)
        # selected[y]=True
        number_of_edges +=1
    else:
        G[x][y] = 0
        continue

print("Total cosst using kruskals algo is: "+str(total_cost))