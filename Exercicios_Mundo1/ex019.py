import pygame

pygame.init()
pygame.mixer.music.load('ex019.mpeg')
pygame.mixer.music.play()
pygame.event.wait()
