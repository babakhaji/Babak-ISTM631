"""
File: Class5-project3.py
Project 3
uniqe words in a file in alphabetical order. 
"""

file_name = input('enter a file name: ')


f = open(file_name, "r")

a = []




for line in f:


    # using .strip() all leading and trailing whitespaces are removed from the string.
    words = line.strip()
    print(words)

    # split() returns a list of strings after breaking
    # the given string by the specified separator.
    words = words.split()
    print(words)

    for word in words:
        if not word in a:
            a.append(word)
    

            

print(a)

a.sort()
print(a)
