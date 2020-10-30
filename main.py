import pygame
import RPi.GPIO as GPIO
import time
import math
from time import sleep

pygame.init()

pygame.mixer.init()


GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 18 to be an input pin and set initial value to be pulled low (off)

_songs = ["1.ogg","2.ogg","3.ogg","4.ogg","5.ogg","6.ogg","7.ogg","8.ogg","9.ogg","10.ogg","11.ogg","12.ogg","13.ogg","14.ogg","15.ogg","16.ogg","17.ogg"]

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        play_next_song()
        print('Song Played')
        time.sleep(1)
    if GPIO.input(17) == False:
        pygame.mixer.music.stop()
