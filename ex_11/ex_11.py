import re
fname = input("File name: ")
handle = open(fname)

total = 0
count = 0

line = handle.read()  
num = re.findall('([0-9]+)', line)
#re.findal will return a list of strings
for n in num:
    total = total + int(n)
    count = count + 1

#print(count)
print(total)
