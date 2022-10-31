#!/usr/bin/env python

'''
with open("show_version.txt") as my_file:
    data = my_file.readlines()

print(f"\nLength of list {len(data)}\n")

print("Print line number1")
print("-" * 40)
print(data[0].rstrip())
print("-" * 40)

print()
print("Print line number34")
print("-" * 40)
print(data[34].rstrip())
print("-" * 40)
print()

fields = data[0].split(",")
os_version = fields[2].strip()
print("OS Version:")
print(os_version)
print()

Lists Ex2
----------

a. Read the file "show_version.txt" (in the current directory). Remember the VS Code file
location issue.

b. Read in the contents of the file using the readlines() method. This will create a list.

c. Print the length of the list. This will give you the number of lines in that file.

d. Print out lines number 1 and 35 respectively. Which indices are these?

e. Split line number1 into fields using a comma as the field separator. One of these fields
should be OS Version. Print this to standard output.

'''
with open("show_version.txt") as show_version:
    data = show_version.readlines()
    
    print(data)

print(len(data))

print(data[0])
print(data[34])

fields = data[0].split(",")
print(fields)

version = fields[2].strip()
print(f"\nVersion is {version}\n")