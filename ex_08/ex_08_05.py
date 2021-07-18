# Open the file mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        count = count + 1
        email = line.split()
        print(email[1])
print("There were", count, "lines in the file with From as the first word")