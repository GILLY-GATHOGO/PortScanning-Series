import socket

IP_ADDRESS = '192.168.0.104'

 #Socket Object
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    for port in range(100, 150):  # Scan the range of ports given
        try:
            s.connect((IP_ADDRESS, port))
            print(f'port{port} is open and listening')
        except:
            print(f'port {port} is closed')


