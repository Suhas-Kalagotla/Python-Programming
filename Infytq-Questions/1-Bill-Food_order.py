#!/usr/bin/env python3

'''
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate.
Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point.
The delivery charges are as mentioned below:

                        Distance in kms        Delivery charge is Rs per km
                        For first 3 kms        0
                        For next 3 kms         3
                        For the remaining      6

Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point,
write a python program to calculate the final bill amount to be paid by a customer.

The below information must be used to check the validity of the data provided by the customer:
Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.
Distance in kms must be greater than 0.
Quantity ordered should be minimum 1.

If any of the input is invalid, the bill amount should be considered as -1.

Input Format

First line input is an character indicating type of food, second line input is an integer indicating quantity (no. of plates)
and third line input is an integer indicating distance in kms from the restaurant to the delivery point

Constraints

Refer sample input and output.

Output Format:
Is an integer which indicate final bill amount to be paid by a customer.

Sample Input 0

Dish you want to order = N
No. of plates = 2
Distance in kms from the restaurent = 7

Sample Output 0

Bill = 315
'''
#!/usr/bin/env 	python3

food = input('Dish you want to order = ')
quantity = int(input('No. of plates = '))
dis = float(input('Distance in kms from the restaurent = '))

def validity(food,quantity,dis):         # if-else conditions to validate user input
    if food.upper() not in ['V','N'] or quantity < 1 or dis <= 0 :
        return False
    else:
        return True

def main(food,quantity,dis):       # here cost is calcuated
    bill = 0

    if food.upper() == 'V':        # cost of items is added to bill
        bill += 120
    elif food.upper() == 'N':
        bill += 150

    bill *= quantity               # cost is multiplied by no of plates ... and here cost is equal to bill

    init = dis
    while init > 6:                # while loops to add the distance cost to the bill
        bill += 6
        init -= 1
    while 3 < init <= 6:
        bill += 3
        init -= 1

    return bill                    # function returns the final bill

if validity(food,quantity,dis):
    print('Bill =',main(food,quantity,dis))   # if input values are appropiate we calculate the bill

else:
    bill = -1                      # if input values are not valid the bill is -1
    print('Bill =',bill)
