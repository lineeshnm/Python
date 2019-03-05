from pprint import pprint
import sys
import random
import math
from collections import defaultdict
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

    def print_tree_info(self):
        print("X: %d Y: %d Num_of_Monkeys: %d Threshold: %d Tree_Num: %d " % (
            self.xaxis, self.yaxis, self.num_monkeys, self.threshold, self.Tree_Num))

    def total_trees(self):
        return Tree.Tree_Num

    def monkey_jump(self, tree):
        # when monkey jump from self, reduce threshold and reduce number of monkeys remaining in the tree, increse number of monkeys on target
        self.threshold -= 1
        if self.threshold <= 0:
            self.__del__()
        self.num_monkeys -= 1
        tree.num_monkeys += 1

    def __del__(self):
        return True


def euclidean_distance(x1, y1, x2, y2, ):
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return distance


if __name__ == '__main__':
    input1 = input()
    N = int(input1.split()[0])
    C = float(input1.split()[1])

    trees = [[0] * 1 for i in range(N)]
    total_monkeys = 0
    for i in range(N):
        input1 = input()
        x, y, m, t = input1.split()
        total_monkeys += int(m)
        trees[i] = Tree(int(x), int(y), int(m), int(t))
        # trees[i].print_tree_info() ## This will print information about Entered Trees

    cnt = 0
    a = 0
    for i in range(N):
        if trees[i].num_monkeys > trees[i].threshold:
            # print("Monkey cannot jump")
            a = i
            cnt = cnt + 1
            if cnt > 1:
                print(-1)
                sys.exit()
    graph_matrix = [[0] * (N + 1) for i in range(N + 1)]
    graph_matrix_new = [[0] * (2 * N + 1) for i in range(2 * N + 1)]

    for i in range(N + 1):
        if i == 0:
            graph_matrix_new[0][i] = 0
        else:
            graph_matrix_new[0][i] = trees[i - 1].num_monkeys

    for i in range(N + 1):
        if i != 0:
            graph_matrix_new[i][N + i] = trees[i - 1].threshold

    for i in range(N + 1):

        for j in range(N + 1):

            if j < N and i < N:

                distance = euclidean_distance(trees[i].xaxis, trees[i].yaxis, trees[j].xaxis, trees[j].yaxis)
                if distance <= C:
                    graph_matrix_new[N + i + 1][j + 1] = 100000
    for i in range(2 * N + 1):
        graph_matrix_new[i][0] = 0

    # pprint(graph_matrix_new)
    graph_matrix_check = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:

                graph_matrix_check[i][j] = 0
            else:
                distance = euclidean_distance(trees[i].xaxis, trees[i].yaxis, trees[j].xaxis, trees[j].yaxis)
                if distance <= C:
                    graph_matrix_check[i][j] = 1
    z = []
    if (sum(map(sum, graph_matrix_check))) == (N * (N - 1)) and a == 0:
        # pp("Monkeys can meet at all the trees")
        for i in range(N):
            z.append(i)

        print(*z)
        sys.exit()
    if (sum(map(sum, graph_matrix_check))) == (N * (N - 1)) and a != 0:
        # pp("Monkeys can meet at all the trees")
        print(a)
        sys.exit()
        # If the trees are not connected and monkeys are present
    for i in range(N):
        sm = 0
        for j in range(N):
            sm = sm + graph_matrix_check[i][j]
        if sm == 0 and trees[i].num_monkeys > 0:
            print(-1)
            sys.exit()

    # pp(graph_matrix)
    # pp(graph_matrix_check)
    # pp(graph_matrix)

    final_result = [[0] for i in range(N)]
    for i in range(N):
        b = deepcopy(graph_matrix_new)
        g = Graph(b)
        source = 0;
        sink = i + 1
        output = 0
        output = g.FordFulkerson(source, sink)

        # print(output)
        if output >= (total_monkeys):
            final_result[i] = 1
        else:
            final_result[i] = 0
    s = []

    for index, final_result in enumerate(final_result):
        if final_result != 0:
            s.append(index)

    print(*s)
    # print(index, final_result)
