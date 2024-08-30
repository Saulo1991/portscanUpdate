import nmap

scanner = nmap.PortScanner()

alvo = input('Alvo: ')
port = input('Port: ')

scanner.scan(alvo, port)

for host in scanner.all_hosts():
    print('-' * 30)
    print('[+] Host: %s {%s}' % (host, scanner[host].hostname()))
    print('[+] State: %s' % (scanner[host].state()))
    print('-' * 30)
    for proto in scanner[host].all_protocols():
        print('[+] Protocol: %s' % proto)
        
        list_ports = list(scanner[host][proto].keys())
        list_ports.sort()
        for port in list_ports:
            print('[+] Port: %s \t State: %s' % (port, scanner[host][proto][port]['state']))
        