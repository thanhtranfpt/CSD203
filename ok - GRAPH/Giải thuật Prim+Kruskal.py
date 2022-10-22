import networkx as nx
import matplotlib.pyplot as plt

def containCycle(vertexList,edgeList): #ok tested: vertexList is dinstinct; edgeList is duplicate
    listLienThong = vertexList.copy()
    while listLienThong != []:
        #create label:
        label = {}
        for vertex in vertexList:
            label[vertex] = -1
        #create queue:
        queue = []
        queue.append(listLienThong[0])
        label[listLienThong[0]] = 0
        listLienThong.remove(listLienThong[0])
        #add vertex into queue:
        for k in queue:
            for vertex in vertexList:
                if (k,vertex) in edgeList:
                    if label[vertex] == 0:
                        return True
                    if label[vertex] == -1:
                        queue.append(vertex)
                        label[vertex] = 0
                        if vertex in listLienThong:
                            listLienThong.remove(vertex)
            label[k] = 1
    return False


class Graph_weight:
    def __init__(self):
        self.vertexes = []
        self.edges = {}
    def addNode(self,name):
        self.vertexes.append(name)
    def addEdge(self,name1,name2,weight):
        if not name1 in self.vertexes:
            self.vertexes.append(name1)
        if not name2 in self.vertexes:
            self.vertexes.append(name2)
        if not (name1,name2) in self.edges:
            self.edges[(name1,name2)] = weight
        if not (name2,name1) in self.edges:
            self.edges[(name2, name1)] = weight
    def Prim_makeMST(self, startPoint):
        mstR = nx.Graph()
        status = self.vertexes.copy()
        detail = {}
        detail[startPoint] = {}
        status.remove(startPoint)
        pointDetailList = []
        while status != []:
            for k in detail:
                if k in pointDetailList:
                    continue
                for point in status:
                    if (k,point) in self.edges:
                        detail[k][point]=self.edges[(k,point)]
                pointDetailList.append(k)
            costList = []
            for a,b in detail.items():
                for c,d in b.items():
                    if d is not None:
                        costList.append(d)
            costMin = min(costList)
            breaker = False
            for a,b in detail.items():
                for c,d in b.items():
                    if d == costMin:
                        if c in status:
                            point1 = a
                            point2 = c
                            w = d
                            breaker = True
                            break
                if breaker:
                    break
            mstR.add_weighted_edges_from([(point1,point2,float(w))])

            detail[point2] = {}
            del(detail[point1][point2])
            status.remove(point2)
            for a,b in detail.items():
                for c,d in b.items():
                    if c==point2:
                        detail[a][c] = None

        #ve do thi = networkx:
        pos = nx.spring_layout(mstR)
        nx.draw(mstR, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(mstR, 'weight')
        nx.draw_networkx_edge_labels(mstR, pos, edge_labels=edge_weight)
        plt.show()

    def KruskalMST(self):
        vertexList = self.vertexes.copy()
        egdeList = {}
        WeightList = []
        # create WeightList
        ddd = {}
        for a,b in self.edges.items():
            if (a[0],a[-1]) not in ddd:
                WeightList.append(b)
                ddd[(a[-1],a[0])] = True
        sortWeightList = sorted(WeightList)
        #start find the min weight
        i=0
        #==
        for weight in sortWeightList:
            for a,b in self.edges.items():
                if b==weight:
                    egdeList[(a[1], a[0])]=b
                    egdeList[(a[0], a[1])] = b
                    if containCycle(vertexList,egdeList):
                        del(egdeList[(a[0],a[1])])
                        del (egdeList[(a[1], a[0])])


        #add edgeList into drawGraph:
        mstR = nx.Graph()
        for a,b in egdeList.items():
            mstR.add_weighted_edges_from([(a[0], a[-1], float(b))])

        #ve do thi = networkx:
        pos = nx.spring_layout(mstR)
        nx.draw(mstR, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(mstR, 'weight')
        nx.draw_networkx_edge_labels(mstR, pos, edge_labels=edge_weight)
        plt.show()

if __name__ == '__main__':
    g= Graph_weight()
    g.addEdge('0','1',4)
    g.addEdge('0', '7', 8)
    g.addEdge('1', '2', 8)
    g.addEdge('1', '7', 11)
    g.addEdge('2', '3', 7)
    g.addEdge('2', '5', 4)
    g.addEdge('2', '8', 2)
    g.addEdge('3', '4', 9)
    g.addEdge('3', '5', 14)
    g.addEdge('4', '5', 10)
    g.addEdge('5', '6', 2)
    g.addEdge('6', '7', 1)
    g.addEdge('6', '8', 6)
    g.addEdge('7', '8', 7)

    #make drawG:
    g.Prim_makeMST('0')
    g.KruskalMST()