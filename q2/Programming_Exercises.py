# Exercise1 : Count even numbers from 2-20
for i in range(2, 21, 2):
  #starts from 2 ends in 20 because 21 isnt included, 2 is the increment
  print (i)

# Exercise2 : The Countdown Timer
i = 10
while i>=1:
  print(i)
  i -= 1
  # i starts at 10 and until it isnt equal to zero it will still follow the loop
else:
  print("Time is up!")

# Exercise3 : Skip Multiples (of three)
for i in range(1,16):
  # % means it gives what is left over after you divide it by three & 
  #the remainder of all multiples of three are 0 .
  if i % 3 == 0:
    #this skips the current value of i when it satisfies the condition then continues as normal
    continue
  print(i)

# Exercise4 : Multiplication Table Generator
def show_table(number):
  for i in range(1, 11):
    print(number * i)
#to make sure that the user strictly enters a number from 1-10 (baka kasi matigas ulo)
while True:
  try:
    number = int(input("Give me a number from 1 to 10: "))
    if 1 <= number <= 10:
      #to get out of the loop
      break  
    else:
      print("Please enter a number between 1-10.")
  except ValueError:
    print("Please enter an integer")
#calls the function
show_table(number)
