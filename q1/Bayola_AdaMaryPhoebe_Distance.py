print("Im gonna solve a distance a distance formula gimme your two points")

x1 = int(input("Mkay, enter x1: "))
y1 = int(input("Uhh, enter y1 too: "))

x2 = int(input("Erm, enter x2: "))
y2 = int(input("Lastly, enter y2: "))

import math 

distance = math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

rounded_distance = round(distance, 2)

print(f"Okay so the distance between the two points are :{rounded_distance}")

#Reflection :
#the Math library helped me in a way that my code is shorter, if it never existed I would have declared more variables and maxed out the simple operations.
#sqrt() & pow() helped to not give me more complex calculations since its built in by the nice people in the world that dont even want credit (half-joking) and is more effiecient and practical than doing it from scratch from the sake of convienience.
