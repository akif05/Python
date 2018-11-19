#def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
#    print (arg1)
#    print (arg2)
#    print (args)
#    print (kwarg1)
#    print (kwarg2)
#    print (kwarg3)
#print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg=8, kwarg4=9)

def print_args1(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11, 12, 13, 14)
print_args1(*t)

