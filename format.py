import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

if len(sys.argv) < 2:
    raise ValueError
path = sys.argv[1].encode('utf-8').strip()
# print path
for filename in os.listdir(path):
    contents = ''
    with open(path + '/' + filename , 'r') as file:
        contents = file.readlines()
        multi = True
        if len(contents) == 1:
            contents = contents[0]
            multi = False
    with open(path + '/' + filename , 'w') as file:
        if multi:
            for wizard in contents:
                file.write(wizard.rstrip() + ' ')
        else:
            arr = (find_between(contents, '[', ']')[1: -1]).split(',')
            ordering = [a.strip().strip("'").strip() for a in arr]
            for wizard in ordering:
                file.write(wizard + ' ')
