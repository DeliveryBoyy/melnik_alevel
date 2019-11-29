print ("Enter fizz")
fizz = int(input())
print ("Enter buzz")
buzz = int(input())
print ("Enter ham")
ham = int(input())

for i in range (1, ham+1):
    if not (i % fizz) and not (i % buzz):
        print ("FB")
    elif not (i % fizz):
        print ("F")
    elif not (i % buzz):
        print ("B")
    else:
        print (i)