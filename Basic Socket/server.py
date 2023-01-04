import socket

SERVER_IP ='192.168.0.109'
SERVER_PORT= 5678

#use socket object and reference it using variable s
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    #bind the socket to the ip address and the port number
    s.bind((SERVER_IP,SERVER_PORT))
    print(f'Server Listening...')
    #Tell the server to listen for connections from the client. one connection at a time.
    s.listen(1)  #The server won't execute anything below this code until it gets a connection
    #Once the server gets a connection,it runs this.....which returns the conn and the address of the client
    conn,addr=s.accept()
    print(f'Connection Established from{addr}')

    #Use the conn object the send data back and forth with the client
    with conn:
        while True:
            conn.send(b'Hello world')   #While there is a connection, the server sends hello world in binary thats why b'
            #close the program
            break




