message = "Let's caltulate your week payslip.\nRemember, you get 1.5 times the hourly rate if you work above 40hs!"
print(message)

#function
def computepay(hours, rate) :
    #print("In computepay", hours, rate) 
    if hours > 40 :
        ovt = hours - 40.0
        ovt_rate = (rate * 1.5)
        pay = (40.0 * rate) + (ovt * ovt_rate)
        print(f"total hours = {hours} hs, overtime = {ovt} hs, overtime rate = £{ovt_rate}".title())

    else:
        print("Regular pay")
        pay = fhour * frate

    return pay

sh = input("Enter Hours: ")
sr = input ("Enter Rate: ")
try:
    fhour = float(sh)
    frate = float(sr)
except:
    print("Error, please enter numeric input.")
    quit()

xp = computepay(fhour,frate)

print("gross pay:".upper(),xp)