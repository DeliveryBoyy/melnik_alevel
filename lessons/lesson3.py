flats_per_floor = 4
floors = 24

print ("Enter the apartment number you need to look for")
flat_needed = int(input()) #113
current_floor = 1
current_flats = current_floor * 4

while current_floor <= floors:
    if flat_needed <= current_floor * flats_per_floor:
        print("Floor {}, apartment found!".format(current_floor))
        break
    current_floor +=1