#! /Users/akifyusein/.virtualenvs/demo/bin/python
""" Main function """

import sys
import os
import os.path
import re
import argparse
from parser import parser
from bs4 import BeautifulSoup
from func import get_request_url_data
from func import get_all_object_by_id
from get_objects_info import get_objects_info
from is_object_in import is_object_in
from print_obj_dict import print_obj_dict
from get_config_data import get_config_data

## This is main funciton
def main():

    """" Create dict with all available tags and create help function to give info
    Expect list of key value pairs form command line!
    explisit_tag = "available stock"
    Check if file exist and is accessable!
    """
    flag = False
    parse = argparse.ArgumentParser()

    ## If no any argumet passed print help and exit
    if len(sys.argv) < 2:
        parse.print_help()
        sys.exit(1)

    dic_cl_args = parser(parse)
    print("Retriving objects with flowing details: ")
    print_obj_dict(dic_cl_args, 0)

    config_file = "/Users/akifyusein/.my_a_pass"
    if not (os.path.isfile(config_file) and os.access(config_file, os.R_OK)):
        print(f'File: {config_file} not found, or not accesable.')
        sys.exit(1)

    # Get dictionary with config variables for auth and urls
    dic_conf = get_config_data(config_file)
    print(f"Retriving data: {dic_conf['url']}")
    req = get_request_url_data(dic_conf['url'], dic_conf['username'], dic_conf['passwd'])
    soup = BeautifulSoup(req.text, 'lxml')

    # Create urls for all objects except PDU and cable organizer
    urls = get_all_object_by_id(soup, dic_conf['base_url'])

    # Working lamda for sorting
    # str1='https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=object&tab=default&object_id=18'
    # int(re.search(r'object_id=([0-9]*)', str1).group(1))   ## this is working
    # urls.sort(key=lambda x: int(re.search(r'object_id=([0-9]*)', x).group(1)), reverse=False)

    soup = ""
    i = 0 
    # From each url in list get data and find objects with explisit tag Shared cPanel
    for url in urls:
        try:
            print(f"Retriving data: {url}")
            req = get_request_url_data(url, dic_conf['username'], dic_conf['passwd'])
        except:
            print(f'Can not retrive: {url}')
            continue
        soup = BeautifulSoup(req.text, 'lxml')
        obj_dict = get_objects_info(soup)
        for cl_key, cl_value in dic_cl_args.items():
            ## Check against the key value read from command line!
            flag = is_object_in(obj_dict, cl_key, cl_value)
            if not flag:
                break
        if flag:
            # Get the object num form url and print out for user info.
            object_number = str(re.findall(r'object_id=([0-9]*)', url)).strip("[]'")
            print_obj_dict(obj_dict, object_number)
        else:
            continue

if __name__ == '__main__':
    main()
