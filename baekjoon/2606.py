computer = int(input())
graph = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    if not a in graph:
        graph[a] = set([])
    if not b in graph:
        graph[b] = set([])
    graph[a].add(b)
    graph[b].add(a)
    

count = 0
queue = [1]
already = []
while queue :
    now = queue.pop(0)
    if not now in already:
        count += 1
        already.append(now)
        if now in graph:
            queue.extend(list(graph[now] - set(already)))
print(count-1)

