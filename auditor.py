inventory = 0
Failed = 0

stock = input("Please enter the stock quantity:")

while stock != "quit":
    if not stock.isdigit() or stock < str(0):
        print("Invalid stock quantity. Please enter again!")
        stock =input("Please enter the stock quantity:")
        Failed += 1
    else:
        inventory += 1

print("Total Units Processed:", inventory)
print ("Number of Failed/Rejected Entries:", Failed, "units")

if inventory > 500:
    print("Inventory is exceeded.")
    