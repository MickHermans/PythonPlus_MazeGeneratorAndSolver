from random import choice
import pygame

# pygame setup
resolution = width, height = 1302, 702
tile = 50
columns, rows = width // tile, height // tile

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


def check_cell(x, y):
    def find_index(x_coordinate, y_coordinate): return x_coordinate + y_coordinate * columns
    if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
        return False
    return grid_cells[find_index(x, y)]


class Cell:
    def __init__(self, x, y):
        self.grid_cells = None
        self.x, self.y = x, y
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.visited = False

    def draw_leading_cell(self):
        x, y = self.x * tile, self.y * tile
        pygame.draw.rect(screen, pygame.Color("red"), (x + 2, y + 2, tile - 2, tile - 2))

    def draw(self):
        x, y = self.x * tile, self.y * tile
        if self.visited:
            pygame.draw.rect(screen, pygame.Color("white"), (x, y, tile, tile))

        if self.walls["top"]:
            pygame.draw.line(screen, pygame.Color("black"), (x, y), (x + tile, y), 2)
        if self.walls["right"]:
            pygame.draw.line(screen, pygame.Color("black"), (x + tile, y), (x + tile, y + tile), 2)
        if self.walls["bottom"]:
            pygame.draw.line(screen, pygame.Color("black"), (x + tile, y + tile), (x, y + tile), 2)
        if self.walls["left"]:
            pygame.draw.line(screen, pygame.Color("black"), (x, y + tile), (x, y), 2)

    def check_neighbouring_cells(self, grid_tiles):
        self.grid_cells = grid_tiles
        neighbors = []
        top = check_cell(self.x, self.y - 1)
        right = check_cell(self.x + 1, self.y)
        bottom = check_cell(self.x, self.y + 1)
        left = check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False


def remove_walls_of_next_cell(current, next_wall):
    dx = current.x - next_wall.x
    if dx == 1:
        current.walls['left'] = False
        next_wall.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next_wall.walls['left'] = False
    dy = current.y - next_wall.y
    if dy == 1:
        current.walls['top'] = False
        next_wall.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next_wall.walls['top'] = False


grid_cells = [Cell(col, row) for row in range(rows) for col in range(columns)]
current_cell = grid_cells[0]
stack = []
colors, color = [], 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(pygame.Color("black"))

    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_leading_cell()

    next_cell = current_cell.check_neighbouring_cells(grid_cells)
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        colors.append((min(color, 255), 10, 100))
        color += 1
        remove_walls_of_next_cell(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()

    pygame.draw.rect(screen, pygame.Color("green"), (1250 + 2, 650 + 2, tile - 2, tile - 2))

    pygame.display.flip()
    clock.tick(1000)
