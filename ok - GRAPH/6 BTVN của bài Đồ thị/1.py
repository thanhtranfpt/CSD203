# ========== 1 ==========
'''
input:
0 : [0. 1. 1. 1.]
1 : [1. 0. 0. 0.]
2 : [1. 0. 0. 1.]
3 : [1. 0. 1. 0.]
output:
[0]: [1,2,3]
[1]: [0]
[2]: [0,3]
[3]: [0,2]
'''


v = int(input('Enter number of vertexes: '))
vertexes = input('Enter vertexes (separated by " "): ')
vertexes = vertexes.strip().split(' ')
vertexes = sorted(vertexes)
#vertexes = [0,1,2,3]
#print(vertexes)
line = {}
line_result = {}
for i in range(v):
    print('Enter the ',i+1,'(th) line of the matrix given (sorted vertexes, separated by " "): ',sep='',end='')
    line[i+1] = input()
    line[i+1] = line[i+1].strip().split(' ')
#print(line)
#line = {1: [0,1,1,1], 2: [1,0,0,0], 3 : [1 0 0 1], 4 : [1 0 1 0]}
for k in range(len(vertexes)):
    line_result[vertexes[k]] = []
    i = 0
    for x in line[k+1]:
        if x == '0':
            i = i+1
        elif x == '1':
            line_result[vertexes[k]].append(vertexes[i])
            i = i+1
#print(line_result)
for a,b in line_result.items():
    print(a,': ',b)
