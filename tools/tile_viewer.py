import pygame
import sys

pygame.init()
pygame.display.set_mode((1, 1)) 


def load_tileset(tileset_path, tile_width, tile_height, margin=1):

    tileset_image = pygame.image.load(tileset_path).convert_alpha()
    tileset_width, tileset_height = tileset_image.get_size()
    columns = tileset_width // (tile_width + margin)
    rows = tileset_height // (tile_height + margin)

    tiles = []
    for row in range(rows):
        for col in range(columns):
            x = col * (tile_width + margin)
            y = row * (tile_height + margin)
            tile = tileset_image.subsurface((x, y, tile_width, tile_height))
            tiles.append(tile)
    return tiles


tiles = load_tileset(r'workshop_pygame_src\assets\overworld_tileset.png', 16, 16, margin=1)

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tile Viewer")


WHITE = (255, 255, 255)


tile_display_size = 100  
current_tile_index = 0

font = pygame.font.Font(None, 36)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_RIGHT:
                current_tile_index = (current_tile_index + 1) % len(tiles)
            elif event.key == pygame.K_LEFT:
                current_tile_index = (current_tile_index - 1) % len(tiles)

    screen.fill(WHITE)

    tile = tiles[current_tile_index]
    tile_resized = pygame.transform.scale(tile, (tile_display_size, tile_display_size))
    tile_x = (screen_width - tile_display_size) // 2
    tile_y = (screen_height - tile_display_size) // 2
    screen.blit(tile_resized, (tile_x, tile_y))

    index_text = font.render(f"Tile Index: {current_tile_index}", True, (0, 0, 0))
    text_x = (screen_width - index_text.get_width()) // 2
    text_y = tile_y + tile_display_size + 10
    screen.blit(index_text, (text_x, text_y))

    pygame.display.flip()

pygame.quit()
sys.exit()
