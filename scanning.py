import nmap

scanner = nmap.PortScanner()

target = input("Target: ")
port = input("Port: ")

scanner.scan(target, port)

for host in scanner.all_hosts():
    print("==================")
    print("[+] Host: %s {%s}" % (host, scanner[host].hostname()))
    print('[+] State: %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('=================')
        print('[+] Protocol: %s' % proto)
        
        lport = list(scanner[host][proto].keys())
        lport.sort()
        for port in lport:
            print('[+] Port: %s \t State: %s' % (port, scanner[host][proto][port]['state']))