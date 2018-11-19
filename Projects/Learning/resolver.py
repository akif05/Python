import socket
from timeit import timeit

class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()
    
    def has_host(self, host):
        return host in self._cache

#resolver = Resolver()
#resolver('dir.bg')
#print(resolver._cache)
#print(resolver.__call__('dir.bg'))
#
#resolver("pluralsight.com")
#print(resolver._cache)
#print(resolver.__call__('dir.bg'))
#
## timeit(setup="from __main__ import resolver", stmt="resolver('python.org')", number=1)
#
#
## t = timeit(setup="from __main__ import resolver", stmt="resolver('google.com')", number=1)
#print(t)
#t = timeit(setup="from __main__ import resolver", stmt="resolver('google.com')", number=1)
#print(t)
### print non scientific output
#print("{:f}".format(t))
#print("")
#print(resolver._cache)
#print(resolver.__call__('dir.bg'))
#
#print("\n\n")
#r = Resolver()
#print(r._cache)
#print(r.has_host("dir.bg"))
#
