import time
from queue import Queue

def dfs(graph, start, goal):
    visited = []
    path = []
    fringe = []
    fringe.append((0, start, path, visited))

    while not len(fringe)!=0:
        depth, current_node, path, visited = fringe.get()

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

def bfs(matrix, start_coord, finish_coord):

    queue = [start_coord]
    parents = {start_coord: None}
    while len(queue) != 0:
        current_coord = queue.pop(0)
        if current_coord == finish_coord:
            return get_path(parents, finish_coord)

        neighboring_nodes = matrix[current_coord]

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