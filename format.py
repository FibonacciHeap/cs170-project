import os
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

if len(sys.argv) < 2:
    raise ValueError
path = sys.argv[1]
# print path
for filename in os.listdir(path):
    with open(path + '/' + filename , 'r+') as file:
        contents = file.read()
        # print 'contents: ', contents
        arr = (find_between(contents, '[', ']')[1: -1]).split(',')
        # print 'arr: ', arr
        ordering = [a.strip().strip("'").strip() for a in arr]
        # print 'ordering: ', ordering
        for wizard in ordering:
            # print wizard
            file.write(wizard + '\n')