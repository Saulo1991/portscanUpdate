import nmap

name = nmap.PortScanner()

target = input("Target: ")
port = input("Port: ")

name.scan(target, port)

for host in name.all_hosts():
    print("==================")
    print("[+] Host: %s {%s}" % (host, name[host].hostname()))
    print('[+] State: %s' % name[host].state())
    for proto in name[host].all_protocols():
        print('=================')
        print('[+] Protocol: %s' % proto)
        
        lport = list(name[host][proto].keys())
        lport.sort()
        for port in lport:
            print('[+] Port: %s \t State: %s' % (port, name[host][proto][port]['state']))
