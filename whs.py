import sys
from urllib.parse import urlsplit


def domains():
    #getting string with URL
    domain = str(sys.argv[1])
    #splitting url with urllib
    splited = urlsplit(domain)
    #getting xxx.yyy part from url
    if splited.netloc != '':
        domain = (splited.netloc)
    #converting to idn and deleting "b''" part from it
    domain = domain.encode("idna").decode("utf-8")
    print(domain)
