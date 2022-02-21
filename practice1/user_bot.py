import collections


# Data structure for use in BFS function
class Point:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir


# Breadth-First Search implementation for tile grid
def bfs(check, x, y):
    # set for storing visited tiles
    visited = set()
    visited.add(f"{x}, {y}")

    # queue for tiles to visit
    q = collections.deque()
    q.append(Point(x + 1, y, "right"))
    q.append(Point(x - 1, y, "left"))
    q.append(Point(x, y + 1, "down"))
    q.append(Point(x, y - 1, "up"))

    while q:
        # checking if tile was visited
        p = q.popleft()
        pos = f"{p.x}, {p.y}"
        if pos in visited:
            continue
        visited.add(pos)

        # other tile checks
        if check("wall", p.x, p.y):
            continue
        if check("gold", p.x, p.y):
            return p.dir

        # adding unvisited adjacent tiles to queue
        if f"{p.x + 1}, {p.y}" not in visited:
            q.append(Point(p.x + 1, p.y, p.dir))
        if f"{p.x - 1}, {p.y}" not in visited:
            q.append(Point(p.x - 1, p.y, p.dir))
        if f"{p.x}, {p.y + 1}" not in visited:
            q.append(Point(p.x, p.y + 1, p.dir))
        if f"{p.x}, {p.y - 1}" not in visited:
            q.append(Point(p.x, p.y - 1, p.dir))
    return "pass"


def script(check, x, y):
    if check("gold", x, y):
        return "take"
    return bfs(check, x, y)
