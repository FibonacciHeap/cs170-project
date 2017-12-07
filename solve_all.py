import os

inputs = os.listdir('./phase3_inputs')
for i in inputs:
    filename = i.split('/')[-1]
    print 'Running ' + filename
    os.system('python phase3_inputs/' + filename + ' phase3_outputs/' + filename)
    print 'Solved ' + filename
    os.remove('python phase3_inputs/' + filename)
