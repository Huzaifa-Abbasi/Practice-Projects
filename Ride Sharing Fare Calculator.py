'''Question 3: Ride-Sharing Fare Calculator
You are working on a Ride-Sharing Fare Calculator. Develop a Python function calculate_fare(distance, 
time_of_day) that takes the distance of the ride and the time of day as input and returns the fare. Apply 
a 20% surcharge during peak hours (8 am - 10 am and 5 pm - 7 pm) and a 10% discount for late-night 
rides (10 pm - 5 am).'''

def calculate_fare(distance):
    fare = distance * price_per_kilometer
    return fare

price_per_kilometer = 100
distance = int(input("Enter your Distance in Km "))
time = int(input("Enter the Current Time "))

if 8 >= time <= 10 or 17 >= time <= 19:
    price_per_kilometer += price_per_kilometer * 0.2
    print("the amount of your share is ",calculate_fare(distance))
else:
    price_per_kilometer  *= 0.9
    print("the amount of your share is ",calculate_fare(distance))