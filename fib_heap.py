import sys
import os

"""
#python solver.py phase2_inputs/inputs20/input20_0.in test_out.txt

#how to run:
#python fib_heap.py -n num -file yy_x (see below)
#-n: number of iterations, an integer
#-file: 20_x, 35_x, or 50_x where x is the file number you want to test on

"""

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def run_commands(num, file_name):
    output = []
    for i in range(int(num)):
        output.append(os.system('nohup python solver.py phase2_inputs/inputs' + file_name[:2] + '/input' + file_name + '.in outputs/test_out' + file_name + '_' + str(i) + '.txt &'))
    print(output)

if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    if '-n' in myargs:
        num = myargs['-n']
    if '-file' in myargs:
        f = myargs['-file']
    run_commands(num, f)

    #print(myargs)
