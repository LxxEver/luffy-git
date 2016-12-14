#!/usr/bin/env python

'create text file'

print '111111111111111'
import os

ls = os.linesep

print ls

print '111111111111111'
print

fname = "readmenow"

while True:

    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

all = []

print "\nEnter lines ('.' by itself to quit).\n"

while True:
    entry = raw_input('>')
    if entry == '.':
        break;
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()

print 'DONE!'


