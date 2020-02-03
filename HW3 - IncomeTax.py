#inputs from user

A = False



while A ==False:
    



    gross_income = input('Please enter your gross income or press "Enter" to exit: ')
    if gross_income =='':
        break
    else:
        gross_income=float(gross_income)
    
    num_dep = int(input('Enter the number of dependent(s): '))

    
    
    B = False

    while B==False:

        if gross_income >=0:
            if num_dep >=0:
                break
            else:
                num_dep = int(input('RE-enter the number of dependent(s): '))
        else:
            gross_income = input('Please enter your gross income or press "Enter" to exit: ')
            if gross_income =='':
                break
            else:
                gross_income=float(gross_income)

        
    gross_income = round(gross_income,2)


    deductible = 10000+3000*num_dep

    taxable_income = gross_income - deductible

    if taxable_income >= 0:
        income_tax = 0.2 * taxable_income
    else:
        income_tax=0
        taxable_income=0

    print('Gross income is $' + str(round(gross_income,2)))
    print('Your deductible is $' + str(round(deductible,2)))
    print('Taxable income is $' + str(round(taxable_income,2)))
    print('Your income tax is $' + str(round(income_tax,2)))
