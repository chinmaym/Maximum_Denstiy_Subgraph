from Graph import Graph


if __name__=="__main__":
#     graph_values = [[0, 16, 13, 0, 0, 0],
#         [0, 0, 10, 12, 0, 0],
#         [0, 4, 0, 0, 14, 0],
#         [0, 0, 9, 0, 0, 20],
#         [0, 0, 0, 7, 0, 4],
#         [0, 0, 0, 0, 0, 0]]

    graph_values = [[0,2,0,4,0,0],
                    [0,0,3,1,0,0],
                    [0,0,0,3,0,4],
                    [0,0,0,0,3,0],
                    [0,0,1,0,0,3],
                    [0,0,0,0,0,0]]
    graph = Graph(graph_values)
    source = 0 
    sink = 5
    graph.findMinCut(source, sink)
    print "The min cut of the graph", graph.minCut