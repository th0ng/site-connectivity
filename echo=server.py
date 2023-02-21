# echo-server.py

import socket

HOST = "10.5.2.71" #Standard loopback interface address
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCKET_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
