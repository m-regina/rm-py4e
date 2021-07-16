largest = None
smallest = None
while True:
    num = input("Enter a number: ").lower()
    if num == "done" :
        break
    try :
        inum = int(num)
        if largest is None :
            largest = inum
        if smallest is None :
            smallest = inum
    except :
        print("Invalid input")
        
    if inum >= largest :
        largest = inum
    if inum <= smallest:
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)