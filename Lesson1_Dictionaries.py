# Real-World Python Dictionary Applications

# Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Adding 2 Beverages to menu
restaurant_menu.update({
    "Beverages": {"Coca-Cola": 2.99, "Lemonade": 1.99}
})
print(restaurant_menu)

# Updating price of steak
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

# Removing an item from the menu
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)


# Python Progamming Challenges for Customer Service Data Handling

# Task 1 Customer Service Ticket Tracker

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id():  # created a function that will return an id I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct? y/n")
        if correct == 'y': # create ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else: #go back to the top of the while loop (skip to the next iteration)
            continue

def update_status():
    while True:
        try:
            ticket_number = int(input("Please enter ticket number you would like to update: ")) # enter the ticket number you would like to update. User input will be an int.
            if ticket_number in service_tickets: # for ticket number in service tickets 
                service_tickets[ticket_number]["Status"] = "closed" # if the ticket number status is opened change to closed
                print(service_tickets[ticket_number])
                confirmation = input("Is this information correct? y/n ") # confirm your information
                if confirmation == "y":
                    break
                else:
                    continue
            else:
                print("Invalid input. Please try again.")
        except:
            print("Please enter a valid input. ")
            continue

def display(): # Dispay service tickets
    while True:
        print(service_tickets)
        break

def quit(): # If quit print have a good day.
    while True:
         print("Thanks for making a service ticket. Have a good day!")
         break



def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1- Open a new service ticket.
    2- Update the status of an existing ticket  to "closed".
    3- Display all tickets.
    4 - Quit
''')
        if ans == '1':
            new_ticket() # function to add a new ticket
        elif ans == '2':
            update_status() # funtion to update an existing ticket
        elif ans == '3':
            display()  # function to display all tickets
        elif ans == '4':
            quit() # function to quit 
        else:
            print("Please enter the correct number")
        
main()