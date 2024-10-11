import argparse
import socket
import ssl
from datetime import datetime

def certCheck(domain):
    try:
        daysAlert = 7
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.settimeout(5)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        issuer = dict(x[0] for x in cert['issuer'])
        issuedBy = issuer.get('organizationName', 'Unknown')
        notAfter = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        currentDate = datetime.now()
        daysRemaining = (notAfter - currentDate).days

        if daysRemaining < 0:
            certState = 'EXPIRED'
        elif daysRemaining <= daysAlert:
            certState = 'SOON'
        else:
            certState = 'OK'

        print(f"{domain} => Issuer: {issuedBy}, Valid until: {notAfter} State: [{certState}]")
    except Exception as e:
        print(f"{domain} => Error: {e}")

def checkDomainsList(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
        for domain in domains:
            domain = domain.strip()
            if domain:
                certCheck(domain)
    except Exception as e:
        print(f"Error opening file: {e}")

def checkMultipleDomains(domains):
    for domain in domains:
        certCheck(domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check domain or domains list SSL certificates')
    parser.add_argument('domains', type=str, nargs='*', help='Single domain to check SSL certificate or domains list separated by space')
    parser.add_argument('-f', '--file', type=str, help='File with domains list to check')
    
    args = parser.parse_args()
    
    if args.file:
        checkDomainsList(args.file)
    elif args.domains:
        checkMultipleDomains(args.domains)
    else:
        print("Error: you must specify domain or domains list file, please check available options with -h")

