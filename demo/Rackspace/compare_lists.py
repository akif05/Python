""" Compare two lists element by element 
    list1 = ['VDS cPanel, managed, tsohost']
    list2 = ['managed, VDS cPanel, tsohost']
    After using split() Lists will look like:
    list2 = ['managed', 'VDS cPanel', 'tsohost']
"""
def compare_lists(list1, list2):

    # If one of the lists is emty return False
    if (
        len(list1) == 0
        or len(list2) == 0
        or None in list1
        or None in list2
    ):
        return False

    new1 = list1[0].split(', ')
    new2 = list2[0].split(', ')
    for item in new1:
        ## I item we gave from command line is in the objects 
        ## Properties, breack and check the next one in the list
        if str(item) not in new2:
            break

    ## If break didn't ocure meance that item of list 
    ## is not in second, the we return False which will
    ## Exlude the object 
    else:
        return True 
    return False           
