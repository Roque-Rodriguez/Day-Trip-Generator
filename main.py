import random

#List of Options
destination_list = ["Miami", "New York City", "Chicago", "Las Vegas", "Los Angeles"]
restaurant_list = ["Versailles", "Kat's Delicatessen", "Burt's Place", "Primal Steakhouse", "n/naka"]
transportation_list = ["Car", "Train", "Plane", "Helicopter", "Scooter", "Skate Board", "Walking"]
entertainment_list = ["Beach", "Baseball Game", "Football Game", "Gamble", "Art", "Dance"]

 
# Makes random decision from list
destination = random.choice(destination_list)
resturant = random.choice(restaurant_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)

# Makes a first Generic Proposol for trip

generated_trip = (f" For this trip we have picked that you should land in {destination}, go eat at this delicious resturant {resturant}, all while getting to your entertainment on a {transportation} to enjoy {entertainment}")

print(generated_trip)

#check to see if cx is satified
satified = (input("Are you satified with the choices? Press y for yes or n for no "))

if satified == "n":
    change = input("Which would you like to change? d for Destination, r for resturant, t for transportation, e for entertainment, or a for all?")
    if change == "d":
        destination = random.choice(destination_list)
        print(f"Your new destination is {destination}")
    if change == "r":
        resturant = random.choice(restaurant_list)
        print(f"Your new resturant of choice is {resturant}")
    if change == "t":
        transportation = random.choice(transportation_list)
        print(f"Your new form of transportation is {transportation}")
    if change == "e":
        entertainment = random.choice(entertainment_list)
        print(f"Please enjoy your new form of entertainment: {entertainment}")
    if change == "a":
        print(f"Please enjoy your new trip {generated_trip}")
    



    



##I want to do a if statement if the cx chooses no it will lead to which option including all to change.  if Cx chooses yes then it will print out Please enjoy your day.
