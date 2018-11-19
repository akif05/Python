"""
Reading password and another configuragion from text file
file is in format:
[myvars]
username: my_username
passwd: my_password
"""
import configparser
import sys

def get_config_data(config_file):

    """ Reading data from file and returning dictionary"""

    d_conf = dict()
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
    except:
        print(f"Reading file {config_file} problem.")
        sys.exit(2)

    d_conf['passwd'] = config.get("myvars", "passwd")
    d_conf['username'] = config.get("myvars", "username")
    d_conf['url'] = config.get("myvars", "url")
    d_conf['base_url'] = config.get("myvars", "base_url")
    return d_conf
