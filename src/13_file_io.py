"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
filename = "src/foo.txt"
file = open(filename, 'r')
print(file.read())
file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filename = "src/bar.txt"
file = open(filename, "w")
changes = ["Line 1 ", "Line 2 ", "Line 3 not 4 "]
file.writelines(changes)
file.close()

# Second try
filename = "src/bar2.txt"
file = open(filename, "w")
change1 = "Line 1 "
change2 = "Line 2 "
change3 = "Line 3 "
file.write(change1)
file.write(change2)
file.write(change3)
file.close()
