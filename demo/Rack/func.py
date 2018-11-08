import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import re
import sys
import configparser
import os.path

def get_request_url_data(url, username, password):
    
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

def get_all_object_by_id(soup, obj_base_url):

    urls = []
    exlude_list = ["CableOrganizer", "Organizer", "spacer", "PDU", "Shelf", "PatchPanel"]

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
