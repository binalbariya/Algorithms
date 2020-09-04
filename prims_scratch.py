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

selected = [0,0,0,0,0]
selected[0] = True
number_of_edges = 0
total_cost = 0

while (number_of_edges<V-1):
    minimum = infinity
    x=0
    y=0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j] and G[i][j]):
                    if minimum>G[i][j]:
                        minimum = G[i][j]
                        x=i
                        y=j
    print(str(x)+"-->"+str(y)+":     "+str(G[x][y]))
    total_cost +=G[x][y]
    selected[y] = True
    number_of_edges +=1
print("Total cosst using prims algo is: "+str(total_cost))