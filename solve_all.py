import os

inputs = os.listdir('./phase3_inputs')
print 'Input files to be processed: \n\n', inputs

for i in inputs:
    print 'Running ' + i
    if os.system('python solver.py phase3_inputs/' + i + ' phase3_outputs/' + i):
        exit()
    print 'Solved ' + i
    os.remove('phase3_inputs/' + i)
