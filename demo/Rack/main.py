import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import re
import sys
import configparser
import os.path
import time
from func import *
from get_objects_info import *
from is_object_in import *
from print_obj_dict import print_obj_dict
from get_config_data import get_config_data

def main():

    line = "=" * 50
    explisit_tag = "available stock"
<<<<<<< HEAD
    config_file = "/Users/akifyusein/.my_a_pass"
    req = get_request_url_data(config_file)
=======
   
    ## check if file exist if not exit!
    config_file = "/Users/akifyusein/.my_a_pass"
>>>>>>> woking_print
    
    # Get dictionary with config variables for auth and urls
    d = get_config_data (config_file) 

    # s = """Passwd: %s\nUsername: %s\nUrl: %s\nBase_url: %s\n""" % (d['passwd'], d['username'], d['url'], d['base_url'])
    # print(s)
    # sys.exit(1)
    
    req = get_request_url_data(d['url'], d['username'], d['passwd'])
    soup = BeautifulSoup(req.text, 'lxml')

    # Create urls for all objects except PDU and cable organizer
    urls = get_all_object_by_id(soup, d['base_url'])
    soup = ""
    # From each url in list get data and find objects with explisit tag Shared cPanel
    i = 0
    for url in urls:
        i += 1
<<<<<<< HEAD
        if i > 6:
=======
        if i > 10:
>>>>>>> woking_print
            sys.exit(3)
        
        try:
            req = get_request_url_data(url, d['username'], d['passwd'])
        except:
            print(f'Can not retrive: {url}')
            continue
        soup = BeautifulSoup(req.text, 'lxml')
        obj_dict = get_objects_info(soup)

        ## Get the key and lookup from command line!
        key = 'Explicit_tags'
        lookup = 'managed'
        # lookup = 'available stock'
        flag = is_object_in(obj_dict, key, lookup)

        if flag == True:
            # Get the object num form url and print out for user info.
            object_number = str(re.findall(r'object_id=([0-9]*)', url)).strip("[]'") 
            print_obj_dict(obj_dict, object_number)
        else:
            continue
 
if __name__ == '__main__':
    main()

<<<<<<< HEAD
## Hypervisor: Yes
## Common name: hvhost-008
## Contains: [ list of vms.......]
## Object type: Server
## Explicit tags: Tanium
## Asset tag:
## Create help giving info which key value needes to be provided
=======
>>>>>>> woking_print
