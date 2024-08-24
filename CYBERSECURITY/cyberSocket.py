import socket

ports = [21, 23, 80, 443, 8080]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex(('127.0.0.1', port))
    if code == 0:
        print(f'Port: {port} open')
    else:
        print(f'Port: {port} closed')