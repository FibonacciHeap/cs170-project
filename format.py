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
        # contents = file.read()
        contents = file.readlines()
        # if contents[0] != '[':
        #     continue
        if len(contents) == 1:
            continue
    with open(path + '/' + filename , 'w') as file:
        file.write('[')
        # # print 'contents: ', contents
        # arr = (find_between(contents, '[', ']')[1: -1]).split(',')
        # # print 'arr: ', arr
        # ordering = [a.strip().strip("'").strip() for a in arr]
        # # print 'ordering: ', ordering
        # for wizard in ordering:
        #     # print wizard
        #     file.write(wizard + '\n')
        for i in range(len(contents) - 1):
            # print wizard
            file.write(contents[i] + ', ')
        file.write(contents[len(contents) - 1] + ']')
