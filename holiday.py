"""
This program assists a customer to determine the cost of a chosen holiday. 
"""
print("Welcome to Flight and Sight, Done Right!")
print("We assist you in all your holiday cost needs!")
print("First, here the flight destinations you may choose from: ")
print("1. London\n" + "2. Dubai\n" + "3. Barcelona\n" + "4. Bangkok")
city_flight = input("Please enter your chosen destination from the list: ")
print("Excellent choice! Next, we need to know how long you intend to stay")
num_nights = int(input("Enter the number of nights stay at a hotel: "))
print("Exciting! Finally, we need details on any plans for car rental")
rental_days = int(input("Enter the number of days a car will be rented for: "))
print("Thank you for providing us with all the required information!")
print("We will now return the costs of the following to you: ")
print("1. Flight(s)\n" + "2. Accommodation\n" + "3. Car rental")
print("Once these are yielded, the total cost of your holiday will be returned!")

def plane_cost(city_flight):
    """
    Calculate the cost of the flight from the chosen travel destination

    Argument(s):
    city_flight: chosen destination yields cost of travel.
    """
    # Provide pricing options based on destination selected.
    if city_flight.lower() == "london":
        return 20000
    elif city_flight.lower() == "dubai":
        return 13000
    elif city_flight.lower() == "barcelona":
        return 23000
    elif city_flight.lower() == "bangkok":
        return 12000
    else:
        return 0
    
def hotel_cost(num_nights, city_flight):
    """
    Calculate the cost of hotel accommodation from the destination choice
    
    Argument(s):
    num_nights: number of nights chosen for hotel stay
    city_flight: chosen destination yields cost of travel 
    """
    # Provide pricing options based on destination selected.
    if city_flight.lower() == "london":
        return num_nights * 1000
    elif city_flight.lower() == "dubai":
        return num_nights * 2000
    elif city_flight.lower() == "barcelona":
        return num_nights * 1200
    elif city_flight.lower() == "bangkok":
        return num_nights * 500
    else:
        return 0

def car_rental(rental_days):
    """
    Calculate the cost of renting a car during stay

    Argument(s):
    rental_days: number of days for car rental
    """
    # Set car rental price established as an offer by the company.
    return rental_days * 800

def holiday_cost(city_flight, num_nights, rental_days):
    total = (plane_cost(city_flight) +
             hotel_cost(num_nights, city_flight) +
             car_rental(rental_days)
    )
    return total
# Defining the variable total when determining the total holiday cost.
total = holiday_cost(city_flight, num_nights, rental_days)
# Final prompts to the customer before presenting the cost of the holiday.
print("--------Holiday Cost Summary--------")
print(f"The cost of your flight amounts to: R{plane_cost(city_flight)}")
print(f"The cost of your hotel stay amounts to: R{hotel_cost(num_nights, city_flight)}")
print(f"The cost of your car rental amounts to: R{car_rental(rental_days)}")
print(f"Overall, the cost of your holiday trip amounts to: R{total}")