# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted G

from collections import defaultdict


# Class to represent a G


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store G

    # function to add an edge to G
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct drawG using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant drawG

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given G, we can create a copy of G
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        #print("Edges in the constructed drawG")
        for u, v, weight in result:
            minimumCost += weight
            #print("%d -- %d == %d" % (u, v, weight))
        #print("Minimum Spanning Tree", minimumCost)

        return result


if __name__ == '__main__':

    g = Graph(4) #số đỉnh
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call:
    edges_of_MST = g.KruskalMST() #nếu muốn print ra màn hình: phá 3 dấu # ở gần cuối def KruskalMST


    # minh họa vẽ drawG:
    import networkx as nx
    import matplotlib.pyplot as plt
    MST = nx.Graph()
    for k in edges_of_MST:
        MST.add_weighted_edges_from([(k[0],k[1],k[-1])])
    pos = nx.spring_layout(MST)
    nx.draw(MST, pos, with_labels=True, font_weight='bold')
    edge_weight = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos, edge_labels=edge_weight)
    plt.show()