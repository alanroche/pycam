import sys
print sys.argv

file_name = sys.argv[1]

with open(file_name, "r") as fileObj:
    for ( i, line ) in enumerate( fileObj):
        print "%s: %r" % ( i, len(line) )
