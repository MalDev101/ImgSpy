import socket
import tqdm
import os
import atexit

#--------------------------
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
#--------------------------

BUFFER_SIZE = 4096
SEPARATOR = "<----->"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(8)

def quit():
    s.close()

atexit.register(quit)

def atconnection():
    print(f"[!] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    client_socket.close()

while True:
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept()

    atconnection()
