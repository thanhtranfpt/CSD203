'''2- Sử dụng cách biểu diễn đồ thị bằng ma trận kề,
đọc dữ liệu từ và một file theo cấu trúc: dòng đầu số đinh,
dòng sau là các cạnh kết nối giữa các đỉnh cách nhau bởi khoảng trắng'''
'''
4
0 1
0 2
0 3
2 3
'''

qq = input('Enter file name: ')
if len(qq)<1:
    fhand = open('../file_import.txt','r')
else:
    fhand = open(qq, 'r')
fhand = fhand.readlines()
k = 0
for line in fhand:
    if k==0:
        x = line
    k+=1
x = int(x)

v = x
e = k-1
vertexes = []
ve_ed = {}
z = 0
for line in fhand:
    if z==0:
        z+=1
        continue
    edge = line

    edge = edge.strip().split(' ')
    for k in edge:
        if k not in vertexes:
            vertexes.append(k)
    if edge[0] not in list(ve_ed.keys()):
        ve_ed[edge[0]] = [edge[1]]
    else:
        ve_ed[edge[0]].append(edge[1])
    if edge[1] not in list(ve_ed.keys()):
        ve_ed[edge[1]] = [edge[0]]
    else:
        ve_ed[edge[1]].append(edge[0])

vertexes = sorted(vertexes)
print(' ' * 5, end='')
for i in vertexes:
    print(str(i).center(5, ' '), end='')
print()
print('_' * 5 * (len(vertexes) + 1))
for i in vertexes:
    print((str(i) + ' |').ljust(5, ' '), end='')
    for k in vertexes:
        if k in ve_ed[i]:
            print(str(1).center(5, ' '), end='')
        else:
            print(str(0).center(5, ' '), end='')
    print()
