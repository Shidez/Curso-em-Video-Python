import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("SDBIMB.mp3")
pygame.mixer.music.play()
pygame.event.wait()
