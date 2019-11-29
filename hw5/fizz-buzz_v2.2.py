# this version requires the input and output files to be created and empty
# call them whatever you like, but pass them as arguments when running the script

from random import randint
from sys import argv
from fizz_buzzing import generate_three_numbers, transformation

filename = argv[1]
filename1 = argv[2]

# open the input file in 'append' mode, generate 20 lines of random numbers
f = open(filename, 'a')
for i in range(20):
    f.write(generate_three_numbers() + "\n")
f.close()

# open both input and output files, input in 'read' and output in 'append' mode
f = open(filename, 'r')
f1 = open(filename1, 'a')

# for each line in input file, separate the line to get three integer values
for line in f:
    transformation(line, f1)

# close both input and output file
f.close()
f1.close()