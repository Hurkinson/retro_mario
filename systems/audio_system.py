import pygame


def initialize_audio():
    pygame.mixer.init()

    pygame.mixer.music.load('assets/main_theme.mp3')  
    pygame.mixer.music.set_volume(0.3)  
    pygame.mixer.music.play(-1)  

    jump_sound = pygame.mixer.Sound('assets/jump_sfx.wav')  
    jump_sound.set_volume(0.6)

    sfx_bank = {
    "jump_sound": jump_sound

}

    return sfx_bank

def play_sound(sfx, sfx_bank):
    sfx_bank[sfx].play()