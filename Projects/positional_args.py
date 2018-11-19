
def hypervol(*args):
    print(args)
    print(type(args))

hypervol(3, 4)
hypervol(3, 4, 5)

def hypervol1(*lenghts):
    i = iter(lenghts)
    v = next(i)
    for lenghts in i:
        v *= lenghts
    return v

hypervol1(2, 4)
hypervol1(2, 4, 5)
hypervol1(2, 4, 5, 8)
hypervol1(2)



def hypervol2(length, *lenghts):
    v = length
    for item in lenghts:
        v *= item
    return v

hypervol2(2, 4)
hypervol2(2, 4, 5)
hypervol2(2, 4, 5, 8)
hypervol2(2)
hypervol2()
