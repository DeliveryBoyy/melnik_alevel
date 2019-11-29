# this version requires the input and output files to be created and empty
# call them whatever you like, but pass them as arguments when running the script

import sys
import random

filename = sys.argv[1]
filename1 = sys.argv[2]

# open the input file in 'append' mode, generate 20 lines with 3 random numbers in each one, then close the file
# the first two random numbers are in range from 1 to 19 and the third one is in range from 20 to 30
f = open(filename, 'a')
for i in range(20):
    f.write(str(random.randint(1, 19)) + " " + str(random.randint(1, 19)) + " " + str(random.randint(20, 30)) + "\n")
f.close()

# open both input and output files, input in 'read' and output in 'append' mode
f = open(filename, 'r')
f1 = open(filename1, 'a')

# for each line in input file, separate the line to get three integer values
for line in f:
    line_list = line.split()
    fizz = int(line_list[0])
    buzz = int(line_list[1])
    ham = int(line_list[2])
    # perform fizz buzz operation on the set three int values and write it to the result file on a single string
    for i in range(1, ham + 1):
        if not (i % fizz) and not (i % buzz):
            f1.write("FB ")
        elif not (i % fizz):
            f1.write("F ")
        elif not (i % buzz):
            f1.write("B ")
        else:
            f1.write(str(i) + " ")
    f1.write("\n")

f.close()
f1.close()
