class Graph():
    def __init__(self,graph):
        self.graph = graph
        self.orginal_graph = [i[:] for i in graph]
        self.row = len(self.graph)
        self.col = len(self.graph[0])
        self.minCut = []
        
    def checkPath(self,s,t,parent):
        visited = [False]*self.row
        q = []
        q.append(s)
        visited[s] = True
        
        while q:
            u = q.pop(0)
            for ind,val in enumerate(self.graph[u]):
                if visited[ind] == False and val>0:
                    q.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    
    def minCut(self,source,sink):
        parent = [-1] * self.row
        max_flow = 0
        while self.checkPath(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s!=source:
                path_flow = min(path_flow,self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v!=source:
                u = parent[v]
                self.graph[v][u] -= path_flow
                self.graph[u][v] += path_flow
                v = parent[v]

        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.orginal_graph[i][j] > 0:
                    self.minCut.append((i,j))
        
        