import networkx as nx
import matplotlib.pyplot as plt

# A Python program for Prim's Minimum Spanning Tree (drawG) algorithm.
# The program is for adjacency matrix representation of the G

import sys  # Library for INT_MAX


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed drawG stored in parent[]
    def printMST(self, parent):
        # import vào G mới để dễ truy xuất và minh họa:
        MST_Graph = nx.Graph()
        #
        #print("Edge \tWeight")
        for i in range(1, self.V):
            #print(parent[i], "-", i, "\t", self.G[i][parent[i]])
            MST_Graph.add_weighted_edges_from([(parent[i],i,self.graph[i][parent[i]])]) #đây là các edge của cây khung.

        return MST_Graph

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print drawG for a G
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed drawG
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # G[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in drawG
                # Update the key only if G[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        #self.printMST(parent)

        return parent


if __name__ == '__main__':

    g = Graph(5)

    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    # THỰC THI - nếu muốn print ra màn hình thì phá 2 cái # ở def printMST./.
    parent = g.primMST()
    graphDraw = g.printMST(parent)
    #vẽ minh họa kết quả:
    pos = nx.spring_layout(graphDraw)
    nx.draw(graphDraw, pos, with_labels=True, font_weight='bold')
    edge_weight = nx.get_edge_attributes(graphDraw, 'weight')
    nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edge_weight)
    plt.show()