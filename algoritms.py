import time
from queue import PriorityQueue
from Node import Node
counter = [1, 1, 1]
def findTime(startTime, counter):
    result = time.time() - startTime
    if counter == 1:
        print(result)

def dfs1(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from

def dfs(graph, start, goal):
    startTime = time.time()
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))
    findTime(startTime, counter[0])
    counter[0] -= 1
    while not fringe.empty():

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



def bfs(graph, start, goal):
    startTime = time.time()

    queue = [start]
    parents = {start: None}
    while len(queue) != 0:
        current_coord = queue.pop(0)
        if current_coord == goal:
            findTime(startTime, counter[1])
            counter[1]-=1
            return get_path(parents, goal)

        for next in graph.neighbors(current_coord):
            if next not in parents:
                parents[next] = current_coord
                queue.append(next)


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


def alphabeta(node: Node, depth, a, b, maximizingPlayer, enemy, player):
    if depth == 0 or node.is_terminal:
        return  node.evaluation_function(enemy, player), node
    if maximizingPlayer:
        value = -float('inf')
        best_node = node
        for child in node.generate_children(player):
            alphaResult, alphaNode = alphabeta(child, depth - 1, a, b, True)
            if alphaResult > value:
                value = alphaResult
                best_node = child
            if value >= b:
                break  # (* b cutoff *)
            if value > a:
                a = value
        return (value, best_node)
    else:
        worst_node = node
        value = float('inf')

        for child in node.generate_children(player):
            alphaResult, alphaNode = alphabeta(child, depth - 1, a, b, False)
            if alphaResult < value:
                value = alphaResult
                worst_node = child
            if value <= a:
                break
            if value < b:
                b = value
        return (value, worst_node)


def expectiminimax(node: Node, depth, maximizingPlayer, player, enemy):
    if depth == 0 or node.is_terminal:
        return (node.evaluation_function(enemy, player), node)
    if maximizingPlayer:
        result = [expectiminimax(child, depth - 1, False) for child in node.generate_children(player)]
        alphaResult, alphaNode = max(result, key=lambda x: x[0], default=node)
        return (alphaResult / len(result), alphaNode)
    else:
        result = [expectiminimax(child, depth - 1, True) for child in node.generate_children(player)]
        alphaResult, alphaNode = min(result, key=lambda x: x[0], default=node)
        return (alphaResult / len(result), alphaNode)
