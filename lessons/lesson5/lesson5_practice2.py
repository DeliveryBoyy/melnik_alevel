numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def square_number(number):
    if (number != 1) and (number != 2):
        for divider in range(2, number):
            if not (number % divider):
                return number
            else:
                return (number * number)
    elif (number == 2):
        return 4
    else:
        return number

print(list(map(square_number, numbers)))