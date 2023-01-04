import socket

IP_ADDRESS = '192.168.0.109'
PORT = 139

#Socket Object......Scans TCP
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    try:

        s.connect((IP_ADDRESS, PORT))   #Tuple
        print(f'port {PORT} is open and listening')
    except:
        print(f'failed to Connect to {PORT}')
