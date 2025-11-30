import os
import time
import keyboard
x = int("\x31\x36")
y = int("\x35")
while True:
    for i in range(y):
        print('%' * x)
    time.sleep(0.16)
    
    if keyboard.is_pressed("\x77"): y-=1
    if keyboard.is_pressed("\x73"): y+=1
    if keyboard.is_pressed("\x61"): x-=1
    if keyboard.is_pressed("\x64"): x+=1
    os.system("clear")
