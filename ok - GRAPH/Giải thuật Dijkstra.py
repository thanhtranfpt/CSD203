class Graph: #đồ thị vô hướng
    def __init__(self):
        self.vertexes = []
        self.edges = []
        self.weightDetail = {}
    def printSet(self):
        print('Vertexes: ',self.vertexes)
        print('Edges: ',self.edges)

    def addEdge_weight(self,a,b,w):
        if not a in self.vertexes:
            self.vertexes.append(a)
        if not b in self.vertexes:
            self.vertexes.append(b)
        if not (a,b) in self.edges:
            self.edges.append((a,b))
        if not (a,b) in self.weightDetail:
            self.weightDetail[(a,b)] = w
        if not (b,a) in self.weightDetail:
            self.weightDetail[(b,a)] = w

    def DIJKSTRA(self, start = 1):
        self.vertexes = sorted(self.vertexes)
        lst = {}
        lst_route = {}
        visited = {}
        for k in self.vertexes:
            visited[k] = False
            lst[k] = 0
            lst_route[k] = []
        que = [start]
        visited[start] = True
        for k in que:
            for i in self.vertexes:
                if visited[i] == False:
                    if (i,k) in self.edges or (k,i) in self.edges:
                        if (lst[i] > lst[k] + self.weightDetail[(k,i)]) or lst[i] == 0:
                            lst[i] = lst[k] + self.weightDetail[(k,i)]
                            lst_route[i] = []
                            for point in lst_route[k]:
                                lst_route[i].append(point)
                            lst_route[i].append(k)
                        if i not in que:
                            que.append(i)
            visited[k] = True
        return lst,lst_route

if __name__ == '__main__':
    g = Graph()

    # TEST THUẬT TOÁN Dijkstra's TÌM ĐƯỜNG ĐI NGẮN NHẤT GIỮA 2 ĐIỂM BẤT KỲ
    # Step 1/3: Input edges with weight
    g.addEdge_weight(1, 2, 7)
    g.addEdge_weight(1, 6, 14)
    g.addEdge_weight(1, 3, 9)
    g.addEdge_weight(2, 3, 10)
    g.addEdge_weight(4, 2, 15)
    g.addEdge_weight(3, 6, 2)
    g.addEdge_weight(3, 4, 11)
    g.addEdge_weight(5, 6, 9)
    g.addEdge_weight(4, 5, 6)

    # Step 2/3: Input start-end points
    x = input('Bạn muốn đi từ đâu tới đâu (phân cách bởi " "): ')

    # Step 3/3: Use the function DIJKSTRA(start)
    x = x.strip().split(' ')
    start = int(x[0])
    end = int(x[-1])
    ketQua = g.DIJKSTRA(start)

    # Print the result
    print('Độ dài ngắn nhất từ đỉnh tên ', start, ' đến đỉnh tên ', end, ' là: ', ketQua[0][end])
    print('Lộ trình ngắn nhất đi từ đỉnh tên ', start, ' đến đỉnh tên ', end, ' là: ', end=' ')
    for k in ketQua[1][end]:
        print(k, end=' --> ')
    print(end)

    # END OF TEST THUẬT TOÁN Dijkstra's TÌM ĐƯỜNG ĐI NGẮN NHẤT GIỮA 2 ĐIỂM BẤT KỲ