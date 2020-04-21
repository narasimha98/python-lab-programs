#Given an input file which contains list of names, phone numbers and email-ids separated by spaces in the following format:-
#Alex 80-23425525 alex234@yahoo.com
#Emily 322-56775342 em_44@gmail.com
#Grace 20-24564555 softech_grace@rediffmail.com
#Phone number contains 3 or 2 digit area code and a hyphen followed by 8 digit number
#Perform the following using regular expressions:-
#	Find all names having phone numbers with 3 digit area code.
#	Find the total number of people having Gmail id.
#	Find user name part of email id for all people whose name start with 'G' or 'E' and ends with 'y'

import re

#Find all phone numbers having 4 consecutive 0s at the end.
f = open("details.txt","r")
print("\n2a Solution\n")
for line in f:
	m=re.search(r"[a-zA-z]+\s+(\d{2,3}-\d{4}0{4})\s+",line)
	if m:
		print(m.group(1))
f.close()

#Find all names having phone numbers with 3 digit area code.
f = open("details.txt","r")
print("\n2b Solution\n")
for line in f:
	m=re.search(r"([a-zA-z]+)\s+\d{3}-\d{8}\s+",line)
	if m:
		print(m.group(1))
f.close()

#Find the total number of people having Gmail id.
f = open("details.txt","r")
all_lines = f.read()
print("\n2c Solution\n")
L = re.findall(r"\w+@gmail\.com",all_lines)
print(L)
print(len(L))
f.close()

#Find user name part of email id for all people whose name start with 'G' or 'E' and ends with 'y'
f = open("details.txt","r")
print("\n2d Solution\n")
for line in f:
	m = re.search(r"^[GE][a-z]*y\s+.*\s+(\w+)@\w+\.\w+",line)
	if m:
		print(m.group(1))
f.close()

#Find all names whose phone numbers are not in proper format.
f = open("details.txt","r")
print("\n2e Solution\n")
for line in f:
	m = re.search(r".*\s+\d{2,3}-\d{8}",line)
	if not m:
		m=re.search(r"(^[A-Z][a-z]+)",line)
		print(m.group(1))
f.close()