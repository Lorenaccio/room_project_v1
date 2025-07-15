import random
from shapely.geometry import box

class Furniture:
    def __init__(self, name, width, height, color):
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.rect = None

def fitness(candidate, polygon, obstacles):
    x, y, w, h = candidate
    rect = box(x, y, x + w, y + h)
    if not polygon.contains(rect):
        return -1000
    for obs in obstacles:
        if rect.intersects(obs):
            return -500
    return 1000 - (abs(x) + abs(y))

def genetic_place(furniture, polygon, obstacles, offset_x, offset_y):
    population_size = 30
    generations = 40
    candidates = []

    for _ in range(population_size):
        x = random.randint(offset_x, offset_x + 500)
        y = random.randint(offset_y, offset_y + 300)
        candidates.append((x, y, furniture.width, furniture.height))

    for _ in range(generations):
        scored = [(fitness(c, polygon, obstacles), c) for c in candidates]
        scored.sort(reverse=True)
        top = [c for score, c in scored[:10]]

        new_candidates = top.copy()
        while len(new_candidates) < population_size:
            parent = random.choice(top)
            dx = random.randint(-20, 20)
            dy = random.randint(-20, 20)
            new_x = max(offset_x, parent[0] + dx)
            new_y = max(offset_y, parent[1] + dy)
            new_candidates.append((new_x, new_y, parent[2], parent[3]))

        candidates = new_candidates

    best = max(candidates, key=lambda c: fitness(c, polygon, obstacles))
    furniture.rect = best
    return best, fitness(best, polygon, obstacles)
