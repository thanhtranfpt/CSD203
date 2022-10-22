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
    def graphColoring(self):
        color = {}
        for k in range(1,len(self.vertexes)+1):
            color[k] = []
        for v in self.vertexes:
            for a,b in color.items():
                c = True
                for k in b:
                    if (v,k) in self.edges:
                        c = False
                        break
                if c == True:
                    color[a].append(v)
                    break
        num=0
        for a,b in color.items():
            if b != []:
                print('Màu:',a,'- Các đỉnh:',b)
                num+=1
        return num

def drawGraph(graph):
        graphDraw = nx.Graph()
        for a, b in graph.edges.items():
            graphDraw.add_weighted_edges_from([(a[0], a[-1], b)])
        pos = nx.spring_layout(graphDraw)
        nx.draw(graphDraw, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(graphDraw, 'weight')
        nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edge_weight)
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

    drawGraph(g)

    # THỰC THI
    print('Số màu tối thiểu (the chromatic number) is: ',g.graphColoring())