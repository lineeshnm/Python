#! python3
from pprint import pprint as pp
import sys
import random
import math
from collections import defaultdict
from copy import deepcopy

class Graph:
    v = 0
    adjList = []
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
    def Graph(self, vertices):
        self.v = vertices
        initAdjList(self.v)
    def initAdjList(self, v):
        adjList = []
        for i in range(v):
            adjList[i] = []
    # add edge from u to v
    def addEdge(self, u , v):
        adjList[u].append(v)
    def getAdjList(self, u):
        return adjList[u]
    # Prints all paths from source to destination
    def printAllPaths(self, s, d):
        isVisited = []
        pathList = []
        result = []
        pathList.append(s)
        printAllPathsUtil(s, d, isVisited, pathList,result)
        return result
    def printAllPathsUtil(self, u, d, isVisited, localPathList, result):
        isVisited[u] = True
        if