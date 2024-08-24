import sys
import dns.resolver

#python dnsbrute.py youtube.com wordlistdominios.txt
arguments = sys.argv
try:
    domain = arguments[1]
    listing = arguments[2]
except IndexError:
    print("It's required arguments")
    sys.exit(1)
    
try:
    with open(listing) as file:
        lines = file.read().splitlines()
except FileNotFoundError:
    print('File not found or invalid')
    sys.exit(1)
    
for line in lines:
    subdomain = line + '.' + domain
    try:
        responses = dns.resolver.resolve(subdomain, 'A')
        for result in responses:
            print(subdomain, result)
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
