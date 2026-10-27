'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
while mixer.music.get_busy():
    mixer.time.Clock().tick(10)