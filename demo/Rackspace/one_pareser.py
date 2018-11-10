from optparse import OptionParser

parser = OptionParser()
parser.add_option("--group",
                  action="append",
                  dest="my_groups")
(options, args) = parser.parse_args()
print options.my_groups
