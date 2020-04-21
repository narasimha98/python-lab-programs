#Given n, generate Pascal triangle for n rows. Use list of lists.
#If n = 5, output should be
#                   1
#                1      1
#             1     2       1
#          1     3      3      1
#      1      4     6      4      1
#Check : str.format for formatting and replication operator to get # of spaces

# generate pascal triangle
print("Enter n:",end="")
n=int(input())
# create a list of lists, each list having varying # of elements
#	- jagged array

# create n lists
pt = []
for i in range(n) :
	pt.append([])
	pt[i].append(1)
	for j in range(1, i) :
		pt[i].append(pt[i-1][j-1] + pt[i-1][j])
	if i != 0 : pt[i].append(1)

#print(pt)
for i in range(n) :
	# output spaces; # of spaces decreases as i increases
	print( "   " * (n - i), end = "", sep = "")
	for j in range(i + 1) :
		print("{0:6}".format(pt[i][j]), end = "", sep = "")
	print()