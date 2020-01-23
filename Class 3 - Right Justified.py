# Two approaches

# Approach 1:

x = str(input("Enter an integer number: "))
y = str(input("Enter an integer number: "))
z = str(input("Enter an integer number: "))
              
print(x.rjust(6), y.rjust(6), z.rjust(6))


# Approach 2:

a=int(input("Enter an integer number: "))
b=int(input("Enter an integer number: "))
c=int(input("Enter an integer number: "))

print("%6d%7d%7d"%(a,b,c))




          
