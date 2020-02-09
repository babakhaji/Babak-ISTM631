# return the factorial of the input value

A = True

n = input("Enter an integer number: ")


while A == True:

    n=int(n)

    # defining a function for calculating factorial of a number
    # this is an example of a recursive function

    def factorial(a):
        if a ==1 or a==0:
            return 1
        else:
            return a*factorial(a-1)

    print(factorial(n))

    n = input('Enter another integer number or press "Enter" to STOP: ')

    if n =='':
        A=False


    
