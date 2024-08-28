import dns.resolver
import sys

try:
    domain = sys.argv[1]
    file = sys.argv[2]
except IndexError:
    print('Usage: python kkk.py <domainname> <filename>')
    sys.exit(1)

try:
    with open(file) as filex:
        lines = filex.read().splitlines()
except FileNotFoundError:
    print(f'{file} does not exist')
    sys.exit(1)
    
record_types = ['A', 'AAAA', 'NS', 'CNAME', 'PTR', 'TXT', 'SOA']
for record in record_types:
    print(f'Record: {record}')

for line in lines:
    subdomain = line + '.' + domain
    print(f'Subdomain: {subdomain}')
    try:
        responses = dns.resolver.resolve(subdomain, record)
        print(responses)
        for result in responses:
            print(subdomain, result)
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass
    except KeyboardInterrupt:
        print(f'ctrl + C not allowed')
    except Exception as e:
        print(f'Error: {e}')