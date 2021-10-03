import collections

class Graph:
    def __init__(self):
        self.edges = {}
        self.weight = {}

    def neighbors(self, id):
        return self.edges[id]

    def cost(self, from_node, to_node):
        return self.weight.get(to_node, 1)

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

