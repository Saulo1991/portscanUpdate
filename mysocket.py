import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
    print('[+] Connection done')
except socket.error:
    print("[+] Error!")

msg = b'There you go'
sock.send(msg)