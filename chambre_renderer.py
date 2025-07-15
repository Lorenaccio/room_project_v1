import pygame
from shapely.geometry import Polygon, LineString
from config import *
from genetic_furniture import Furniture, genetic_place

def get_center_line(wall):
    (x1, y1), (x2, y2) = wall
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    if x1 == x2:
        return LineString([(x1 - 5, mid_y - 30), (x1 + 5, mid_y + 30)])
    else:
        return LineString([(mid_x - 30, y1 - 5), (mid_x + 30, y1 + 5)])

def draw_legend(screen, font):
    labels = [
        ("Mur", WALL_COLOR),
        ("Porte", DOOR_COLOR),
        ("Fenêtre", WINDOW_COLOR),
        ("Lit", FURNITURE_COLORS["lit"]),
        ("Armoire", FURNITURE_COLORS["armoire"]),
        ("Table", FURNITURE_COLORS["table"])
    ]
    x, y = 20, 60
    for label, color in labels:
        pygame.draw.rect(screen, color, (x, y, 20, 20))
        text = font.render(label, True, TEXT_COLOR)
        screen.blit(text, (x + 30, y + 2))
        y += 30

def render_chambre():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chambre optimisée")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)

    points_m = [(0,0), (4,0), (4,2), (6,2), (6,5), (0,5)]
    points_px = [(x*SCALE, y*SCALE) for x, y in points_m]
    offset_x = (WINDOW_WIDTH - max(x for x, y in points_px)) // 2
    offset_y = (WINDOW_HEIGHT - max(y for x, y in points_px)) // 2
    points_px = [(x+offset_x, y+offset_y) for x, y in points_px]
    polygon = Polygon(points_px)
    walls = list(zip(points_px, points_px[1:] + [points_px[0]]))

    door_wall = walls[0]
    window_wall = walls[-2]
    door_shape = get_center_line(door_wall).buffer(5)
    window_shape = get_center_line(window_wall).buffer(5)
    obstacles = [door_shape, window_shape]

    furniture_items = [
        Furniture("lit", int(0.9*SCALE), int(2.0*SCALE), FURNITURE_COLORS["lit"]),
        Furniture("armoire", int(1.0*SCALE), int(0.5*SCALE), FURNITURE_COLORS["armoire"]),
        Furniture("table", int(1.5*SCALE), int(0.7*SCALE), FURNITURE_COLORS["table"])
    ]

    total_score = 0
    for f in furniture_items:
        rect, score = genetic_place(f, polygon, obstacles, offset_x, offset_y)
        obstacles.append(polygon.intersection(Polygon([
            (rect[0], rect[1]),
            (rect[0]+rect[2], rect[1]),
            (rect[0]+rect[2], rect[1]+rect[3]),
            (rect[0], rect[1]+rect[3])
        ])))
        total_score += score

    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.polygon(screen, WALL_COLOR, points_px, 5)
        pygame.draw.line(screen, DOOR_COLOR, *get_center_line(door_wall).coords, 8)
        pygame.draw.line(screen, WINDOW_COLOR, *get_center_line(window_wall).coords, 8)

        for f in furniture_items:
            if f.rect:
                pygame.draw.rect(screen, f.color, pygame.Rect(*f.rect))

        score_text = font.render(f"Score total: {int(total_score)}", True, TEXT_COLOR)
        screen.blit(score_text, (20, 20))

        draw_legend(screen, font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
