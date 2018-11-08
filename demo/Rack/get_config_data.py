import configparser
import os.path

def get_config_data (config_file):

    d = dict();
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
    except:
        print(f"Reading file {config_file} problem")
        sys.exit(2)

    d['passwd'] = config.get("myvars", "passwd");
    d['username'] = config.get("myvars", "username");
    d['url'] = config.get("myvars", "url");
    d['base_url'] = config.get("myvars", "base_url");
    
    return d
