import socket

SERVER_IP = '192.168.0.109'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
    s.connect((SERVER_IP, SERVER_PORT))
    #   receive the massage and store in variable data
    data = s.recv(124)
    print(data)
input()
