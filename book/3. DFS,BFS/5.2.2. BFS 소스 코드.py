from collections import deque과의

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


#bfs(graph, 1, visited)
