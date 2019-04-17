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
    visited = []
    temp = [start]
    print("----------")
    while temp :
        print(temp)
        n = temp.pop(0)
        if not n in visited :
            visited.append(n)
            temp.extend(list(graph[n] - set(visited)))
    visited = list(map(str, visited))    
    print("----------")

    print(" ".join(visited))

def dfs(start):
    visited = []
    temp = [start]

    while temp :
        n = temp.pop(0)
        if not n in visited :
            visited.append(n)
            temp = list(graph[n] - set(visited))
    visited = list(map(str, visited))
    print(" ".join(visited))


def main () :
    n, m, v = map(int, input().split())
    setGraph(m)
    print(graph)
    dfs(v)
    bfs(v)

main()

