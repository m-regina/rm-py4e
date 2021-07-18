# Open the file romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
#empty list
lst = list()

for line in fh:
    line = line.rstrip()
    for word in line.split(" "):
        if word not in lst:
            lst.append(word)

print(sorted(lst))

