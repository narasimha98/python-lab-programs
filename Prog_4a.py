#Given a file “stateinfo.txt” containing names of the state and cities separated by “:”,
# create a file for each state named as “statename”.txt containing names of cities in that state.
# Sample input file “stateinfo.txt” is attached.
# Steps to follow: Walk through the file.
# Create a dictionary whose key is the state name and value is the file handle.
# Write city names into the file.
# Do close all the files at the end of processing using values in dictionary.

# create file for each state
state_dict = { }
f = open("stateinfo.txt")

for line in f :
	line = line.strip()
	(state, city) = line.split(':')
	if state not in state_dict :
		state_dict[state] = open(state, 'w')
	print(state, city, file = state_dict[state])
f.close()

for fh in state_dict.values() :
	fh.close()
