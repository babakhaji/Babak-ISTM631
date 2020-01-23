import random

# this file generates two text files

# one is a file containing 50 integer numbers

f = open('integers.txt', 'w')

for count in range(50):
    number=random.randint(1,500)
    f.write(str(number)+ '\n')
            

f.close()

# here is another file containing 50 words with three random letters 


f = open('test-text.txt', 'w')

for count in range(50):
    number=random.randint(32,127)
    f.write(chr(number)+ chr(number+1) + chr(number+2) + '\n')
              

f.close()
