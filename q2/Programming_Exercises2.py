#1 : My School Bag
school_items = ["notebook","pen",'calculator','laptop','book']

print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])
print()
print(school_items[0])
print(school_items[4])

#2 : 
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

for place in destinations:
    print(place)
print()
print(destinations[1:4])
print()
search_place = input("Enter a destination to search for: ")

if search_place in destinations:
    print(search_place + " exists in the list.")
else:
    print(search_place + " does not exist in the list.")
print()
destinations[2] = "Iloilo"
print(destinations)
