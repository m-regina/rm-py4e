# Write a program which repeatedly reads number until the user enters "done".
# Print out the total, count, average of the numbers. 
# If the user enters anyhin other than a number, detect their mistake using try and except.

num = 0
tot = 0
while True :
	sval = input('Enter a number: ').lower()
	if sval == 'done' :
		break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue

	num = num + 1
	tot = tot + fval

print(f"Total: {tot}, Count: {num}, Average: {tot/num}")