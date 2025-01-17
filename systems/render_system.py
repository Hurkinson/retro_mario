import pygame 

def render_manager(background, screen, facing_right, camera_x, camera_y, frames, current_frame, adjusted_player_x, adjusted_player_y):

    screen.blit(background, (-camera_x, -camera_y))

    # Si le joueur fait face à droite, retourner la sprite
    if facing_right:
        flipped_frame = pygame.transform.flip(frames[current_frame], True, False)  # True = flip horizontal
        screen.blit(flipped_frame, (adjusted_player_x, adjusted_player_y))
    else:
        screen.blit(frames[current_frame], (adjusted_player_x, adjusted_player_y))

    
    return pygame.display.flip()
