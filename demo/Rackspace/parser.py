"""
Parsing input and creating parameters to look for
"""
from optparse import OptionParser

PARSER = OptionParser()
PARSER.add_option("-b", "--backup_server",
                  dest="backup_server",
                  type="str",
                  help="Find all servers backing up to this storage.")
PARSER.add_option("-o", "--object_type",
                  dest="object_type",
                  type="str",
                  help="Specify object type: Server or VM")
PARSER.add_option("-e", "--explicit_tags",
                  action="append",
                  dest="explicit_tags",
                  type="str",
                  help="--explicit_tags='managed, Dedicated Server, MSD-Level4'")
PARSER.add_option("-i", "--implicit_tags",
                  action="append",
                  dest="implicit_tags",
                  type="str",
                  help="--implicit_tags='Client Server, cPanel Server, paragon'")
(OPTIONS, ARGS) = PARSER.parse_args()

print("backup_server is %s" % OPTIONS.backup_server)
print("object_type is %s" % OPTIONS.object_type)
print("explicit_tags is %s" % OPTIONS.explicit_tags)
print("implicit_tags is %s" % OPTIONS.implicit_tags)
print("non-option argument list is %s" % str(ARGS))
