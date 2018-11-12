"""" Print each key value pair for any dictionary!
     If obj_id provided print it as well!
"""

def print_obj_dict(object_dict, obj_id):
    """" Print each key value pair in dictionary!"""
    line = "=" * 50

        ## If object id is not zero print it  
    if int(obj_id) > 0:
        print(f'Object id: {obj_id}')

    if hasattr(object_dict, 'items'):
        for key, val in object_dict.items():
            print(f'{key}: {val}')
    
    print(line)
