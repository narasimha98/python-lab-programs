#Write a program to
#####Determine whether the given string is a palindrome or not using slicing (::-1) and without using slicing.
#####Convert a string to camel case. E.g.: If the given string is "This is a test", the output should be "ThisIsATest"
#####Find the number of vowels and consonants in a given string

S=input("Enter string: ")

#checking for palindrome with slicing

if S == S[::-1]:
	print("Entered string is a palindrome")
else:
	print("Entered string is not a palindrome")


#checking for palindrome without slicing
L = list(S)
L.reverse()
Reverse = "".join(L)
if S == Reverse:
	print("Entered string is a palindrome")
else:
	print("Entered string is not a palindrome")


#checking for palindrome without slicing
C = S
l = len(S)
for i in S:
	if i != C[l-1]:
		print("Entered string is not a palindrome")
		break
	l-=1
else:
	print("Entered string is a palindrome")



S = input("Enter string: ")
lst = []

for word in S.split():
	lst.append(word[0].upper() + word[1:])

Cam = " ".join(lst)
print("String '%s' converted to camel case is '%s'" % (S, Cam))


S=input("Enter string :")

v=0
c=0

for char in S:
	if char in ["a","e","i","o","u"] or char in ["A","E","I","O","U"]:
		v+=1
	elif char.isalpha():
		c+=1

print("Number of vowels is %d and number of consonants is %d" %(v,c))
