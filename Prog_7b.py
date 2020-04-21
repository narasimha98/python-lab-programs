#Do the following using regular expressions:-
#	Find all occurrences of a word in a multiline string. The search must be case insensitive. Also find and display the starting index of each matched word in the input string.
#	Given a line of text find all characters other than vowels and space characters.
#	Given a list of strings find all strings that start with a digit or an underscore.

import re

line = '''this String is a multiline string
used to test the usage of re.multilinestring in a
multiline string'''

#To search the word "string" in line
match_Obj = re.finditer(r"\bstring\b",line,re.I)


'''If the word to be searched is stored in the variable "word_to_find", then the
   regular expression can be written as follows

word_to_find = "string"
match_Obj = re.finditer(r"\b%s\b"%word_to_find,line,re.I)  '''


for word in match_Obj:
	print(word.group()+" at index ",int(word.start()))

import re

line = 'this is a line 		of text !'

L=re.findall(r"[^aeiou \t]",line)
print(L)

import re

L = ["apple","4sdj","_5dfkjghd","__next","abcd","02352"]

for item in L:
	if re.search(r"^[\d_]",item):
		print(item)


