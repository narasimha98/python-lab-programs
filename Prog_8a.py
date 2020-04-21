#Given an input file, do the following using regular expression and create an output file.
#	Remove extra whitespaces between two words.
#	Insert a white space after the end of a sentence (after . or ? or !).
#	First letter of each sentence should be upper case
#	Remove consecutive duplicate words.

import re

f = open("sample.txt","r")
str = f.read()
f.close()

def change_upper_start(m):
	return m.group(1).upper()

def change_upper_startline(m):
	return m.group(1)+m.group(2).upper()
#Remove spaces at the beginning and convert first char to uppercase
s1 = re.sub(r"^\s*([a-z])",change_upper_start,str)

#Insert whitespace at the end of each sentence
s2 = re.sub("([.?!])",r"\1 ",s1)

#Remove extra spaces between words
s3= re.sub(r"[ \t]+"," ",s2)

#Convert first char of each sentence to uppercase
s4=re.sub(r"([.?!]\s+)([a-z])",change_upper_startline,s3)

#Remove consecutive duplicate words
s5=re.sub(r"(\b\w+\b\s+)(\1)+",r"\1",s4)

f=open("converted.txt","w")
f.write(s5)
f.close()

