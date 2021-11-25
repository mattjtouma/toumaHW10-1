# This program takes two text files and concatenates their alternating elements
# into one output file.
#
# Example invocation: reconstructSentence.py input1.txt input2.txt
#
# Written by Matthew J. Touma on 11/24/2021
#

import sys
import pdb

# Use the command line arguments as input text file names
input1_filename = sys.argv[1]
input2_filename = sys.argv[2]

# Open the two text files for reading
input1_file = open(input1_filename, "r")
input2_file = open(input2_filename, "r")

# Get the files' contents as a 1-item string list
input1 = input1_file.readlines()
input2 = input2_file.readlines()

# Remove the newline character
input1 = input1[0].strip()
input2 = input2[0].strip()

# Split the string by the spaces
input1 = input1.split(" ")
input2 = input2.split(" ")
print "\n" + input1_filename + ": " + " ".join(input1)
print input2_filename + ": " + " ".join(input2) + "\n"

# Create an empty output list
out = []

# Get the length of the two inputs
in1_length = len(input1)
in2_length = len(input2)
print input1_filename + " length: " + str(in1_length)
print input2_filename + " length: " + str(in2_length) + "\n"

#pdb.set_trace()

# Initialize the index counter
this_end = 1

# When the length of the output list equals the length of
# the sum of the two input lists, that means we have read
# all the words from both lists.
while len(out) <  in1_length + in2_length:
	
	# Since the two input strings could have different
	# lengths, make sure that the index counter
	# does not exceed the number of elements in either.
	if this_end <= in1_length:
		# Append the item from input1 to the output list
		out.append(input1[-this_end])
	if this_end <= in2_length:
                # Append the item from input1 to the output list
		out.append(input2[-this_end])
	# Increment the index counter
	this_end = this_end+1

# Join the words in the output list with spaces
out = " ".join(out)
print "Output: " + "".join(out) + "\n"

# Write the output string to a file
outfile = open("output.txt", "w")
outfile.write(out)

# Close the files
input1_file.close()
input2_file.close()
outfile.close()
