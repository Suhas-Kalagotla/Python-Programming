#!/usr/bin/env python3

'''
The Metro Bank provides various types of loans such as car loans,
business loans and house loans to its account holders.
Write a python program to implement the following requirements:

Initialize the following variables with appropriate input values:account_number,
account_balance, salary, loan_type, loan_amount_expected and customer_emi_expected.

The account number should be of 4 digits and its first digit should be 1.
The customer should have a minimum balance of Rupees 1 Lakh in the account.

If the above rules are valid, determine the eligible loan amount and the EMI
that the bank can provide to its customers based on their salary and the loan type
they expect to avail.

The bank would provide the loan, only if the loan amount and the number of EMI’s
requested by the customer is less than or equal to the loan amount and the number
of EMI’s decided by the bank respectively.

Display appropriate error messages for all invalid data. If all the business rules
are satisfied ,then display account number, eligible and requested loan amount and EMI’s.
Test your code by providing different values for the input variables.

          Salary        Loan Type         Eligible loan amount         no.of EMI's required to repay
         > 25000        Car               500000                       36
         > 50000        House             6000000                      60
         > 75000        Business          7500000                      84

Input Format

First line consist an integer denoting Account Number.
Second line consist an integer denoting Salary.
Third line is account balance represented as integer.
Fourth line is string denoting Loan Type. Fifth line consist an integer indicatine
expected loan amount. Last line of input is expected number of EMI as denoted as integer.

Constraints
Refet Sample input and output

Output Format

Use the below given print statements to display the output, in case of success
"Account number:"followed by account_number "Eligible loan amount Rs."followed by
eligible_loan_amount "Eligible EMIs :"followed by bank_emi_expected "Requested loan amount:"
followed by loan_amount_expected "Requested EMI's:"followed by customer_emi_expected

Use the below given print statements to display the output,
in case of invalid data. "Insufficient account balance" "Requested EMI's not avilable"
 "Invalid account number" "Invalid loan type or salary"

Sample Input 0

1001
40000
250000
Car
300000
30

Sample Output 0

Account number:1001
Eligible loan amount Rs.500000
Eligible EMIs:36
Requested loan amount:300000
Requested EMI's:30
'''

#!/usr/bin/env python3
"""
taking the required inputs from the user and assigning them to variables
with appropiate names
"""
account_number = int(input('Enter account number: '))
salary = int(input('Enter salary: '))
account_balance = int(input('Enter account_balance: '))
loan_type = input('Enter loan type: ')
loan_amount_expected = int(input('Enter loan amount expected: '))
customer_emi_expected = int(input('''Enter emi's expected: '''))

"""
we validate users input i.e. account number , account balance and salary
we have two different validations this is the first validation , we are using
two different because if the values validated  here are correct then we produce
to second validation to check the necessary branching conditions

this validation calls the second validation if everything is correct i.e. branching validations
"""

def validations_input(ac_no,salary,ac_ba,loan_type,loan_amount_expected,customer_emi_expected) :
    if ac_no < 1000 or str(ac_no)[:1] != '1' :
        return 'Invalid account number'
    elif  ac_ba < 100000 :
        return 'Insufficient account balance'
    else:
        return branching_validations(ac_no,salary,ac_ba,loan_type,loan_amount_expected,customer_emi_expected)


"""
the function does the additional validation of loan_type and respective salary
required , requested emi less then required emi , and requested loan less then
required loan and if everything is correct then it calls the output function or
else respective error messages are returned
"""


def branching_validations(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected) :

    #initializing required errors

    loan_salary_error = 'Invalid loan type or salary'
    emi_error = "Requested EMI's not avilable"

    # using if-else statements to validate and returing the initialized required errors

    # if-else to validate the conditions for a car loan and call output function
    # if everything is correct

    if loan_type == 'Car' and salary >= 25000 :
        if loan_amount_expected <= 500000 :  #for this if statement there is no 'else' statements because there is no error given to produce when the condition is not met
            if customer_emi_expected <= 36 :
                return output(account_number,500000,36,loan_amount_expected,customer_emi_expected) #calling function with appropiate parameters
            else :
                return emi_error

    # if-else statements to validate the conditions for a house loan and calling
    # output function if everything is correct

    elif loan_type == 'House' and salary >= 50000 :
        if loan_amount_expected <= 6000000 :
            if customer_emi_expected <= 60 :
                return output(account_number,6000000,60,loan_amount_expected,customer_emi_expected)
            else:
                return emi_error

    # we are using same format as used for validating car, house in validating
    # business conditions

    elif loan_type == 'Business' and salary >= 75000 :
        if loan_amount_expected <= 7500000 :
            if customer_emi_expected <= 84 :
                return output(account_number,7500000,84,loan_amount_expected,customer_emi_expected)
            else:
                return emi_error
    else:
        return loan_salary_error


# this function takes care about the print output format


def output(account_number,eli_loan,eli_emi,req_loan,req_emi) :
    # here we used triple quotes to print the multiline string as asked in output
    return f'''\nAccount number:{account_number}
Eligible loan amount Rs.{eli_loan}
Eligible EMIs:{eli_emi}
Requested loan amount:{req_loan}
Requested EMI's :{req_emi} '''

'''
this is the main function which starts the program it's work is to the call
the function i.e. validations_input if everything is correct ... the second
function branching_validations will be called and if it returns true (i.e. everything
is correct ) then the output function is called and the output is printed
this is the working flow of the code and if the required parameters are not met
respective errors are printed and flow-of-code is terminated
'''
def main(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected) :
    print(validations_input(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected))

# now the main function is called
main(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected)
