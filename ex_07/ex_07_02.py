# use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print("Error. Try again.")
	quit()

count = 0 
total = 0

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	count = count + 1
	
	fnum = line.find(" ")
	num = line[fnum+1:]
	flnum = float(num)
	
	total = total + flnum
	av = total/count

print("Average spam confidence:", av)