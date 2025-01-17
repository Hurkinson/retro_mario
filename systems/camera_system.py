

def camera_manager(player_x, player_y, screen_width, screen_height, background_width, background_height ):

    # Gérer le mouvement de la caméra (X)
    if player_x < screen_width // 2: 
        camera_x = 0
    elif player_x > background_width - screen_width // 2:  
        camera_x = background_width - screen_width
    else:
        camera_x = player_x - screen_width // 2  # Centrer la caméra sur le joueur par defaut

    # Gérer le mouvement de la caméra (Y)
    if player_y < screen_height // 2:  
        camera_y = 0
    elif player_y > background_height - screen_height // 2: 
        camera_y = background_height - screen_height
    else:
        camera_y = player_y - screen_height // 2  # Centrer la caméra sur le joueur par defaut

    adjusted_player_x = player_x - camera_x
    adjusted_player_y = player_y - camera_y + 30

    return camera_x, camera_y, adjusted_player_x, adjusted_player_y