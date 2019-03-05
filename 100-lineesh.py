from pprint import pprint as pp
from collections import defaultdict
import random

import sys
import math
from copy import deepcopy


class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    # self.COL = len(gr[0])
    # pp(self.graph)

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    # Delete the object
    def __del__(self):
        self.graph = ""
        return True


class Tree:
    Tree_Num = 0

    def __init__(self, x, y, monkeys, thres):
        self.xaxis = x
        self.yaxis = y
        self.num_monkeys = monkeys
        self.threshold = thres
        Tree.Tree_Num += 1



    def __del__(self):
        return True


def euclidean_distance(x1, y1, x2, y2, ):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    #print("Distance: %f" % distance)
    return distance


if __name__ == '__main__':
    # Get first line and add find out Number of tress and Jumping capacity
    firstline = input()
    N = int(firstline.split()[0])
    C = float(firstline.split()[1])

    # get information about trees and create tree objects with x, y and monkeys, threshold values
    trees = [[0] * 1 for i in range(N)]
    total_monkeys = 0
    for i in range(N):
        tree_lines = input()
        x, y, m, t = tree_lines.split()
        total_monkeys += int(m)
        trees[i] = Tree(int(x), int(y), int(m), int(t))

    # print -1 if more than one weak trees
    count_of_weak_trees = 0
    weak_tree_num = 0
    for i in range(N):
        if trees[i].num_monkeys > trees[i].threshold:
            weak_tree_num = i
            count_of_weak_trees += 1
            if count_of_weak_trees > 1:
                print(-1)
                sys.exit()
    #matrix = [[0] * (N + 1) for i in range(N + 1)]
    matrix_valid = [[0] * (2 * N + 1) for i in range(2 * N + 1)]

    for i in range(N + 1):
        if i == 0:
            matrix_valid[0][i] = 0
        else:
            matrix_valid[0][i] = trees[i - 1].num_monkeys

    for i in range(N + 1):
        if i != 0:
            matrix_valid[i][N + i] = trees[i - 1].threshold

    for i in range(N + 1):

        for j in range(N + 1):

            if j < N and i < N:

                distance = euclidean_distance(trees[i].xaxis, trees[i].yaxis, trees[j].xaxis, trees[j].yaxis)
                if distance <= C:
                    matrix_valid[N + i + 1][j + 1] = 100000
    for i in range(2 * N + 1):
        matrix_valid[i][0] = 0

    matrix_check = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:

                matrix_check[i][j] = 0
            else:
                distance = euclidean_distance(trees[i].xaxis, trees[i].yaxis, trees[j].xaxis, trees[j].yaxis)
                if distance <= C:
                    matrix_check[i][j] = 1
    connected = []
    if (sum(map(sum, matrix_check))) == (N * (N - 1)) and weak_tree_num == 0:
        # pp("Monkeys can meet at all the trees")
        for i in range(N):
            connected.append(i)

        print(*connected)
        sys.exit()
    if (sum(map(sum, matrix_check))) == (N * (N - 1)) and weak_tree_num != 0:

        print(weak_tree_num)
        sys.exit()
    # If the trees are not connected and monkeys are present on disconnected trees
    for i in range(N):
        connected_tree = 0
        for j in range(N):
            connected_tree += matrix_check[i][j]
        if connected_tree == 0 and trees[i].num_monkeys > 0:
            print(-1)
            sys.exit()



    final_result = [[0] for i in range(N)]
    for i in range(N):
        new_matrix = deepcopy(matrix_valid)
        new_graph = Graph(new_matrix)
        source = 0;
        sink = i + 1
        output = 0
        output = new_graph.FordFulkerson(source, sink)


        if output >= (total_monkeys):
            final_result[i] = 1
        else:
            final_result[i] = 0
    # Print final result
    result = []

    for index, final_result in enumerate(final_result):
        if final_result != 0:
            result.append(index)

    print(*result)

