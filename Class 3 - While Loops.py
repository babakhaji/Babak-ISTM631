thesum = 0

data = input("enter a number or press 'ENTER' to exit: ")
while data != '':
    number = float(data)
    thesum += number
    data = input("enter the next number or press 'ENTER' to stop: ")

print('The total sum is', thesum)

