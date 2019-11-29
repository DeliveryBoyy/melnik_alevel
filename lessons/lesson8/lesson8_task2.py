main_dict = {
    "Waist circumference": ["63-65", "66-69", "70-74", "75-78", "79-83", "84-89", "90-94", "95-97"],
    "Hip girth": ["89-92", "93-96", "97-101", "102-104", "105-108", "109-112", "113-117", "118-122"],
    "International sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL", "XXXL"],
    "Russia sizes": ["42", "44", "46", "48", "50", "52", "54", "56"],
    "Germany sizes": ["36", "38", "40", "42", "44", "46", "48", "50"],
    "USA sizes": ["8", "10", "12", "14", "16", "18", "20", "22"],
    "France sizes": ["38", "40", "42", "44", "46", "48", "50", "52"],
    "Britain sizes": ["24", "26", "28", "30", "32", "34", "36", "38"]
}

print("Type the number of the type of size you know, then press Enter:")
print(
    "1. Waist circumference\n" +
    "2. Hip girth\n" +
    "3. International sizes\n" +
    "4. Russia sizes\n" +
    "5. Germany sizes\n" +
    "6. USA sizes\n" +
    "7. France sizes\n" +
    "8. Britain sizes\n"
)

# translates the user input into the string with a main_dict key
print(list(main_dict.keys()))
chosen_type = list(main_dict.keys())[int(input()) - 1]

print("Choose the size:")
# prints a numbered list of all sizes in a chosen size type
for i in range(len(main_dict[chosen_type])):
    print(str(i + 1) + ". " + main_dict[chosen_type][i])

# finds the depth of the sizes table
chosen_size_depth = int(input()) - 1

# prints the sizes from all systems at the given depth
print("Here are the matching sizes in all systems:")
for key in main_dict:
    print(key + ": " + main_dict[key][chosen_size_depth])
