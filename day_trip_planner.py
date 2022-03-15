destinations = ['Milwaukee', 'Chicago', 'Madison', 'Green Bay']
restaurants = ['AJ Bombers', 'Portillos', 'The Old Fashioned', 'Culvers']
transportation = ['rental car', 'personal vehicle', 'train', 'bus', 'airplain']
entertainment = ['Milwaukee Art Museum', 'National Mustard Museum', 'Lincoln Park Conservatory', 'Lambeau Field']
import random
def find_destination(passed_in_destinations):
    random_destination = random.choice(passed_in_destinations)
    print("I chose", random_destination, "for your destination. Is this acceptable? y/n: ")
    destination_input = input("")
    while destination_input == "n":
        random_destination = random.choice(passed_in_destinations)
        print("How about", random_destination, "? y/n: ")
        destination_input = input ("")
        if destination_input == "y":
            print("Sweet, let's pick out a trasportation method!")
    
    return random_destination

def find_transport(passed_in_transportation):
    transportation = random.choice(passed_in_transportation)
    print("I chose", transportation, "for your mode of trasport. Is this acceptable? y/n: ")
    transport_input = input("")
    while transport_input == "n":
        transportation = random.choice(passed_in_transportation)
        print("How about", transportation, "? y/n: ")
        transport_input = input("")
        if transport_input == "y":
            print("Awesome, let's pick out some entertainment!")

    return transportation

def find_entertainment(passed_in_entertainment):
    entertainment = random.choice(passed_in_entertainment)
    print("I chose", entertainment, "for your entertainment. Is this acceptable? y/n: ")
    entertainment_input = input("")
    while entertainment_input == "n":
        entertainment = random.choice(passed_in_entertainment)
        print("How about", entertainment, "? y/n: ")
        entertainment_input = input("")
        if entertainment_input == "y":
            print("Cool, now let's pick out something to eat while you're there!")
    
    return entertainment

def find_restaurant(passed_in_restaurant):
    restaurants = random.choice(passed_in_restaurant)
    print("I chose", restaurants, "for your restaurant. Is this acceptable? y/n: ")
    restaurant_input = input("")
    while restaurant_input == "n":
        restaurants = random.choice(passed_in_restaurant)
        print("How about", restaurants, "? y/n: ")
        restaurant_input = input("")
        if restaurant_input == "y":
            print("All done! Let's review your trip one more time.")
    
    return restaurants

def confirm_trip():
    confirmed_dest = find_destination(destinations)
    confirmed_transport = find_transport(transportation)
    confirmed_entertainment = find_entertainment(entertainment)
    confirmed_restaurant = find_restaurant(restaurants)
    print("OK! Your trip has been generated. Let's go over your trip and get confirm these options.")
    print("Your destination is:", confirmed_dest)
    print("Your transport will be:", confirmed_transport)
    print("Your entertainment will be:", confirmed_entertainment)
    print("You will be eating at:", confirmed_restaurant)
    print("Please confirm? y/n: ")
    trip_input = input("")
    if trip_input == ("y"):
        print("Wonderful! You will be going to", confirmed_dest, "via", confirmed_transport, "to visit", confirmed_entertainment, "and you will be dining at", confirmed_restaurant), "!"
    else:
        print("I'm sorry. Try again, and I'll think of something new.")

confirm_trip()