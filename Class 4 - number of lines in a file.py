# take the file name as an input
file_name = input('Enter file name: ')

# create a list of available txt files
list = ['integers.txt']

# check if the file is in the list

if file_name in list:
    
# open the file and count the number of lines

    f=open('integers.txt', 'r')

    theSum=0
    Number_lines =0

    for line in f:
        Number_lines += 1
        number = line.strip()
        theSum += int(number)

        if len(number)<=2:
           print(line)

      

    print('The number of line is ', Number_lines)
    print('The total sum is ', theSum)
    print("The average is ", theSum/Number_lines)

else:
# if the file is not in the list print "Error"
    print('Error')

