import socket
import subprocess

host = '127.0.0.1'
port = 9999

def receivedSender(c):
    received = c.recv(1024)
    process = subprocess.check_output(received.decode('utf-8'), shell=True, universal_newlines=True)
    c.sendall(process.encode('utf-8'))
    
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((host, port))
tcp_server.listen(1)
print(f'Listening at port {port}')

c, addr = tcp_server.accept()
print(f'Connection {addr[0]}:{addr[1]}')

while True:
    receivedSender(c)
    
    c.close()
    tcp_server.close()