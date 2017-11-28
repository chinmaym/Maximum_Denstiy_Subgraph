'''
Created on Nov 24, 2017

@author: Chinmay Mishra
'''
from Core.Graph import Graph
from platform import node
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
    print graph
    q = list()
    q.append(source)
    visited = list()
    visited.append(source)
    nodeList = []
    while len(q)!=0:
        node = q[0]
        q.remove(node)
        print node
        print "node", node
        print "source", source
        for ind,u in enumerate(graph[node]):
            if u > 0:
                if ind not in visited:
                    q.append(ind)
                if ind not in nodeList:
                    nodeList.append(ind)
                visited.append(ind)
    return nodeList

def createNewGraph(nodeList,graph):
    print nodeList
    n=0;m=0
    newGraph = []
    for index,i in enumerate(graph):
#         print i
        if (index+1) in nodeList:
            n+=1
            if nodeList:
                currentNodeList = [x for ind,x in enumerate(i) if ind+1 in nodeList]
            else:
                currentNodeList = i
            m += sum(currentNodeList)
    #         print currentNodeList
            newGraph.append(currentNodeList)
    print n,m/2,newGraph
    return n,m/2,newGraph

def densestSubgraph(graph,v,e):
    origGraph = copyGraph(graph)
    checkValue = float(1)/(v*(v-1))
    nodeSet = [x for x in range(1,v+1)]
    removedNodes = []
    removedNodesCount = 1
    print "checkValue", checkValue
    n=5; m=6
    l=0;u=m;
    while u-l>=checkValue:
        print "l",l
        print "u",u
        g = (float(u)+l)/2;
        print "g",g
        print "u-l", u-l
        print "checkValue",checkValue
        print "graph ", graph
        deg = [calculateDegree(i, graph) for i,_ in enumerate(graph)]
        graph1 = convert2network(graph, deg, n, m,g)
        modifiedGraph = copyGraph(graph1)
        print "converted graph to network  ",graph1
        graph2 = Graph(graph1)
        graph2.findMinCut(0, len(graph1)-1)
        print "mincut  ", graph2.minCut
        print "modified graph  ", modifiedGraph
        removeEdges(modifiedGraph, graph2.minCut)
        print "after removing edges ", modifiedGraph
        s = findSets(modifiedGraph)
        print "nodes in set s ", s
        n1,m1,newGraph = createNewGraph(s,graph)
        if len(s) == 0:
            u = g
        else:
            l = g       
            graph = newGraph
            removedNodes.append(([x for x in range(1,len(modifiedGraph)-1) if x not in s ],removedNodesCount))
            removedNodesCount+=1
            n=n1;m=m1
        raw_input()
    return graph,removedNodes
        
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
    vertices = input("Enter the number of vertices :")
    print "Enter the adjacency matrix \n"
    mat = []
    edges = 0
    for _ in range(vertices):
        row = map(int,raw_input().split(' '))
        edges = sum(row)
        mat.append(row)
    edges = edges/2
    print mat
    deg = []
    for i in range(v):
        deg.append(calculateDegree(i,mat))
    densestSubGraphNetwork,removedNodes = densestSubgraph(mat,vertices,edges)
    print densestSubGraphNetwork
    print removedNodes