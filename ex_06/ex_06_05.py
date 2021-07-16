#Extracts the number at the end of the line below. 
#And it converts it to a float point number.

text = "X-DSPAM-Confidence:      0.8475"
cero = text.find("0")
five = text.find("5")
num = text[cero:five+1]
fnum = float(num)
print(fnum)