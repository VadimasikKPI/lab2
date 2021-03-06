
from queue import PriorityQueue

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
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
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        if came_from[current] == (125, 125):
            continue
        else:
            current = came_from[current]
        path.append(current)

    path.reverse()
    return path

def findWayToEnemy(path, num):
    temp = 100
    lendth ={ 0:100, 1:100, 2:100, 3:100}
    index = 0
    for i in range(num):

        if len(path[i]) <= temp:
            lendth[i] = len(path[i])
            temp = len(path[i])
            index = i
        else:
            continue

    return index