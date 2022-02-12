import random
import user_bot_gh


def near_gold(check, x, y, r):
    for dx in range(-r, r):
        for dy in range(-r, r):
            if check("gold", x + dx, y + dy):
                if dx > 0 and not check("wall", x + 1, y):
                    return "right"
                if dx < 0 and not check("wall", x - 1, y):
                    return "left"
                if dy > 0 and not check("wall", x, y + 1):
                    return "down"
                if dy < 0 and not check("wall", x, y - 1):
                    return "up"
    return "pass"


def far_wall(check, x, y):
    left = right = up = down = 1
    while True:
        if check("wall", x + right, y):
            break
        else:
            right += 1
    while True:
        if check("wall", x - left, y):
            break
        else:
            left += 1
    while True:
        if check("wall", x, y + down):
            break
        else:
            down += 1
    while True:
        if check("wall", x, y - up):
            break
        else:
            up += 1
    top = max(left, right, up, down)
    if top == right:
        return "right"
    if top == down:
        return "down"
    if top == left:
        return "left"
    if top == up:
        return "up"
    return "pass"


def line_gold(check, x, y):
    left = right = up = down = 1
    while True:
        if check("gold", x + right, y):
            break
        if check("wall", x + right, y):
            right = 9999
            break
        else:
            right += 1
    while True:
        if check("gold", x - left, y):
            break
        if check("wall", x - left, y):
            left = 9999
            break
        else:
            left += 1
    while True:
        if check("gold", x, y + down):
            break
        if check("wall", x, y + down):
            down = 9999
            break
        else:
            down += 1
    while True:
        if check("gold", x, y - up):
            break
        if check("wall", x, y - up):
            up = 9999
            break
        else:
            up += 1
    if left == right == up == down == 9999:
        return "pass"
    else:
        floor = min(left, right, up, down)
        if floor == right:
            return "right"
        if floor == down:
            return "down"
        if floor == left:
            return "left"
        if floor == up:
            return "up"
    return "pass"


def move_somewhere(check, x, y):
    if not check("wall", x + 1, y):
        return "right"
    if not check("wall", x, y + 1):
        return "down"
    if not check("wall", x - 1, y):
        return "left"
    if not check("wall", x, y - 1):
        return "up"
    return "pass"


def move_random(check, x, y):
    return random.choice(["left", "right", "up", "down"])


# doesn't work for shit
def pathfind_gold_step(check, x, y, r, dir, path):
    if r > 10:
        return False
    if check("gold", x, y):
        path.append(dir)
        return True
    if check("wall", x, y):
        return False
    if not dir == "left":
        if pathfind_gold_step(check, x + 1, y, r + 1, "right", path):
            path.append(dir)
            return True
    if not dir == "up":
        if pathfind_gold_step(check, x, y + 1, r + 1, "down", path):
            path.append(dir)
            return True
    if not dir == "right":
        if pathfind_gold_step(check, x - 1, y, r + 1, "left", path):
            path.append(dir)
            return True
    if not dir == "down":
        if pathfind_gold_step(check, x, y - 1, r + 1, "up", path):
            path.append(dir)
            return True
    return False


# nuclear option (failed)
def pathfind_gold(check, x, y):
    path = list()
    if pathfind_gold_step(check, x, y, 0, "", path):
        last = path.pop()
        if last == "":
            last = path.pop()
        return last
    return "pass"


class Coords:
    def __init__(self):
        self.x2 = -1
        self.y2 = -1
        self.x1 = -1
        self.y1 = -1
        self.ticks = 0
        self.wall = False

    def update(self, x, y):
        self.x2 = self.x1
        self.y2 = self.y1
        self.x1 = x
        self.y1 = y

    def stuttercheck(self, x, y):
        if self.x2 == -1 or self.y2 == -1 or self.x1 == -1 or self.y1 == -1:
            return False
        if self.x2 == x and self.y2 == y and (self.x1 != x or self.y1 != y):
            self.ticks = 10
            return True
        else:
            return False


coords = Coords()


def script(check, x, y):
    # on 4th level override the algorithm with Krutix's script cause mine fails. yikes.
    if check("level") == 4:
        return user_bot_gh.script(check, x, y)
    # obvious first step
    if check("gold", x, y):
        return "take"
    # trying to detect stutter
    if coords.ticks > 0:
        coords.update(x, y)
        coords.ticks -= 1
        if coords.wall:
            cmd = move_somewhere(check, x, y)
        else:
            cmd = far_wall(check, x, y)
        if coords.ticks == 0:
            coords.wall = not coords.wall
        if cmd != "pass":
            return cmd
    if coords.stuttercheck(x, y):
        return "right"
    coords.update(x, y)
    # checking for gold within 2 tiles
    cmd = near_gold(check, x, y, 2)
    if cmd != "pass":
        return cmd
    # checking for gold in straight line
    cmd = line_gold(check, x, y)
    if cmd != "pass":
        return cmd
    # checking for gold within 6 tiles
    cmd = near_gold(check, x, y, 6)
    if cmd != "pass":
        return cmd
    # going towards the farthest wall
    cmd = far_wall(check, x, y)
    if cmd != "pass":
        return cmd
    # if gold not found, random movement
    if check("level") == 3:
        cmd = move_somewhere(check, x, y)
    else:
        cmd = move_random(check, x, y)
    if cmd != "pass":
        return cmd
    # if all else fails
    return "pass"
