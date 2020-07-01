import copy
def getLongestAlternatingSubsequenceDP(A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        dpRiseEnd = [0] * len(A)
        dpFallEnd = [0] * len(A)
        backTrackRise = [[A[0]] for _ in range(len(A))]
        backTrackFall = [[A[0]] for _ in range(len(A))]
        dpFallEnd[0] = dpRiseEnd[0] = 1
        for i in range(1, len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    if dpFallEnd[j] + 1 > dpRiseEnd[i]:
                        backTrackFall[j].append(A[i])
                        backTrackRise[i] = copy.deepcopy(backTrackFall[j])
                        backTrackFall[j].pop()
                    dpRiseEnd[i] = max(dpRiseEnd[i], dpFallEnd[j] + 1)
                if A[j] > A[i]:
                    if dpRiseEnd[j] + 1 > dpFallEnd[i]:
                        backTrackRise[j].append(A[i])
                        backTrackFall[i] = copy.deepcopy(backTrackRise[j])
                        backTrackRise[j].pop()
                    dpFallEnd[i] = max(dpFallEnd[i], dpRiseEnd[j] + 1)
        result =  backTrackRise[-1] if len(backTrackRise[-1]) >= len(backTrackFall[-1]) else backTrackFall[-1]
        sum = 0
        for x in result:
            sum+=x
        print(sum)
getLongestAlternatingSubsequenceDP([4,3,8,5,3,8])
def dijkstra(graph,src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src][i]  # 初始化
    # print(distance)
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance  # 进行距离更新
                    k=d
                    pre=v
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        print(visited,nodes)  # 输出节点的添加过程
    return distance,path
if __name__ == '__main__':


    a = 1;
    b = copy.copy(a)
    c = copy.deepcopy(a)
    print(id(a),id(b),id(c))