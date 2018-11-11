"""
Parsing input and creating parameters to look for
"""
import argparse
import sys

def parser(PARSER):

    dictionary = {"Backup_Server":None, "Object_type":None, 
                  "Explicit_tags":None, "Implicit_tags":None}
    
    # PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-b", "--backup_server",
                        required=False, action="store", dest="backup_server",
                        help="Find all servers backing up to this storage.",
                        default=None)
    PARSER.add_argument('-o', '--object_type',
                        required=False, action="store", dest="object_type",
                        help="Specify object type: Server or VM",
                        default=None)
    PARSER.add_argument("-e", "--explicit_tags",
                        required=False, action="append", dest="explicit_tags",
                        help="--explicit_tags='managed, Dedicated Server'",
                        default=None)
    PARSER.add_argument("-i", "--implicit_tags",
                        required=False, action="append", dest="implicit_tags",
                        help="--implicit_tags='Client Server, cPanel Server, paragon'",
                        default=None)
    
    ARGS = PARSER.parse_args()
    dictionary["Backup_Server"] = ARGS.backup_server
    dictionary["Object_type"] = ARGS.object_type
    dictionary["Explicit_tags"] = ARGS.explicit_tags
    dictionary["Implicit_tags"] = ARGS.implicit_tags
    
    return dictionary
