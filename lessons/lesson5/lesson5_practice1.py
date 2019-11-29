def to_lowercase(target_string):
    return target_string.lower()

def to_uppercase(target_string):
    return target_string.upper()

# inq_string = "NOBODY expects the Spanish Inquisition! Our chief weapon is surprise...surprise and fear...fear and surprise.... Our two weapons are fear and surprise...and ruthless efficiency.... Our *three* weapons are fear, surprise, and ruthless efficiency...and an almost fanatical devotion to the Pope.... Our *four*...no... *Amongst* our weapons.... Amongst our weaponry...are such elements as fear, surprise.... I'll come in again."

test_list_1 = ["aa", "BB", "cc", "DD"]
test_list_2 = ["EE", "ff", "GG", "hh"]

print(list(map(to_lowercase, test_list_1)))
print(list(map(to_uppercase, test_list_2)))

