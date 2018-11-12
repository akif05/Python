"""
    Accepting dictionary with objects attributes
    and if key value exist return True else return false
"""
from compare_lists import compare_lists

def is_object_in(dict_obj, key, val):

    """ Check object """
    ## If is dictionary get the values for the key
    ## if the if object is not dictionary or 
    ## key value is not string return false
    if hasattr(dict_obj, 'get'):
        ## if val we are lookin for is a list, then convet value to list as well
        if isinstance(val, list):
            value = [dict_obj.get(key)]

            ## if dictionary returns None which meance no emlement found
            if None in value:
                return False
        else:
            value = dict_obj.get(key)

        #if not isinstance(value, str):
        #return False

    ## Check if the value is list or string and is lookup string we
    ## Are looking for. If yes return True if not retrun False
    #breakpoint()
    
    ## If val is a list then check for subset, if not check for tring in string
    ## myset is not zero if val na value have not same value iside the list
    ## Tried with sort but is not working!
    if isinstance(val, list):
        flag = compare_lists(val, value)
        return flag 
    else:
        return val in value
