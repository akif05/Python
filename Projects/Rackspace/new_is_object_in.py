"""
    Accepting dictionary with objects attributes
    and if key value exist return True else return false
"""

def is_object_in(dict_obj, key, val):

    """ Check object """
    ## If is dictionary get the values for the key
    ## if the valie is not string return false
    if hasattr(dict_obj, 'get'):
        value = dict_obj.get(key)
        if not isinstance(value, str):
            return False

    ## Check if the value is list or string and is lookup string we
    ## Are looking for. If yes return True if not retrun False
    return [val in value]
