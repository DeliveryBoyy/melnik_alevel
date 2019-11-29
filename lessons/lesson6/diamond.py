def star_printing(number):
    if (number > 0) and (number % 2):
        star_number = 1
        indentation = number // 2
        for i in range(0, number // 2):
            print(" " * indentation + "*" * star_number + " " * indentation)
            star_number += 2
            indentation -= 1

        for j in range(0, (number // 2) + 1):
            print(" " * indentation + "*" * star_number + " " * indentation)
            star_number -= 2
            indentation += 1

    else:
        print("Invalid number")
        return

    # for j in range (i, number)


# print("How wide your diamond should be:")
# star_size:
star_printing(7)

# print("\n")
# print(" " * 5 + "test")
