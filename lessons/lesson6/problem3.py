import sys
import re

filename = sys.argv[1]
re_object = re.compile("([0-9]+\s)+[0-9]+;([0-9]+\s)+[0-9]+")
f = open(filename, 'r')
for line in f:
    print(line.strip())
    if re_object.match(line):
        print("True\n")
    else:
        print("False\n")

f.close()

# for line in f:
#     # I'm really sorry
#     input_string = list(map(int, list(line.split(";")[0].split())))
#     print("Strings we are working with:")
#     print(input_string)
#     sum_result = sum(input_string)
#     integer_result = sum_result // len(input_string)
#     remainder_result = sum_result % len(input_string)
#     print("Integer result = " + str(integer_result) + "\nRemainder = " + str(remainder_result))