import socket
import sys

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    print('Usage: python mysocket.py host port')
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
    print('[+] Connection done')
except socket.error:
    print("[+] Error!")

msg = b'There you go'
sock.send(msg)