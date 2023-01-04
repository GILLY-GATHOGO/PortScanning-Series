
import socket
import threading
import queue

IP_ADDRESS = '192.168.0.104'
# Queue Object containing all the port numbers that we wanna scan
q = queue.Queue()

# Store port numbers in our Queue...It will grab port 1 -1000
for i in range(1, 1001):
    q.put(i)       # Put port elements inside the Queue

# Scan function from which al threads will run
def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((IP_ADDRESS, port))
                print(f'port{port} is open')
            except:
                pass
        q.task_done()

#  Number of threads we want to use
for i in range(30):
    t = threading.Thread(target=scan, daemon=True)  # call Scan Function.
    t.start()

q.join()
print(f'Finished')



