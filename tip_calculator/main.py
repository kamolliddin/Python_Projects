#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = float(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people to split the bill between: "))
tip_percentage = float(input("Enter the percentage of tip: "))

if bill == 0 or number_of_people == 0:
    print("Cannot take 0 for bill or number of people !!!")
else:
    tip_amount_per_person = bill / 100 * tip_percentage / number_of_people
    amount_per_person = round(bill / number_of_people + tip_amount_per_person, 2)
    print(f"Each person must pay ${amount_per_person:.2f}")