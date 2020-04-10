import sys
filename = sys.argv[0]
# read file
f = open(filename, 'r') # file descriptor is now in file
for line in f: # for every line in the file
    print(line)
f.close() # close the file