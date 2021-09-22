import time
counter = [1, 1, 1]
def findTime(startTime, counter):
    result = time.time() - startTime
    if counter == 1:
        print(result)


def dfs(graph, start, goal, asteroid_coords):
    startTime =time.time()
    stack = [start]
    path = []
    visited = []
    for i in range(8):
        for j in range(12):
            visited[i][j] = 1
    visited[start[0]][start[1]] = 1
    while len(stack)!=0:
        current_coord = stack.pop()
        visited[current_coord[1]][current_coord[0]] = 1
        for i in range(len(asteroid_coords)):
            if current_coord == asteroid_coords[i]:
                continue
        if current_coord == goal:
            findTime(startTime, counter[0])
            counter[0] += 1
            return path

        neighboring_nodes = graph[current_coord]
        for node in neighboring_nodes:
            stack.extend(node)
        if len(neighboring_nodes) == 0:
            stack.pop()
            path.pop



def bfs(graph, start, goal, asteroid_coords):
    startTime = time.time()

    queue = [start]
    parents = {start: None}
    while len(queue) != 0:
        current_coord = queue.pop(0)
        for i in range(len(asteroid_coords)):
            if current_coord == asteroid_coords[i]:
                continue

        if current_coord == goal:
            findTime(startTime, counter[1])
            counter[1]-=1
            return get_path(parents, goal)

        neighboring_nodes = graph[current_coord]

        for node in neighboring_nodes:
            if node not in parents:
                parents[node] = current_coord
                queue.append(node)


def ucs(graph, start, goal, asteroid_coords):
    startTime = time.time()
    queue = [start]
    parents = {start: None}
    while len(queue) != 0:
        current_coord = queue.pop(0)
        for i in range(len(asteroid_coords)):

            if current_coord == asteroid_coords[i]:
                continue

        if current_coord == goal:
            findTime(startTime, counter[2])
            counter[2] += 1
            return get_path(parents, goal)

        neighboring_nodes = graph[current_coord]

        for node in neighboring_nodes:
            if node not in parents:
                parents[node] = current_coord
                queue.append(node)

def get_path(parents, finish_coord):
    arr = []
    current = finish_coord
    while current != None:
        arr.insert(0, current)
        current = parents[current]

    return arr

