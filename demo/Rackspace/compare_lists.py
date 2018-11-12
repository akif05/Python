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
        for item2 in new2:
            if str(item) == str(item2):
                break
        else:
            return False
    return True            
