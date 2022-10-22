#from collections import defaultdict: cái này ko cần ở đây.

class Graph:
    def __init__(self,number_of_Vertex):
        self.V = number_of_Vertex
        self.adjMatrix = [ [0 for i in range(self.V)]
                            for j in range(self.V) ]
        self.visited = [False] * self.V

    def addEdge(self,u,v):
        self.adjMatrix[u][v] = 1 #đồ thị ko trọng số
        self.adjMatrix[v][u] = 1 #đây là đồ thị vô hướng, ko trọng số

    def DFS_Recursion(self,u):
        self.visited[u] = True
        print(u, end=' ')
        for v in range(self.V):
            if self.visited[v] == False and self.adjMatrix[u][v] > 0:
                self.DFS_Recursion(v)

    def DFS_nonRecursion(self,s):
        visited = [False for i in range(self.V)]

        # Create a stack for DFS
        stack = []

        # Push the current source node.
        stack.append(s)

        while stack != []:
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                print(s, end=' ')
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for u in range(self.V):
                if self.adjMatrix[s][u] > 0 and (not visited[u]):
                    stack.append(u)

    def BFS_Recursion(self,q):
        if q == []:
            return
        v = q[0]
        self.visited[v] = True
        print(v, end=' ')
        q = q[1:]
        for u in range(self.V):
            if self.adjMatrix[v][u] > 0 and self.visited[u] == False:
                self.visited[u] = True
                q.append(u)
        self.BFS_Recursion(q)

    def BFS_nonRecursion(self,s):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in range(self.V):
                if visited[i] == False and self.adjMatrix[s][i] > 0:
                    queue.append(i)
                    visited[i] = True

    def Connectivity_DFS(self):
        i=0
        print('\n', ' DFS --> check Connectivity '.center(50, '='), sep='')
        self.visited = [False] * g.V
        while False in self.visited:
            i+=1
            for v in range(self.V):
                if self.visited[v] == False:
                    self.DFS_Recursion(v)
                    print()
                    break
        if i > 1:
            print('No connectivity.')
        else:
            print('CONNECTIVITY.')

        print('Đồ thị có: ',i,' thành phần liên thông.')

if __name__ == '__main__':
    g = Graph(4) #khai báo số đỉnh: các đỉnh COI NHƯ sẽ đánh tên từ 0,1,2,3,...
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.adjMatrix)

    # === DFS ĐỆ QUY: đúng ý giảng viên ===
    print('\n',' DFS ĐỆ QUY '.center(30,'='),sep='')
    for v in range(g.V):
        print(v, ': ', end=' ')
        g.visited = [False]*g.V
        g.DFS_Recursion(v)
        print()

    # === DFS KHÔNG ĐỆ QUY: khả năng cao là đúng ===
    print('\n',' DFS KHÔNG ĐỆ QUY '.center(30,'='),sep='')
    for v in range(g.V):
        print(v, ': ', end=' ')
        g.DFS_nonRecursion(v)
        print()

    # === BFS ĐỆ QUY: ===
    print('\n', ' BFS ĐỆ QUY '.center(30, '='), sep='')
    for v in range(g.V):
        print(v, ': ', end=' ')
        g.visited = [False] * g.V
        q = [v]
        g.BFS_Recursion(q)
        print()

    # === BFS KHÔNG ĐỆ QUY: ===
    print('\n', ' BFS KHÔNG ĐỆ QUY '.center(30, '='), sep='')
    for v in range(g.V):
        print(v, ': ', end=' ')
        g.BFS_nonRecursion(v)
        print()


    #4- Dựa trên DFS kiểm tra một đồ thị có liên thông hay không (tức là đồ thị gọi là liên thông nếu giữa 2 điểm bất kỳ luôn tồn tại 1 đường đi)
    #5- Nếu đồ thị không liên thông thì nó có thể tách thành các thành phần liên thông
        #a- Đồ thị có bao nhiêu thành phần liên thông
        #b- In ra từng thành phần liên thông

    g.Connectivity_DFS()