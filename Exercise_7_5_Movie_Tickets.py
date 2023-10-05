# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15.
# Write a loop in which you ask user their age, and then tell them the cost of their movie ticket.

while True:
    age = input("Enter your age: ")
    age = int(age)

    if age < 0:
        print("Enter correct age.")
    elif age < 3:
        price = 'free'
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    
    print(f"For you, ticket would be {price}")