##Floyd
def output(X, Y, Z, listA, nums):
    size = len(nums)+1
    graph = [[0]*size for r in range(size)]
    distance = [[0]*size for r in range(size)]
    path = [[0]*size for r in range(size)]
    for i in range(1, len(listA)):
        for j in range(1, len(listA)):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = 9999
    for i in range(len(listA)):
        start = listA[i][0]
        end = listA[i][1]
        graph[start][end] = listA[i][2]
    
    vertex_total = len(nums)
    for i in range(1, vertex_total+1):
        for j in range(1, vertex_total+1):
            distance[i][j] = graph[i][j]
            path[i][j] = j
    for k in range(1, vertex_total+1):
        for i in range(1, vertex_total+1):
            for j in range(1, vertex_total+1):
                if distance[i][k]+distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]
                    path[i][j] = path[i][k]
    result = distance[Y][Z]
    if result == 9999:
        print(-1)
    else:
        _path = str(Y)
        p = path[Y][Z]
        while p!=Z:
            _path = _path+' '+str(p)
            p = path[p][Z]
        _path  = _path+' '+str(Z)
        print(_path)
        print(result)

if __name__ == '__main__':
    n = list(map(int, input().split(" ")))
    X = n[0]
    Y = n[1]
    Z = n[2]
    listA = []
    nums = []
    for i in range(X):
        temp = list(map(int, input().split(" ")))
        listA.append(temp)
        nums.append(temp[0])
        nums.append(temp[1])
    nums = list(set(nums))
    output(X, Y, Z, listA, nums)

