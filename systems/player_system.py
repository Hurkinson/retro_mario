
##### ETAPE 2,3 =====================================================

# import pygame

# def move_manager(keys, 
#                  player_x,
#                  player_speed, 
#                  player_width, 
#                  screen_width, 
#                  facing_right=False, 
#                  current_frame=0
#                  ):
    
#     if keys[pygame.K_LEFT]:
#         player_x -= player_speed
#         facing_right = False  # Le personnage fait face à gauche
#         current_frame = (current_frame + 1) % 6 # len(frames)
        
#     if keys[pygame.K_RIGHT]:
#         player_x += player_speed
#         facing_right = True  # Le personnage fait face à droite
#         current_frame = (current_frame + 1) % 6 # len(frames)
 
#     # Empêcher le personnage de sortir de l'écran
#     if player_x < 0:
#         player_x = 0
#     if player_x > screen_width - player_width:
#         player_x = screen_width - player_width

#     return player_x, facing_right, current_frame


##### ETAPE 4 ========================================================

# import pygame

# def move_manager(keys, 
#                  player_x,
#                  player_y, 
#                  player_speed, 
#                  player_width,
#                  player_height,
#                  jump_power,
#                  gravity, 
#                  screen_width,
#                  background_height,
#                  facing_right, 
#                  current_frame=0,
#                  player_velocity_x=0,
#                  player_velocity_y=0,
#                  player_state="land"):
    
    
    
#     # Gestion du mouvement latéral
#     if keys[pygame.K_LEFT]:
#         player_velocity_x = -player_speed
#         facing_right = False  
#         current_frame = (current_frame + 1) % 6  # Incrémenter la frame
#     elif keys[pygame.K_RIGHT]:
#         player_velocity_x = player_speed
#         facing_right = True  
#         current_frame = (current_frame + 1) % 6 # Incrémenter la frame
#     else:
#         player_velocity_x = 0

#     # Gestion du saut
#     if keys[pygame.K_UP] and player_state == "land":
#         player_velocity_y = jump_power  # Appliquer la vitesse initiale du saut
#         player_state = "air"

#     # Appliquer la gravité lorsque le joueur est en l'air
#     if player_state == "air":
#         player_velocity_y += gravity  # Ajouter la gravité à la vitesse verticale

#     # Limiter la vitesse de chute
#     if player_velocity_y > 15:  # Limiter la vitesse de chute à 15 pixels par frame
#         player_velocity_y = 15

#     # Déplacer le joueur
#     player_x += player_velocity_x
#     player_y += player_velocity_y

#     # Empêcher le personnage de sortir de l'écran
#     if player_x < 0:
#         player_x = 0
#     if player_x > screen_width - player_width:
#         player_x = screen_width - player_width

#     # Limiter le joueur aux bords de l'image de fond (Y)
#     if player_y < 0:
#         player_y = 0
#     if player_y > (background_height - 110) - player_height:
#         player_y = (background_height - 110) - player_height
#         player_state = "land"  
#         player_velocity_y = 0  

#     return player_x, player_y, player_velocity_y, facing_right, current_frame, player_state





##### ETAPE 5 =======================================================

import pygame
from systems.audio_system import play_sound


def move_manager(keys, 
                 player_x,
                 player_y, 
                 player_speed, 
                 player_width,
                 player_height,
                 jump_power,
                 gravity, 
                 background_width,
                 background_height,
                 facing_right,
                 sfx_bank, 
                 current_frame=0,
                 player_velocity_x=0,
                 player_velocity_y=0,
                 player_state="land"):
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        facing_right = False  # Le personnage fait face à gauche
        current_frame = (current_frame + 1) % 6 # len(frames)
        
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        facing_right = True  # Le personnage fait face à droite
        current_frame = (current_frame + 1) % 6 # len(frames)

    # Gestion du saut
    if keys[pygame.K_UP] and player_state == "land":
        play_sound("jump_sound", sfx_bank) 
        player_velocity_y = jump_power 
        player_state = "air"

    # Appliquer la gravité lorsque le joueur est en l'air
    if player_state == "air":
        player_velocity_y += gravity  

    # Limiter la vitesse de chute
    if player_velocity_y > 15:  # Limiter la vitesse de chute à 15 pixels par frame
        player_velocity_y = 15

    # Déplacer le joueur
    player_x += player_velocity_x
    player_y += player_velocity_y
 
    # Limiter le joueur aux bords de l'image de fond (X)
    if player_x < 0:
        player_x = 0
    if player_x > background_width - player_width:
        player_x = background_width - player_width

    # Limiter le joueur aux bords de l'image de fond (Y)
    if player_y < 0:
        player_y = 0
    if player_y > (background_height - 110) - player_height:
        player_y = (background_height - 110) - player_height
        player_state = "land"  
        player_velocity_y = 0 

    return player_x, player_y, player_velocity_y, facing_right, current_frame, player_state