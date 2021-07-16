# Rewrite your pay computation to give the employee 
# 1.5 times the hourly rate hours worked above 40 hours.

message = "Let's caltulate your week payslip.\nRemember, you get 1.5 times the hourly rate if you work above 40hs!"
print(message)

sh = input("Enter Hours: ")
sr = input ("Enter Rate: ")

try:
    fhour = float(sh)
    frate = float(sr)
except:
    print("Error, please enter numeric input.")
    quit()

if fhour > 40 :
    ovt = fhour - 40.0
    ovt_rate = (frate * 1.5)
    xp = (40.0 * frate) + (ovt * ovt_rate)
    print(f"total hours = {fhour} hs, overtime = {ovt} hs, overtime rate = £{ovt_rate}".title())

else:
    print("Regular")
    xp = fhour * frate

# Calculate net pay (after tax - 20%)
tax = (20.0 * xp) / 100.0
net = xp - tax

print("gross pay:".title(),xp)
print("net pay:".upper(),net)

