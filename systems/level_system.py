
## 3 layer

# -- background (no collision)

# -- midlayer (no collision)

# -- frontlayer (collisions)


# import pygame
# import sys

# # Initialiser pygame
# pygame.init()

# pygame.display.set_mode((1, 1)) 

# # Charger et découper les tiles
# def load_tileset(tileset_path, tile_width, tile_height, margin=1):

#     tileset_image = pygame.image.load(tileset_path).convert_alpha()
#     tileset_width, tileset_height = tileset_image.get_size()
#     columns = tileset_width // (tile_width + margin)
#     rows = tileset_height // (tile_height + margin)

#     tiles = []
#     for row in range(rows):
#         for col in range(columns):
#             x = col * (tile_width + margin)
#             y = row * (tile_height + margin)
#             tile = tileset_image.subsurface((x, y, tile_width, tile_height))
#             tiles.append(tile)
#     return tiles

# # Charger les tiles
# tiles = load_tileset(r'workshop_pygame_src\assets\overworld_tileset.png', 16, 16, margin=1)

# # Définir la taille de la fenêtre pour afficher les tiles
# screen_width = 400
# screen_height = 300
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Tileset Display")

# # Couleur de fond pour la fenêtre
# WHITE = (255, 255, 255)

# # Dimensions et positions des tiles
# tile_display_size = 40  # Taille de l'affichage pour chaque tile
# tiles_per_row = screen_width // tile_display_size



# # Boucle principale d'affichage
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(WHITE)

#     # Afficher chaque tile dans la fenêtre
#     for i, tile in enumerate(tiles):
#         x = (i % tiles_per_row) * tile_display_size
#         y = (i // tiles_per_row) * tile_display_size
    
#         # Redimensionner chaque tile à la taille d'affichage
#         tile_resized = pygame.transform.scale(tile, (tile_display_size, tile_display_size))
#         screen.blit(tile_resized, (x, y))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()

#=====================================

# import pygame
# import numpy as np

# # Initialiser Pygame
# pygame.init()

# # Définir les dimensions de la fenêtre et de l'arrière-plan
# screen_width, screen_height = 800, 600
# background_width, background_height = 6400, 1800

# # Créer la surface d'affichage et le fond bleu
# screen = pygame.display.set_mode((screen_width, screen_height))
# background = pygame.Surface((background_width, background_height))
# background.fill((107, 137, 246))

# # Initialiser un array 3D pour le canevas de tiles
# # Dimensions : (background_height // tile_height, background_width // tile_width, 1)
# # Ici, on suppose des tiles de 16x16 pixels
# tile_width, tile_height = 16, 16
# canvas = np.zeros((background_height // tile_height, background_width // tile_width), dtype=int)

# # Boucle pour afficher le fond
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # Blit le fond bleu sur la fenêtre
#     screen.blit(background, (0, 0))
    
#     pygame.display.flip()

# pygame.quit()



# ==============================

