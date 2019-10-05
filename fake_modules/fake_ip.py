import random
import string


def _ip():

    return '{}.{}.{}.{}'.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))

def ip(n=1):
    
    s = []
    for  i in range(n):
        s.append(_ip())

    if n == 1:
        return s[0]
    else:
        return s
