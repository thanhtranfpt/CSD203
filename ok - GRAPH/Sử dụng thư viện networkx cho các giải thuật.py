# Sử dụng thư viện networkx cho các giải thuật:
# - Prim
# - Kruskal
# - Fleury (chu trình Euler)


import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree

#Initial
G = nx.Graph()
l=[('0','1',4) ,('0', '7', 8) ,('1', '2', 8) ,('1', '7', 11) ,('2', '3', 7) ,('2', '5', 4) ,('2', '8', 2) ,('3', '4', 9) ,('3', '5', 14) ,('4', '5', 10) ,('5', '6', 2) ,('6', '7', 1) ,('6', '8', 6) ,('7', '8', 7)]
G.add_weighted_edges_from(l)

'''G=nx.complete_graph(3)''' #use to test Euler cycle, if not need don't care

#Call Kruskal
'''mst = tree.minimum_spanning_edges(G, algorithm='kruskal', data=True)
edgelist = list(mst)
print('Các cạnh của cây khung là: \n',edgelist)'''
#creat new_l for new_G: dùng để vẽ minh họa thôi
'''new_l = []
for k in edgelist:
    new_l.append((k[0],k[1],k[2]['weight']))
new_G = nx.Graph()
new_G.add_weighted_edges_from(new_l)'''

#Call Prim
'''mst = tree.minimum_spanning_edges(G,algorithm='prim',data=True)
edgelist = list(mst)
print('Các cạnh của cây khung là: \n',edgelist)'''
#creat new_l for new_G: dùng để vẽ minh họa thôi
'''new_l = []
for k in edgelist:
    new_l.append((k[0],k[1],k[2]['weight']))
new_G = nx.Graph()
new_G.add_weighted_edges_from(new_l)'''

#Call Fleury
'''e_cycle = list(nx.eulerian_circuit(G, source=1)) #source có thể ko ghi hoặc ghi None.
print(e_cycle)''' #if not eulerian, raise error - so don't be scared

#Draw G
'''pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
plt.show()'''
#Draw new_G
'''pos = nx.spring_layout(new_G)
nx.draw(new_G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(new_G, 'weight')
nx.draw_networkx_edge_labels(new_G, pos, edge_labels=edge_weight)
plt.show()'''