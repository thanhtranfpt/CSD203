import random

vertices = ['a','b','c','d','e','f','g','h','i','j','k']
print(len(vertices))
edges = [('a','c'),('b','c'),('c','e'),('d','e'),('e','f'),('d','f'),('g','f'),('f','h'),\
         ('g','h'),('h','i'),('k','j'),('h','k')]

# === START
which = vertices[random.randint(0,len(vertices)-1)]

lst = [which]
new_edges = []
while len(lst) < len(vertices):
    doing = lst[-1]
    check = False
    for which in vertices:
        if ((which,doing) in edges or (doing,which) in edges) and which not in lst:
            lst.append(which)
            new_edges.append((doing,which))
            check = True
            break
    if check == False:
        i = -2
        while True:
            doing = lst[i]
            for which in vertices:
                if ((which,doing) in edges or (doing,which) in edges) and which not in lst:
                    lst.append(which)
                    new_edges.append((doing,which))
                    check = True
                    break
            if check == True:
                break
            else:
                i -= 1
                continue
print(lst)
print('Edges of spanning tree: ',new_edges)