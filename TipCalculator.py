#Tip Calculator
#A friendly program to calculate your tip and split the bill.

print("Welcome to the Tip Calculator! \U0001F4B5\n")

#Safely get user input
while True:
    try:
        bill_amount = float(input("Enter your bill amount: $"))
        if bill_amount <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive number.\n")

#Suggested gratuities
tips = [0.15, 0.20, 0.25]
print("Suggested Gratuities\n---------------------")
for t in tips:
    print(f"{int(t*100)}%\t\t${bill_amount * t:.2f}")

#Choose tip amount
while True:
    try:
        tip_amount = float(input("\nEnter your desired tip amount: $"))
        if tip_amount < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive number.\n")

#Option to Split the bill
while True:
    try:
        people = int(input("\nSplit between how many people? "))
        if people <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer.\n")

#Calculate the bill total(s)
total = bill_amount + tip_amount
per_person = total / people

print("\n--------------------------------")
print(f"Bill amount: ${bill_amount:,.2f}")
print(f"Tip amount:  ${tip_amount:,.2f}")
print(f"Total to pay: ${total:,.2f}")

#Only displays if more than 1 person is paying/splitting the bill
if people > 1:
    print(f"Each person pays: ${per_person:,.2f}")
    
print("Thank you for using the Tip Calculator! \U0001F4B5")
