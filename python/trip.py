"""Get info from user:
    1 - What is their destination
    2 - What sights they would like to visit (there could be multiple)
    3 - What would you like to eat? (one meal)
====Sample Output====
Destination: Washington, DC (user shouldn't have to enter comma)
Sights you will visit:
    - Visiting the Washington Monument
    - Vistiing the Air and Space Museum
    - Visiting the White House
You will eat: Bugergers and Fries
You will spend
"""
destination_state = ""
while len(destination_state) != 2:
    destination_state = raw_input("What is your state destination? ")
destination_city = raw_input("What is your city destination? ")
sights_amt = int(raw_input("How many sights will you visit? "))


"""multiple_sights = raw_input("List the sights you will visit ")
meal_name = raw_input("What would you like to eat(one meal)? ")

print "Destination: " + destination_city.capitalize + "," + desitnation """
