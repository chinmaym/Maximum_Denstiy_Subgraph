'''
Created on Nov 24, 2017

@author: Chinmay Mishra
'''
from Core.Graph import Graph
def calculateDegree(i,graph):
    deg = sum(graph[i])
    for ind,j in enumerate(graph):
        if ind!=i:
            if j[i] == 1:
                deg += 1
    return deg

def copyGraph(graph):
    newGraph=[]
    for i in graph:
        newGraph.append(list(i))
    return newGraph

def findSets(graph,source = 0):
    q = list()
    q.append(source)
    visited = list()
    newGraph = list()
    while len(q)!=0:
        print q
        nodeList = []
        node = q.pop()
        visited.append(node)
        if node != source:
            nodeList = [0]*len(graph[node])
        for ind,u in enumerate(graph[node]):
            if u == 1 and ind not in visited:
                q.append(ind)
                if node != source:
                    nodeList[u] = 1
        if len(nodeList) > 0:
            newGraph.append(nodeList)
    return newGraph

def densestSubgraph(graph,v,e):
    origGraph = copyGraph(graph)
    n=5; m=6
    l=0;u=m;
    while u-l>=1/(v*(v-1)):
        g = (float(u)+l)/2;
        print g
        deg = [calculateDegree(i, graph) for i,j in enumerate(graph)]
        graph1 = convert2network(graph, deg, n, m,g)
        print graph1
        graph2 = Graph(graph1)
        graph2.findMinCut(0, len(graph1)-1)
        print graph2.minCut
        modifiedGraph = copyGraph(graph2.graph)
        print modifiedGraph
        removeEdges(modifiedGraph, graph2.minCut)
        print modifiedGraph
        s = findSets(modifiedGraph)
        print s
        if len(s) == 0:
            u = g
        else:
            l = g       
            graph = s
        input()
        
def removeEdges(graph,minCut):
    for i,j in minCut:
        graph[i][j] = 0
    pass

def convert2network(graph,deg,v,e,g):
    newGraph = [] 
    source = [0]
    source.extend([e]*v)
    source.append(0)
    sink = [ e+(2*g)-i for i in deg ]
    newGraph.append(source)
    for ind,i in enumerate(graph):
        i1=[0]
        i1.extend(i)
        i1.append(sink[ind])
        newGraph.append(i1)
    newGraph.append([0]*(v+2))
    return newGraph


if __name__=="__main__":
    v=5;e=6
    graph = [[0,1,1,0,1],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [0,0,0,0,1],
         [1,1,1,1,0]
        ]
    print graph
    deg = []
    for i in range(v):
        deg.append(calculateDegree(i,graph))
    densestSubgraph(graph,v,e)
    print graph