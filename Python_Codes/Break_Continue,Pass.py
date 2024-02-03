#Break - Breaks the execution of currect block
#7Get a list of numbers from the user and add to a list
 
print ("Enter list of numbers. Enter Z to exist. ")
list_New = []
while True:
    inp = int(input())
    if inp == "Z":
        break
    list.append(int(inp))

print(list_New)
