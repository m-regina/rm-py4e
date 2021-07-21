# press enter to open the file
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

# create dictionary
di = dict()


# find emails, store in dic and count of the number of times they appear in the file.
for line in handle:
    if line.startswith("From "):
        mail = line.split()
        email = mail[1]
        di[email] = di.get(email, 0) + 1

# reads through the dic and figure out who has sent the greatest number of mail messages.
# using a maximum loop.
largest = 0
person = None
for k,v in di.items():
    if v > largest:
        largest = v
        person = k
print(person, largest)
