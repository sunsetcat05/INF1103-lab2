inventory = 0
Failed = 0

stock = input("Please enter the stock quantity:")

while stock <= 500:
    if not stock.isdigit() or stock < 0:
        print("Invalid stock quantity. Please enter again!")
        stock = input("Please enter the stock quantity:")
        Failed += 1
    else:
        inventory += 1
    if stock == "quit":
        print("Total Units Processed:", inventory)
        print ("Number of Failed/Rejected Entries:", Failed, "units")

if inventory > 500:
    print("Inventory is exceeded.")
    