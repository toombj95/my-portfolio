print('\U0001F3F0 \U0001F478 Welcome to the Ultimate Disneyland App! \U0001F478 \U0001F3F0')
print('\nManage tickets and track rides in one place!\n')


#----Ticketing Section----

def get_guest_type(age):
    '''Determine guest type based on age'''
    if 0<= age <= 2:
        return "t" #toddler
    elif 3 <= age <= 9:
        return "c" #child
    elif age >= 10:
        return "a" #adult
    else:
        return "invalid age" 
		
#Initialize counters and totals

numGuests = 0
guestAge = 0
guestType = ""
numToddler = 0
numChild = 0
numAdult = 0
totalToddlerCost = 0
totalChildCost = 0
totalAdultCost = 0
totalCostForAll = 0

#Ask for the number of guests

while numGuests < 1 or numGuests > 8:
    try:
        numGuests = int(input("How many guests in your party? (Limit 8 guests per party):"))
    except ValueError:
        print("Please enter a valid number.")

#Loop through each guest to get age    
for i in range(numGuests):
    while True:
        try:
            age = float(input(f"\nEnter age of guest {i +1}: "))
            
            guestType = get_guest_type(age)
            
            if guestType == 't':
                numToddler +=1
            elif guestType == 'c':
                numChild +=1
            elif guestType == 'a':
                numAdult +=1
            else:
                print ("Invalid age entered. Please enter a valid age or guest will not be counted.")
                continue
            break
        except ValueError:
            print("Please enter a number for age.")

#Calculate costs
totalToddlerCost = numToddler * 0
totalChildCost = numChild * 125
totalAdultCost = numAdult * 155

totalCostForAll = totalToddlerCost + totalChildCost + totalAdultCost

#Print Ticket summary
print("\n----Ticket Summary----")
print (f"\n{'Ticket Type':40}{'QTY':20}{'Cost'}")
print ("-" * 65)
print (f"{'Adult (ages 10+) - $155.00':40}{numAdult:<20}${totalAdultCost:,.2f}")
print (f"{'Child (ages 3 - 9) - $125.00':40}{numChild:<20}${totalChildCost:,.2f}")
print (f"{'Toddler (ages 0 - 2) - FREE':40}{numToddler:<20}${totalToddlerCost:,.2f}")
print ("-" * 65)
print (f"{'Total cost:':60}${totalCostForAll:,.2f}")

#----Ride Tracker Section----

rides = ["Pirates of the Caribbean",
"Haunted Mansion",
"Space Mountain",
"The Matterhorn",
"Big Thunder Mountain Railroad",
"Autopia",
"Millennium Falcon",
"Rise of the Resistance",
"Snow White's Enchanted Wish",
"Peter Pan's Flight"]

waitTimes = [15, 13, 60, 45, 35, 25, 45, 85, 40, 45]

#Add new rides
while True:
    enter_another = input ("\nWelcome to Disneyland Ride Tracker App \U0001F3F0 \U0001F478 ! Enter another ride? (y/n): ")
    if enter_another == 'y':
      new_ride = input("Enter ride name: ")

      while True:
        try:
            new_waitTime = int(input(f"Enter wait time for {new_ride} in minutes: "))
            break
        except ValueError:
            print("Please enter a valid number for wait time.")

        # Append new values to lists
        rides.append(new_ride)
        waitTimes.append(new_waitTime)
    
    elif enter_another == 'n':
        break
    else:
        print("Please enter 'y' or 'n'.")
    
#Print ride summary
print("\n----Ride Summary----")
print(f"\n{'RIDE':<55}{'WAIT TIME (Min)':>15}")
print("-" * 70)

#average wait time
total_waitTime = 0
avg_wait = 0
index_lowest = 0
index_highest = 0

for i in range(len(rides)):
    print(f"{rides[i]:<55}{waitTimes[i]:>15}")
    total_waitTime += waitTimes[i]  #cumulative total for average
    
    #isolate index for the shortest wait time
    if waitTimes[i] < waitTimes[index_lowest]:
        index_lowest = i
        
    #isolate index for the longest wait time
    if waitTimes[i] > waitTimes[index_highest]:
        index_highest = i
    
avg_wait = total_waitTime / len(waitTimes)

print(f"\nAverage wait time for all rides: {avg_wait:.1f} minutes")
print(f"\nShortest wait time: {rides[index_lowest]} - {waitTimes[index_lowest]:.1f} minutes.")
print(f"\nLongest wait time: {rides[index_highest]} - {waitTimes[index_highest]:.1f} minutes.")
print("\nThank you for using the Ultimate Disneyland App!")
print("\nEnjoy your stay at Disneyland, the happiest place on Earth! \U0001F3F0 ")
