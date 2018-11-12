"""
Parsing input and creating parameters to look for
"""
def parser(parse_me):

    """ Parse arguments from command line"""

    dictionary = {"Backup_Server":None, "Object_type":None,
                  "Explicit_tags":None, "Implicit_tags":None}
    parse_me.add_argument("-b", "--backup_server",
                          required=False, action="store", dest="backup_server",
                          help="Find all servers backing up to this storage.",
                          default=None)
    parse_me.add_argument('-o', '--object_type',
                          required=False, action="store", dest="object_type",
                          help="Specify object type: Server or VM",
                          default=None)
    parse_me.add_argument("-e", "--explicit_tags",
                          required=False, action="append", dest="explicit_tags",
                          help="--explicit_tags='managed, Dedicated Server'",
                          default=None)
    parse_me.add_argument("-i", "--implicit_tags",
                          required=False, action="append", dest="implicit_tags",
                          help="--implicit_tags='Client Server, cPanel Server, paragon'",
                          default=None)
    args = parse_me.parse_args()
    dictionary["Backup_Server"] = args.backup_server
    dictionary["Object_type"] = args.object_type
    dictionary["Explicit_tags"] = args.explicit_tags
    dictionary["Implicit_tags"] = args.implicit_tags
    ## Retrun dictionary with no None values!
    res = {k:v for k, v in dictionary.items() if v is not None}
    return res
