import sys, glob, os
from os.path import basename

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
file_names = glob.glob(pattern)
print(file_names)

# TODO: use os.path.getsize to find each file's size
# our code
for file_size in file_names:
    print(os.path.getsize(file_size), "bytes")

# example from python_demos1 - 14_iterate_files.py
# for file in glob.glob(pattern):
#     size = os.path.getsize(file)
#     print(file, size, "bytes")

# TODO: Add a test to only display files that are not zero length
if file_names:
    print(file_names)
# conditional statement is asking if file_names is true (are they not zero)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
for path in file_names:
    base_name = os.path.basename(path)
    print(base_name)
# file_names is a list
# os.path.basename removes the base name of the files in the list


