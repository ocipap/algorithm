graph = {}

def setGraph (m) :
    for _ in range(0, m):
        nodeA, nodeB = map(int, input().split())
        if not nodeA in graph :
            graph[nodeA] = set([])
        if not nodeB in graph : 
            graph[nodeB] = set([])

        graph[nodeA].add(nodeB)
        graph[nodeB].add(nodeA)

def bfs(start):
    if not start in graph :
        print(start)
        return
    visited = []
    temp = [start]
    while temp :
        n = temp.pop(0)
        if not n in visited :
            visited.append(n)
            temp.extend(sorted(list(graph[n] - set(visited))))
    visited = list(map(str, visited))    
    print(" ".join(visited))

def dfs(start):
    if not start in graph :
        print(start)
        return
    visited = []
    temp = [start]
    while temp :
        n = temp.pop()
        if not n in visited :
            visited.append(n)
            temp.extend(sorted(list(graph[n] - set(visited)), reverse=True))
    visited = list(map(str, visited))
    print(" ".join(visited))



def main () :
    n, m, v = map(int, input().split())
    setGraph(m)
    dfs(v)
    bfs(v)

main()

