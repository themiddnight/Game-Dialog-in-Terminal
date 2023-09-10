import pygame
import time
import os
import sys

pygame.init()

bgMusicFile = "cavern.mid"
dialogFile = "dialog.mp3"

pygame.mixer.init()
pygame.mixer.music.load(bgMusicFile)
pygame.mixer.music.play(-1)

dialogSound = pygame.mixer.Sound(dialogFile)

os.system("clear")

text1 = "Once up on a time, in the wooden land."
text2 = "There is a man who urges to rules the world..."
text3 = "for his family's sake..."
text4 = "...for good."

def printDialogs(texts, wait=True):
    def printDialog(str):
        tx = ""
        for char in str:
            tx += char
            print("\r", end="")         # clear current line
            print(" " + tx, end="")
            dialogSound.play()
            time.sleep(0.03)
        if wait == True: 
            input("\nPress Enter...")
            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[K")  # Clear line
            time.sleep(0.3)
        else:
            print()
            time.sleep(0.5)
    if type(texts) == list:
        for text in texts:
            printDialog(str=text)
    else:
        printDialog(texts)

time.sleep(1)
printDialogs("We are here.")
printDialogs([text1, text2, text3, text4])

pygame.mixer.music.fadeout(1000)
time.sleep(1)

pygame.quit()
