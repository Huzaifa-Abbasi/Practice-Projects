'''Question 1: Crop Monitoring System
Imagine you are developing a Crop Monitoring System for farmers. Write a Python function 
monitor_crop(temperature, humidity, rainfall) that takes environmental conditions as input and returns 
"Watering needed" if the humidity is low and rainfall is below average, and "Optimal conditions" 
otherwise'''

def monitor_crop(temperature, humidity):
    condition = (temperature, humidity)
    return condition

environmental_condition = input("Enter Environmental condition? ") == "clean"
temperature = int(input("Enter the temperate? "))
humidity = int(input("Enter the Humidity? "))
rainfall = input("Rainfalls Yes/No? ") == "no"
if temperature >= 45 and humidity <=20 and rainfall == True and environmental_condition == True:
    print("Water needed")
else:
    print("No Need Water")

condition = monitor_crop(temperature, humidity)

print(condition)