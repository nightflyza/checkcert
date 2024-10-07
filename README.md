# Domain SSL Certificate Checker

Simple Python script to check the SSL certificate expiration date for one or multiple domains.

## Requirements

- Python 3.x
- Required modules: `argparse`, `socket`, `ssl`, `datetime`

## Usage

### Check a Single Domain or Multiple Domains

You can check the SSL certificates for single domain or multiple domains directly by passing them as arguments:

```bash
python checkcert.py example.com
```

To check multiple domains:
```bash
python checkcert.py google.com github.com
````

### Check Domains from a domain list File

To check domains listed in a file, where each domain is on a new line:

```bash
python checkcert.py -f domains.txt
```

## Options
 - `domains`: A space-separated list of domains to check.
 - `-f, --file`: Specify a file that contains a list of domains, one per line.


## Output 

For each domain, the script will display:
   - Issuer: The organization that issued the SSL certificate.
   - Valid until: The expiration date of the certificate.

something like this
```bash
$ python checkcert.py google.com github.com
google.com => Issuer: Google Trust Services, Valid until: 2024-12-09 08:55:47
github.com => Issuer: Sectigo Limited, Valid until: 2025-03-07 23:59:59
```