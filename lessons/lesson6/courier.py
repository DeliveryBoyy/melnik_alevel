target_apartment = 69
floors_in_porch = 9
apartments_on_floor = 4


def courier(target_apartment, apartments_on_floor, floors_in_porch):
    # below finds the target floor number from the total number of floors in the building (all porches)
    if target_apartment % apartments_on_floor:
        # division completed with a remainder
        target_floor = (target_apartment // apartments_on_floor) + 1
        # int(target_floor)
        # return target_floor
    else:
        # no remainder of the division
        target_floor = target_apartment / apartments_on_floor
        # int(target_floor)
        # return int(target_floor)

    # below finds the porch number
    if target_floor % floors_in_porch:
        # division completed with a remainder
        target_porch = (target_floor // floors_in_porch) + 1
        # int(target_porch)
    else:
        # no remainder of the division
        target_porch = target_floor / floors_in_porch
        # int(target_porch)

    result_floor = target_floor - (floors_in_porch * (target_porch - 1))

    print("Your searched apartment is in porch #" + str(int(target_porch)) + ", floor #" + str(int(result_floor)))


courier(target_apartment, apartments_on_floor, floors_in_porch)
