#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
from playsound3 import playsound
sound=playsound("D:/Macaco Produções/Makco/euvimveromakco/audio/Vinheta_halloween.mp3",block=False)
input('Aperte enter para desligar a música')
sound.stop()

