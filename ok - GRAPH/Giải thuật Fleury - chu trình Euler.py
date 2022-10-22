import networkx as nx
import matplotlib.pyplot as plt

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
    def isIsolated(self,vertex):
        check = True
        for edge in self.edges:
            if vertex in edge:
                check = False
        return check
    def chooseY_forFleury(self,ch):
        listY = []
        for Y in self.vertexes:
            if (ch, Y) in self.edges:
                listY.append(Y)
        listY = sorted(listY)
        return listY[0]
    def Fleury(self,X): #chú ý khi thực thi giải thuật này tác động DELETE lên self.edges
        S = [] #Stack
        E = []
        S.append(X)
        while S != []:
            ch = S[-1]
            if self.isIsolated(ch):
                S=S[:-1]
                E.append(ch)
            else:
                Y = self.chooseY_forFleury(ch)
                S.append(Y)
                del self.edges[(ch,Y)]
                del self.edges[(Y,ch)]
        return E



if __name__ == '__main__':
    g= Graph_weight()

    '''g.addEdge('0','1',4)
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
    g.addEdge('7', '8', 7)'''

    g.addEdge(0,1,1)
    g.addEdge(0,4,1)
    g.addEdge(1,4,1)
    g.addEdge(4,3,1)
    g.addEdge(2,4,1)
    g.addEdge(2,3,1)



    def drawGraph(graph):
        graphDraw = nx.Graph()
        for a, b in graph.edges.items():
            graphDraw.add_weighted_edges_from([(a[0], a[-1], b)])
        pos = nx.spring_layout(graphDraw)
        nx.draw(graphDraw, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(graphDraw, 'weight')
        nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edge_weight)
        plt.show()

    drawGraph(g)


    # THỰC THI
    print(g.Fleury(1))