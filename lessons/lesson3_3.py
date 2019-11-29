#this splits text file's line into array and transforms values in that array to integers
import sys
f = open(sys.argv[1], 'r')

for line in f:
    li = [int(x) for x in line.split()] # this is called "line comprehension"
    #li = line.split()
    #li = list(map(int, li))
    print(li)

f.close()