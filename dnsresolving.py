import dns.resolver
import sys

record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
    domain = sys.argv[1]
except IndexError:
    print('Syntax Error - python script.py <domainname>')
    sys.exit()

for record in record_types:
    try:
        answer = dns.resolver.resolve(domain, record)
        print(f'\nRecord: {record}')
        print('-' * 30)
        for server in answer:
            print(server.to_text() + '\n')
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(f'Error retrieving {record} records: {e}')