"""
Parsing input and creating parameters to look for
"""
import argparse
import sys

PARSER = argparse.ArgumentParser()
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
if ARGS.backup_server:
    print(ARGS.backup_server)
elif ARGS.object_type:
    print(ARGS.object_type)
elif ARGS.explicit_tags:
    print(ARGS.explicit_tags)
elif ARGS.implicit_tags:
    print(ARGS.implicit_tags)
else:
    PARSER.print_help()

