import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import re
import sys
import configparser
import os.path

def get_request_url_data(auth_file, url):
    
    config_file = auth_file
    url_loc = url

    config = configparser.ConfigParser()
    try:
        config.read(config_file)
    except:
        print(f"Reading file {config_file} problem")
        sys.exit(2)
    
    password = config.get("myvars", "passwd");
    username = config.get("myvars", "username");

    try:
        r = requests.get(url, auth=(username, password))
    except:
        print(f"Error accessing {url}")
        sys.exit(3)
    
    if r.status_code != 200:
        print(f'Can not get to the URL {url}')
        sys.exit(4)
    
    ## Return r which is obtained from requests.
    return r
### end ########################################

def get_all_object_by_id(soup):

    urls = []
    exlude_list = ["CableOrganizer", "Organizer", "spacer", "PDU", "Shelf", "PatchPanel"]

    obj_base_url = "https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=object&tab=default&object_id="
    div = soup.find("div", {"class":"portlet"})
    table = div.find("table")
    rows = table.find_all("tr", {"class": ["row_odd", "row_even"]})
    for row in rows:
        tmp = str(re.findall(r'<strong>(.*?)</strong>', str(row.find_all('strong'))))
        if any (x in tmp for x in exlude_list): 
            continue
        # Sometime returns two list of two value, extract the first one
        obj_id = re.findall(r'object_id=([0-9]*)">', str(row))
        obj_id = str(obj_id[0].strip("[]'"))
        # obj_id = str(re.findall(r'object_id=([0-9]*)">', str(row))).strip("[]'")
        url = """%s%s""" % (obj_base_url, obj_id)
        urls.append(url)

    # Return list of objects url with object id to retrive information for each object 
    return urls

### end ########################################
def print_obj_dict(object_dict, obj_num):
    line = "=" * 50
    explisit_tags=object_dict.get('Explicit_tags')
    common_name = object_dict.get('Common_name')
    asset_tag = object_dict.get('Asset_tag')
    fqdn = object_dict.get('FQDN')

    s = """Object Num: %s\nFQDN: %s\nCommon name: %s\nExplisit tags: %s\nTag: %s """ \
     % ( obj_num, fqdn, common_name, explisit_tags, asset_tag)

    print(line)
    print(s)
    print(line)
### end ########################################
