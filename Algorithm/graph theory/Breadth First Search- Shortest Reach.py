def bfs(graph, start,dlength):
    visited, queue = set(), [start]
    distances = [-1] * dlength
    distances[int(start) -1]=0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for v in graph[vertex]:
                if distances[int(v)-1]==-1:
                    distances[int(v)-1]=distances[int(vertex)-1]+6
            queue.extend(graph[vertex] - visited)
    return distances
GraList=int(input())

for s in xrange(GraList):
    graph=dict()
    NM=map(int,raw_input().split())
    for k in xrange(NM[1]):
        tup = map(str,raw_input().split())
        graph.setdefault(tup[0],set()).add(tup[1])
        graph.setdefault(tup[1],set()).add(tup[0])

    for x in xrange(1,NM[0]+1):
        if str(x) not in graph.keys():
            graph.setdefault(str(x),set())

    startPoint=str(input())
    sol = [str(j) for j in bfs(graph,startPoint,NM[0]) if j !=0]
    print ' '.join(sol)
