## Print each key value pair in dictionary!
def print_obj_dict(object_dict, obj_id):

    line = "=" * 50
    print(line)
    print(f'Object id: {obj_id}')
    
    if hasattr(object_dict, 'items'):    
        for key, val in object_dict.items():
            print(f'{key}: {val}')

