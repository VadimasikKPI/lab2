import time
from queue import PriorityQueue
counter = [1, 1, 1]
def findTime(startTime, counter):
    result = time.time() - startTime
    if counter == 1:
        print(result)


def dfs(graph, start, goal, asteroid_coords):
    startTime = time.time()
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))
    findTime(startTime, counter[0])
    counter[0] -= 1
    while not fringe.empty():

        depth, current_node, path, visited = fringe.get()
        for i in range(len(asteroid_coords)):
            if current_node == asteroid_coords[i]:
                continue
        if current_node == goal:

            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = graph[current_node]
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path + [node], visited))
    return path



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

