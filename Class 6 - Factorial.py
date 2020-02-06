# return the factorial of the input value

A = True

n = input("Enter an integer number: ")


while A == True:

    n=int(n)

    def factorial(a):
        if a ==1:
            return 1
        else:
            return a*factorial(a-1)

    print(factorial(n))

    n = input('Enter anpther integer number or press "Enter" to STOP: ')

    if n =='':
        A=False


    
