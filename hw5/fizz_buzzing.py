import random


# generates string with three random numbers and newline at the end
# the first two random numbers are in range from 1 to 19 and the third one is in range from 20 to 30
def generate_three_numbers():
    return str(random.randint(1, 19)) + " " + str(random.randint(1, 19)) + " " + str(random.randint(20, 30))


# performs main fizz-buzz transformations
def transformation(line, filename):
    line_list = line.split()
    fizz = int(line_list[0])
    buzz = int(line_list[1])
    ham = int(line_list[2])
    for i in range(1, ham + 1):
        if not (i % fizz) and not (i % buzz):
            filename.write("FB ")
        elif not (i % fizz):
            filename.write("F ")
        elif not (i % buzz):
            filename.write("B ")
        else:
            filename.write(str(i) + " ")
    filename.write("\n")