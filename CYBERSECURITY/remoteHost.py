import socket
import sys

def portScanning(remote_host):
    try:
        for port in range(1, 254 + 1):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data = tcp_socket.connect_ex((remote_host, port))
            if data == 0:
                print(f'[+] Open {port}:::{socket.getservbyport(port)}')
    except socket.gaierror:
        print('[-] Remote host not found [-] ')
        exit()
    except socket.error:
        print('[-] Error while running socket [-]')
        exit()
    return

def main():
    if sys.argv[1] == '-h':
        print('python portscanning.py [host]')
    else:
        remote_host = sys.argv[1]
        portScanning(remote_host)
        
if __name__ == '__main__':
    main()