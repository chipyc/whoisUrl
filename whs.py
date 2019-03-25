import sys
from urllib.parse import urlsplit



def domains():
    domain = str(sys.argv[1])
    splited = urlsplit(domain)
    if splited.netloc != '':
        domain = (splited.netloc)
    domain = domain.encode("idna").decode("utf-8")
    print(domain)


