def is_object_in(dict_obj, key, val):

    ## If is dictionary get the values for the key
    ## if the valie is not string return false
    if hasattr(dict_obj, 'get'):
        value = dict_obj.get(key)
        if isinstance(value, str) == False:
            return False
    else:
        return False
    
    ## Check if the value is list or string and is lookup string we
    ## Are looking for. If yes return True if not retrun False
    if val in value:
        return True
    else:
        return False
