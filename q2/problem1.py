#Program Requirements
#1. Ask for the item's price, quantity, and payment.
#2. Pass the price and quantity as arguments to calculate_total().
#3. Store the returned total in a variable.
#4. Pass the payment and the computed total to calculate_change().
#5. Display the total cost and the customer's change.
#6. If payment is insufficient, display the additional amount needed instead of a negative change.

# -------- PROGRAM ---------

def calculate_total(price, quantity):
  return price * quantity
# calculates & returns the total cost from the items bought 
# price and quantity are placeholder variables (parameters)
# return is for the time you will print the final receipt

def calculate_change(payment, total):
  return payment - total  
# how much change is given back to the customer
# payment is a placeholder variables

price = float(input("Enter items price: "))
quantity = int(input("Enter how many/quantity: "))
payment = float(input("Enter payment: "))
# these are the arguments and these are the ones that will go into their respective values after having the input from the user. 

total = calculate_total(price, quantity)
change = calculate_change(payment, total)

if change >= 0:
  print(f"Your change is PHP{change:.2f}")
else:
  print("You need to pay", change * -1, "more")

print("Your total is: ", total)
print("Your change is:", change)

# Its useful to separate the total and the change to improve code organiztion & how easy it'll be to read and fix for future errors




# big credit goes to the helpful volunteers & jessie beside me to know what to do in this program
# (Arcilla, Remodo, basta mga nag code sa harap... I just wrote it down am sorry big credit talaga sainyo #Ilabyu)
