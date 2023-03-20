# Request user to enter the price of the package they would like to purchase
pkg_price = float(input("Please enter package price: "))

# Request user to enter the total distance of the delivery in kms
distance = float(input("Please enter the total distance of the delivery in kms: "))

# Request user to enter the delivery type of their choice
delivery_type = int(input("Please enter (1) for Air service or (2) for freight service: "))

# Request user to enter the type of insurance they need
insurance_type = int(input("Please enter (1) for full insurance or (2) for limited insurance: "))

# Request to choose if they need gift or not
gift_type = int(input("Please enter (1) for gift or (2) for no gift: "))

# Request user to choose if they need Prioritize or standard service
shipping = int(input("Please enter (1) Priority or (2) standard: "))

# list of variables and values needed through the task

if delivery_type == 1:
    delivery_value = distance * 0.36
else:
    delivery_value = distance * 0.25

if insurance_type == 1:
    insurance_value = 50.00
else:
    insurance_value = 25.00

if gift_type == 1:
    gift_value = 15.00
else:
    gift_value = 0.00

if shipping == 1:
    ship_value = 100.00
else:
    ship_value = 20.00

# Add up the total cost of package based on selection by user
total_cost = delivery_value + pkg_price + insurance_value + gift_value + ship_value
print(f"Your total cost is R{total_cost}")
