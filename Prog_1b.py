#Validate a given date. Input date in the format dd/mm/yyyy. Check also for leap year.
# Validate a given date. Check also for leap year.


maxdays = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
line = input("enter the date as dd/mm/yyyy : ")
(dd, mm, yy) = line.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)
if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0) :
	maxdays[2] = 29
if mm < 1 or mm > 12 :
	print ("invalid month")
elif dd < 1 or dd > maxdays[mm] :
	print ("invalid date")
else:
	print ("date ok")


