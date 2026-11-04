def calculate_average(pages,price_per_page):
  return pages * price_per_page
  
def calculate_balance(payment,total_cost):
  return payment - total_cost

pages = float(input("Enter how many pages you'll print: "))
price_per_page = int(input("Enter price per page : "))
payment = float(input("Enter payment: "))

total_cost = calculate_average(pages,price_per_page)
balance = calculate_balance(payment,total_cost)


print("Your total printing cost is: ", total_cost)

if balance >= 0:
  print(f"Your remaining balance is: {balance:.2f}")
else:
  print("Your payment is insufficient, please pay ", balance * -1, "more")
