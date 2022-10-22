import networkx as nx
import matplotlib.pyplot as plt
import scipy

# khai báo đồ thị vô hướng
G = nx.Graph()
#Nếu là đồ thị có hướng, viết: G = nx.DiGraph()


# LOAD DATA FROM FILE, ADD TO GRAPH.NODES, GRAPH.EDGES()
fhand = input('Enter file name: ')
if len(fhand) < 1:
    fhand = open('file_import.txt','r')
else:
    fhand = open(fhand,'r')
fhand = fhand.readlines()

for line in fhand:
    nodes = line.strip().split(' ')
    if len(nodes) == 1:
        numNodes = int(nodes[0])
    elif len(nodes) > 1:
        for node in nodes:
            G.add_node(node)
        if len(nodes) == 2:
            G.add_edge(nodes[0],nodes[1])
        elif len(nodes) == 3:
            G.add_weighted_edges_from([(nodes[0],nodes[1],float(nodes[-1]))])


# 1- Vào 1 Graph biểu diễn bằng ma trận kề, đọc vào từ 1 file

num = 7*(len(G.nodes())+1)+len(G.nodes())+1
print(' MA TRẬN KỀ '.center(num,'='))

A = nx.adjacency_matrix(G)
print(A.todense())
#Nếu muốn in ra có các cạnh nào thì: print(A)

#MUỐN IN RA ĐẸP THÌ LÀM CÁI NÀY
'''print(' '*7,end='|')
for node in G.nodes():
    print(str(node).center(7,' '),end='|')
print()
print('-' * num)
for node in G.nodes():
    print(str(node).center(7,' '),end='|')
    for node2 in G.nodes():
        if (node2,node) in G.edges():
            print('1'.center(7,' '),end='|')
        else:
            print('0'.center(7, ' '), end='|')
    print()
print()'''
#END OF MUỐN IN RA ĐẸP THÌ LÀM CÁI NÀY


# 2- Vào 1 Graph biểu diễn bằng danh sách kề, đọc vào từ 1 file

print(' DANH SÁCH KỀ '.center(num,'='))

print(G.adj) #Lưu dưới dạng dictionary, muốn in ra dễ đọc phải truy xuất keys, values

#MUỐN IN RA ĐẸP THÌ LÀM CÁI NÀY
'''for a,b in G.adj.items():
    print(a,': ',end='')
    for k in b:
        if b[k] == {}:
            print(k,end=', ')
        else:
            print(k,' (weight: ',b[k]['weight'],'), ',sep='',end='')
    print()
print()'''
#END OF MUỐN IN RA ĐẸP THÌ LÀM CÁI NÀY


# 3- In ra bậc của các đỉnh với đồ thị biểu diễn bằng 1 trong 2 cách ở trên

print(' BẬC CỦA CÁC ĐỈNH '.center(num,'='))

for node in G.nodes():
    print(node,': ',G.degree(node))


# 4- DFS

print(' DFS '.center(num,'='))

for node in G.nodes():
    T = nx.dfs_tree(G,source=node,depth_limit=5) #source và depth_limit KHÔNG GHI CŨNG ĐC
    print(list(T.nodes())) #Hoặc muốn in ra các cạnh: T.edges()


# 5- BFS

print(' BFS '.center(num,'='))

for node in G.nodes():
    T = nx.bfs_tree(G,source=node) #depth_limit KHÔNG GHI CŨNG ĐC, source BẮT BUỘC
    print(list(T.nodes())) #Hoặc muốn in ra các cạnh: T.edges()


# 6- Dijkstra cho đồ thị như ví dụ trong slide

print(' Dijkstra '.center(num,'='))

#import G information:
G_2 = nx.Graph()
E=[(1,2,7),(1,3,9),(1,6,14),(2,3,10),(2,4,15),(3,4,11),(3,6,2),(4,5,6),(5,6,9)]
G_2.add_weighted_edges_from(E)
#end of import G information.

source = 1
destination = 5

#print path and path length:
print(nx.dijkstra_path(G_2,source,destination))
print(nx.dijkstra_path_length(G_2,source,destination))
#end of print path and path length.



# ===== CHÚ THÍCH: MỘT SỐ CÚ PHÁP TRONG NETWORKX =====

# ADD NODES
#G.add_node('A')
#G.add_nodes_from(['B','C','D'])

# ADD EDGES
#G.add_edge('A','B')
#G.add_edges_from([('A','C'),('A','D'),('B','E')])
#G.add_weighted_edges_from([('A','B',2),('A','C',3),('B','D',4),('B','E',5)])

#PRINT DANH SÁCH KỀ, BẬC
#print('G.adj: ',G.adj) hoặc for k in G.adjacency(): print(k)
#print('Degree A: ',G.degree('A'))


# === VẼ ĐỒ THỊ ===
# Nếu là đồ thị không trọng số:
nx.draw(G,with_labels=True,font_weight='bold')
plt.show()
# Nếu là đồ thị có trọng số:
'''pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
plt.show()'''
#lưu ảnh: plt.savefig('drawGraph.png')


# test vẽ đồ thị petersen:
'''GP = nx.petersen_graph()
nx.draw(GP,with_labels=True,font_weight='bold')
plt.show()'''
# end of test vẽ đồ thị petersen