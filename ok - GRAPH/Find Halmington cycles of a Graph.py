import random

f = open('importEdge_Graph.txt', 'r')
f = f.readlines()
edges = []
for k in f:
    k = k.strip().split(' ')
    if len(k) < 1:
        continue
    if (k[0],k[1],float(k[2])) not in edges:
        edges.append((k[0],k[1],float(k[2])))
    if (k[1],k[0],float(k[2])) not in edges:
        edges.append((k[1], k[0], float(k[2])))
vertices = []
for k in edges:
    if k[0] not in vertices:
        vertices.append(k[0])
    if k[1] not in vertices:
        vertices.append(k[1])
print('Vertices: ',vertices)
print('Edges: ',edges)

# === HÀM TỔ HỢP ===

import random

def list_Tổ_hợp(listElements,length):
    số_tổ_hợp = giai_thừa(len(listElements)) // ( giai_thừa(length) * giai_thừa(len(listElements)-length) )
    list_Tổ_hợp = []
    while len(list_Tổ_hợp) < số_tổ_hợp:
        tổ_hợp = set()
        for i in range(length):
            while True:
                x = listElements[random.randint(0,len(listElements)-1)]
                if x not in tổ_hợp:
                    tổ_hợp.add(x)
                    break
                else:
                    continue
        if tổ_hợp not in list_Tổ_hợp:
            list_Tổ_hợp.append(tổ_hợp)
        else:
            continue
    for i in range(len(list_Tổ_hợp)):
        list_Tổ_hợp[i] = tuple(list_Tổ_hợp[i])

    return list_Tổ_hợp

def giai_thừa(number):
    if number <= 1:
        return 1
    return number*giai_thừa(number-1)

# === END OF HÀM TỔ HỢP ===

# ==== HÀM CHECK HALMINGTON CYCLE ===
def is_Halmington_cycle(set_n_edge,listVertices):
    cost = 0
    Halmington_cycle = [set_n_edge[0]]
    for i in range(len(set_n_edge)):
        doing = Halmington_cycle[-1][-2]
        for edge in set_n_edge:
            if edge not in Halmington_cycle and edge[0] == doing:
                Halmington_cycle.append(edge)
                break
            else:
                continue
    check = {}
    for edge in Halmington_cycle:
        check[edge[0]] = check.get(edge[0],0) + 1
        check[edge[1]] = check.get(edge[1], 0) + 1
    if len(check) != len(listVertices):
        return False, None, None, check
    for value in list(check.values()):
        if value != 2:
            return False,None,None,check
    for edge in Halmington_cycle:
        cost += edge[-1]

    return True, Halmington_cycle,cost,check

# ==== END OF HÀM CHECK HALMINGTON CYCLE ===

listOfsets_n_edge = list_Tổ_hợp(edges,len(vertices))
list_Halmington_cycles = []
for set_n_edge in listOfsets_n_edge:
    if is_Halmington_cycle(set_n_edge,vertices)[0]:
        boo, cycle, cost, check = is_Halmington_cycle(set_n_edge, vertices)
        list_Halmington_cycles.append((cycle,cost))

list_Halmington_cycles = sorted(list_Halmington_cycles,key=lambda x:x[1])
chosen = list_Halmington_cycles[0]

print('='*20)
print('Shortest Halmington cycle is: ')
print(chosen[0])
print('Cost: ',chosen[-1])