# What is file handling in python ?

# File handling in Python is the process of performing operations like creating, opening, reading, writing, and closing files on your local file system.

# f.open() :- this helps in opening a file which takes two things as arguement. One is filename and the second one is the mode of the file like read , write etc etc.

# Modes in file :- read (r) , write (w) , append (a), create (x) , text (t)

# 1.) read (r) :- Opens the file for reading only and gives error if the file is not present. This is the default mode. If you dont give any arguement then this will be taken.

# 2.) write (w) :- Opens the file for writing only and creates a new file if it does not already exist.

# 3.) append (a):- This mode opens the file for appending only and creates a new file if the file does not exist.

# 4.) create (x) :- This mode creates a file and gives an error if the file is already present.

# 5.) text (t) :- This mode is used to handle text files. t refers to the text mode.

# 6.) binary (b) :- used to handle binary files (images, pdfs, etc.)

# using with statement the file automatically gets closed without any need to explicitly mentioning it !!

with open('Selvi.txt','a') as f:
    f.write("Appending")
