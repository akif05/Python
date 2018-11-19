def noop(f):
    def noop_wrapper():
        return f()

    ## if we call hellp.__name__ will return 
    ## noop_wrapper without the next two lines
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    
    return noop_wrapper

@noop
def hello():
    """ Print a well-known message."""
    print("Hello, world")

# >>> from noop import hello
# >>> hello.__name__
# 'hello'
# >>> hello.__doc__
# ' Print a well-known message.'
# >>> help(hello)
