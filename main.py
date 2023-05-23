import numpy as np
import math

INF = float('inf')


def Dijkstra(startState, graph):
    valid = [False] * size
    result = [INF] * size
    result[startState] = 0
    for i in range(size):
        minWeight = INF
        minWeightID = -1
        for j in range(size):
            if not valid[j] and result[j] < minWeight:
                minWeight = result[j]
                minWeightID = j
        for k in range(size):
            if result[minWeightID] + graph[minWeightID][k] < result[k]:
                result[k] = result[minWeightID] + graph[minWeightID][k]
        valid[minWeightID] = True
    return result


adjMatrix = np.loadtxt('input.txt')
size = int(math.sqrt(adjMatrix.size))
for i in range(size):
    for j in range(size):
        if adjMatrix[i][j] == 0:
            adjMatrix[i][j] = INF

w = Dijkstra(3, adjMatrix)  # 1-st argument - start state (count from 0)
print(w)  # output array where i-element is distance to i-state of the graph from start point
