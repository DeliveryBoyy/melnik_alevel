from random import randint

# generate 4 random marks
def random_marks():
    return [randint(1,5), randint(1, 5), randint(1, 5), randint(1, 5)]


# set student names
students = {
    'Ivanov': [],
    'Petrov': [],
    'Melnik': [],
    'Martsin': [],
    'Zelenskaya': [],
    'Lavro': []
}

# assign marks
for key in students:
    students[key] = random_marks()

# transform mark lists to averages
for key in students:
    students[key] = round(sum(students[key])/len(students[key]), 1)

# find the hightest average and return it
highest_average = dict([max(students.items(), key=lambda k_v: k_v[1])])
lowest_average = dict([min(students.items(), key=lambda k_v: k_v[1])])

print(students)
print(highest_average, lowest_average)