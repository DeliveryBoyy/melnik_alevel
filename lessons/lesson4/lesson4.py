print("input fizz")
fizz = int(input())
print("input buzz")
buzz = int(input())
print("input ham")
ham = int(input())
for i in range (1, ham + 1):
    if not (i % fizz) and (i % buzz):
        print ("FB")
    elif not (i % fizz):
        print ("F")
    elif not (i % buzz):
        print ("B")
    else:
        print (i)