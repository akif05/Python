#!/Users/akifyusein/.virtualenvs/Projects/bin/python

# help(sorted)
 
scientists = ['Marie Curie', 'Albert Einstain', 'Niel Bohr', 'Isaac Newton', 'Dimitri Mendeleev', 'Anton Lavoisier', 'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']

## Pssing lambda as key argument
## lambda acceptes single argument clled name
## and the body of lambda after ':' clles str.split() 
## Lambda in its self is an expression which results in a callable object
## We can see that binding name lambda 
# last_name = lambda name: name.split()[0]

""" The folowing lambda is working corectely """
# mysort = sorted(scientists, key=lambda name: name.split()[0])
# mysort = sorted(scientists, key=lambda name: name.split()[-1])
#print(mysort)

""" Folowing is working as lambda
    This is working exampel how to pass function to sorted
"""
def first_name(name):
    """Get first name"""
    # return name.split()[-1]
    return name.split()[0]

mysort = sorted(scientists, key=first_name)

print(mysort)

## def is a statement which defind a function and has a function binding to a name
## Regular function must have name
## Argument for functions are delimited by parantheses and separeted by commas

## Argument list for a lambda is terminated by a colon
## Zero of more arguments supported - zero argumetns -> lambda:
## Lambda can contain only expressinons NO STATEMENTS.
## No return statement is allowed in a lambda body
## Lambda cannot have docstrigs
## Lambda is an expressin which return a function object
## Lambdas are annonimous


