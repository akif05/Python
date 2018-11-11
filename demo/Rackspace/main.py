#! /Users/akifyusein/.virtualenvs/demo/bin/python
""" Main function """

import sys
import os
import os.path
import re
import argparse
from bs4 import BeautifulSoup
from func import get_request_url_data
from func import get_all_object_by_id
from get_objects_info import get_objects_info
from is_object_in import is_object_in
from print_obj_dict import print_obj_dict
from get_config_data import get_config_data
from new_parser import parser

## This is main funciton
def main():

    """" Create dict with all available tags and create help function to give info
    Expect list of key value pairs form command line!
    explisit_tag = "available stock"
    Check if file exist and is accessable!
    """
    PARSER = argparse.ArgumentParser()
    command_line_args =  parser(PARSER)
    print(command_line_args)
    sys.exit()



    config_file = "/Users/akifyusein/.my_a_pass"
    if not (os.path.isfile(config_file) and os.access(config_file, os.R_OK)):
        print(f'File: {config_file} not found, or not accesable.')
        sys.exit(1)

    # Get dictionary with config variables for auth and urls
    dic_conf = get_config_data(config_file)

    req = get_request_url_data(dic_conf['url'], dic_conf['username'], dic_conf['passwd'])
    soup = BeautifulSoup(req.text, 'lxml')

    # Create urls for all objects except PDU and cable organizer
    urls = get_all_object_by_id(soup, dic_conf['base_url'])
    soup = ""
    # From each url in list get data and find objects with explisit tag Shared cPanel
    i = 0
    for url in urls:
        i += 1
        if i > 6:
            sys.exit(3)
        try:
            req = get_request_url_data(url, dic_conf['username'], dic_conf['passwd'])
        except:
            print(f'Can not retrive: {url}')
            continue
        soup = BeautifulSoup(req.text, 'lxml')
        obj_dict = get_objects_info(soup)

        ## Get the key and lookup from command line!
        key = 'Explicit_tags'
        value = 'managed'
        # value = "available stock"

        # Check if key value find in obj_dict, which has all info for the object
        # if find print the object, else continue with next object
        flag = is_object_in(obj_dict, key, value)

        if flag:
            # Get the object num form url and print out for user info.
            object_number = str(re.findall(r'object_id=([0-9]*)', url)).strip("[]'")
            print_obj_dict(obj_dict, object_number)
        else:
            continue
if __name__ == '__main__':
    main()
