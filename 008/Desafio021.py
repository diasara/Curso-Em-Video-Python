# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3') # Entre àspas o nome real do arquivo. 
pygame.mixer.music.play('ex021.mp3')
pygame.event.wait()