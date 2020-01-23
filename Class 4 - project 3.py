"""
File: copyfile.py
Project 4.8

Copies the text from a given input file to a given
output file.
"""

# Take the inputs
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")

# Open the input file and read the text

inputFile = open(inName, 'r')
text = inputFile.read()

# Open the output file
outFile = open(outName, 'w')


for line in text:

    code = ""
    
    for ch in line:
        # Add 1 to ASCII value
        ordValue = ord(ch) + 1
        # Convert to binary
        bstring = ""
        while ordValue > 0:
            remainder = ordValue % 2
            ordValue = ordValue // 2
            bstring = str(remainder) + bstring
        # Shift one bit to left
        if len(bstring) > 1:
            bstring = bstring[1:] + bstring[0]
        # Add encrypted character to code string
        code += bstring + " "
    print(code)
    #write code in the output file
    outFile.write(code + '\n')

outFile.close()




#outFile.write(text)
#outFile.close()
