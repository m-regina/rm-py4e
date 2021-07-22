
# press enter to open the file
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

# create dictionary
di = dict()

# find the hour from emails; store in dic with count of the number of times they appear in the file.
for line in handle:
    if line.startswith("From "):
        mail = line.split()
        #print(mail)
        time = mail[5]
        hour = time[:2]
        #print(hour)
        di[hour] = di.get(hour, 0) + 1

# convert dic into a list; sort the list of tuples; print hour (and count)
for k,v in sorted(di.items()):
    print(k,v)
