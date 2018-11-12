"""
    Accepting dictionary with objects attributes
    and if key obj_vlaues exist return True else return false
"""
from compare_lists import compare_lists

def is_object_in(dict_obj, key, cl_val):

    """ Check object """
    ## If is dictionary get the obj_vlauess for the key
    ## if the if object is not dictionary or 
    ## key obj_vlaues is not string return false
    # return True
    if hasattr(dict_obj, 'get'):
        ## if val we are lookin for is a list, then convet obj_vlaues to list as well
        if isinstance(cl_val, list):
            obj_vlaues = [dict_obj.get(key)]

            ## if dictionary returns None which meance no emlement found
            if None in obj_vlaues:
                return False
        else:
            obj_vlaues = dict_obj.get(key)

    ## Check if the obj_vlaues is list or string and is lookup string we
    ## Are looking for. If yes return True if not retrun False
    #breakpoint()
    
    ## If val is a list then check for each element in list
    ## that is present in the list of the objects properties, 
    if isinstance(cl_val, list):
        flag = compare_lists(cl_val, obj_vlaues)
        return flag 
    else:
        ## if val in obj_vlaues will return True, if not False
        return cl_val in obj_vlaues
