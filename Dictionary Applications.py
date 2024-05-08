# 1. Real-World Python Dictionary Applications
# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. 
# You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. 
# This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.

restaurant_menu["Desserts"]["Beverages"] = {"Sparkling Water": 1.99, "Coffee": 3.99, "Juice": 5.99}
print(restaurant_menu)

# Update the price of "Steak" to 17.99.

restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

# Remove "Bruschetta" from "Starters".

del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

# 2. Python Programming Challenges for Customer Service Data Handling
# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. 
# You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
#  - Open a new service ticket.
#  - Update the status of an existing ticket.
#  - Display all tickets or filter by status.
#  Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

def open_ticket(service_tickets):
    customer = input("Enter your full name: ").title()
    issue = input("Briefly describe your issue: ").title()
    # Check if service_tickets dictionary is empty:
    if not service_tickets:
        ticket_number = 0
    else:
        ticket_number = len(service_tickets)
    # Then:
    if customer and issue:
        ticket_number += 1
        ticket_key = f"Ticket{ticket_number}"
        # Create a new ticket with customer name, issue, and status:
        service_tickets[ticket_key] = {"Customer": customer, "Issue": issue}
        service_tickets[ticket_key]["Status"] = "open".title()  # Capitalize status
    elif customer and not issue.strip():    # Check if issue description is blank
        print("Error: The issue description cannot be blank")
    elif not customer.strip():      # Check if customer name is blank
        print("Error: The customer name cannot be blank")
    return service_tickets

def update_status(service_tickets):
    name = input("\nWhose ticket was resolved? ").lower()
    ticket_number = 0
    ticket_present = False
    for ticket_key, ticket_subkey in service_tickets.items():
        ticket_number += 1
        if ticket_subkey["Customer"].lower() == name.lower():   # Check if customer has a ticket
            ticket_present = True
            if ticket_subkey["Status"] == "Open":
                # Change ticket status to Closed if it's Open
                service_tickets[ticket_key]["Status"] = "Closed"
                print(f"Ticket {ticket_key} belonging to {name.title()} has been closed.")
                print(service_tickets)
            else:
                print(f"Ticket {ticket_key} belonging to {name.title()} is already closed.")
                print(service_tickets)
    
    if not ticket_present:  # Print a message if no ticket is found for the specified customer
        print(f"No tickets found for {name.title()}.")

    return service_tickets

    
def filter_tickets(service_tickets):
    tickets_by_status= input("\nWould you like to see your open or closed tickets? ").lower()
    ticket_number = 0
    if tickets_by_status in ["open", "closed"]:     # Check if input is valid
        if service_tickets:
            ticket_present = False
            for ticket_key, ticket_subkey in service_tickets.items():
                ticket_number += 1
                if tickets_by_status == "open" and ticket_subkey["Status"] == "Open":
                    print(f"{ticket_key} is open:")
                    print(ticket_subkey)
                    ticket_present = True
                elif tickets_by_status == "closed" and ticket_subkey["Status"] == "Closed":
                    print(f"{ticket_key} is closed:")
                    print(ticket_subkey)
                    ticket_present = True
                else:
                    ("Please enter a valid response!")
            if not ticket_present:
                print(f"No {tickets_by_status} tickets found.")
        else:
            print("You don't have any tickets opened!")
    else:
        print("Please enter a valid response! Open/Closed: ")
    
    return service_tickets

def service_tracker():
    # Initialize an empty dictionary to store service tickets
    service_tickets = {}

    while True:
        print("\nWelcome to Customer Service Ticket Tracker!")
        print("\nMenu:")
        print("1. Open a new service ticket")
        print("2. Update the status of an existing ticket")
        print("3. Filter tickets by status")
        print("4. Quit")

        choice = input("\nWhat would you like to do? Enter your choice from 1 to 4: ")
        if choice == "1":
            service_tickets = open_ticket(service_tickets)
            print(service_tickets)
        elif choice == "2":
            service_tickets = update_status(service_tickets)
        elif choice == "3":
            service_tickets = filter_tickets(service_tickets)
        elif choice == "4":
            print("Thank you for using our service ticket tracker!")
            break
        else:
            print("Please enter a valid response!")
# Call the main function to start the program
service_tracker()