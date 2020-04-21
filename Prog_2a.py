#Write a function which gets no: of strings using variable no: of arguments and,
#find unique characters in each string. (hint: use set())

def find_unique(*all):
	for word in all:
		unique_char_list=list(set(word))
		print("Unique characters in "+word+":"+str(unique_char_list))

find_unique('aaaa', 'abcd', 'abba', 'xyz', 'abcba')