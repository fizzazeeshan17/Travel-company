# Declare variables/values

Budget_ticket = 500
Economy_ticket = 750
VIP = 2000
Bag_included = 200
Meal_included = 150
addbag = 0
addmeal = 0
choice = True

# Display ticket choices and ask user to input ticket type

print('''Ticket types:
1. Budget (500kr)
2. Economy (750kr)
3. VIP (2000kr)''')
print()
ticket_type = int(input(('Input ticket type >>')))
print()

# Add a loop

while ticket_type > 0 and ticket_type < 4:
    print('''Currently you have:
    0 bags(s) resgistered
    0 meal(s) registered''')
    print()
    break

# Add a loop
# Display main menu (Bag and meal choices) and ask the user to input choice
# Assign ticket prices to variables

while choice:
    print('''Here are your options:
    1. Add Bag (max1)
    2. Add Meal (max1)
    3. Remove bag
    4. Remove meal
    5. Finalize ticket''')
    choice = int(input(('Your choice >>')))
    print()
    if ticket_type == 1:
        ticket_total = Budget_ticket
    if ticket_type == 2:
        ticket_total = Economy_ticket
    if ticket_type == 3:
        ticket_total = VIP
    if choice == 1:
        if addbag == 0:
            addbag = 1
            print('Currently you have: \n', addbag,
                  'bags(s) resgistered \n', addmeal, 'meal(s) registered')
            print()
    elif choice == 2:
        if addmeal == 0:
            addmeal = 1
            print('Currently you have: \n', addbag,
                  'bags(s) resgistered  \n', addmeal, 'meal(s) registered')
            print()
    elif choice == 3:
        if addbag == 1:
            addbag = 0
            print('Currently you have: \n', addbag,
                  'bag(s) resgistered \n', addmeal,  'meal(s) registered')
            print()
    elif choice == 4:
        if addmeal == 1:
            addmeal = 0
            print('Currently you have: \n', addbag,
                  'bags(s) resgistered \n', addmeal,   ' meal(s) registered')
            print()
# Assign Bag and meal prices to variables

    if addbag == 1:
        Bag_included = 200
    else:
        addbag = 0
        Bag_included = 0
    if addmeal == 1:
        Meal_included = 150
    else:
        addmeal = 0
        Meal_included = 0
# Display receipt
    if choice == 5:
        print('Receipt:')
    if ticket_type == 3 and Bag_included == 0 and Meal_included == 0:
        print(f'Ticket : {ticket_total}kr')
        print('-------'.rjust(15))
        Total = ticket_total
        print(f'Total  : {Total}kr')
        break
    elif (choice == 5 and Bag_included == 200 and Bag_included == 0 or
          choice == 5 and Meal_included == 150 and Meal_included == 0 or
          choice == 5 and Bag_included == 0 and Meal_included == 0):
        print(f'Ticket :  {ticket_total}kr')
        print('-------'.rjust(15))
        Total = ticket_total
        print(f'Total  :  {Total}kr')
        break
    elif choice == 5 and Bag_included == 200 and Meal_included == 150:
        print(f'Ticket : {ticket_total }kr')
        print(f'Bag    :  { Bag_included }kr')
        print(f'Meal   :  { Meal_included}kr')
        print('-------'.rjust(15))
        Total = Bag_included + Meal_included + ticket_total
        print(f'Total  : {Total}kr')
        break
    elif choice == 5 and Bag_included == 200:
        print(f'Ticket :  {ticket_total}kr')
        print(f'Bag    :  { Bag_included}kr')
        print('-------'.rjust(15))
        Total = Bag_included + ticket_total
        print(f'Total  :  {Total}kr')
        break
    elif choice == 5 and Meal_included == 150:
        print(f'Ticket :  {ticket_total }kr')
        print(f'Meal   :  { Meal_included}kr')
        print('-------'.rjust(15))
        Total = Meal_included + ticket_total
        print(f'Total  :  {Total}kr')
        break
# The End
