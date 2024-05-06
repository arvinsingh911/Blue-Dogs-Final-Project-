# project_testing
import pandas as pd
from pathlib import Path
import re
import argparse
import sys
import matplotlib.pyplot as plt
import random
import json


#function takes in data & tells user the weather

import random

# Dictionary for random accessory selection
AccessoriesDict = {1: "Sunglasses", 2: "Chain", 3: "Diamond Ring", 4: 
    "Loop Earrings", 5: "Apple Watch"}

def addAccessory(accessorynum=0):
    accessories = []
    if accessorynum == "" or int(accessorynum) == 0:
        accessories.append("No accessories added")
    else:
        for i in range(int(accessorynum)):
            accessories.append(AccessoriesDict[random.randint(1, 5)])
    return accessories


accessorieslist = addAccessory(input("Enter how many accessories you want added to your outfit 1-5, or enter 0 or nothing if you dont want accessories"))
print(accessorieslist)

df_filepath = Path(__file__).parent / "WeatherDataSet.csv"

def weather_filter(filepath):
    df = pd.read_csv(filepath)
    df_counts = df.groupby("Weather").count().reset_index()
    df_counts = df_counts.rename(columns={"Date":"Number of Days"}) #changes the 2nd colunm name from Date to Number of Days 

    # creates a new df w/ the counts of the occurences of each weather type
    # used the reset_index method, so that this df can have a default numbered index 
    # before the reset_index function the weather colunm was the index and a series 
    df_counts.plot.bar(x = "Weather", y="Number of Days")
    plt.show()
    return df_counts

def date_weather(filepath):
    """
    Determines the weather for a date in April 2024, based on the user inputted date.
        Args: 
            stri filepath to the csv file
        Returns:
            string of the weather correpsonding to the date in the csv file
    """
    #add doc string for the function 
    user_input = input("Input a date from April 2024 as M/D/YYYY, ie. 4/1/2024: ")
    try:
        date_pattern = r"(?P<month>\d{1})(?P<slash1>\/)(?P<day>\d{1,2})(?P<slash2>\/)(?P<year>\d{4})"
        match = re.search(date_pattern,user_input)
           
    except:
        raise ValueError("Format is incorrect. Ensure you are using the M/D/YYYY")

     # check to make sure that date is in the range, use logicical epxresions if, else etc.
    month = int(match.group("month"))
    day = int(match.group("day"))
    year =int(match.group("year"))

    if month != 4 or day < 1 or day > 30 or year != 2024:
        raise ValueError ("Ensure that the date entred as a date in April 2024")
    

    df = pd.read_csv(filepath) #loads the dataframe
    #date_column = df.loc[:"Date"] #acesses the data in the date column
    
    df_date = df.loc[df["Date"]==user_input] #filers just the row of data where the user_input = date
    if len(df_date) > 0:
        weather = df_date.iloc[0]["Weather"]
        return weather
        #select the value at 1st row & the 2nd colunm 
        #save that value to weather variable
    else:
        print("Check the format of your date") #should this be a return or try/except?

    
def recommend_sizes():
    while True:
        try:
            weight = int(input('Enter your weight (in pounds): '))
            if weight <= 0:
                raise ValueError('Weight must be a positive number.')

            body_type = input('Enter your body type (Slim/Average/Muscular): ')
            if body_type.lower() not in ['slim', 'average', 'muscular']:
                raise ValueError('Invalid body type. Please enter "Slim", "Average", or "Muscular".')

            
            top_size = 'S' if weight < 150 else ('M' if weight < 180 else 'L+')
            pants_size = '28-30' if weight < 150 else ('31-33' if weight < 180 else '34-36+')
            shoe_size = '8' if weight < 150 else ('9' if weight < 180 else '10+')

            
            print(f'Based on your weight ({weight} lbs) and body type ({body_type}), you should wear:')
            print(f'Top Size: {top_size}')
            print(f'Pants Size: {pants_size}')
            print(f'Shoe Size: {shoe_size}')

            break  
        except ValueError as e:
            print(f'Error: {e}')
            continue


def suggest_outfit_based_on_weather(weather_data):
    with open("weathertoclothing.json", "r", encoding="utf-8") as weather_for_clothing_file:
        clothing_data = json.load(weather_for_clothing_file)
    if weather_data in clothing_data:
        weather_clothing = clothing_data[weather_data]
    else:
        raise ValueError(" No outfits can be created for this type of weather! ")
    # list of randomized outfits
    outfit_suggestions_from_weather = []
    for i in range(3):
        #randomized items from (shirt, pants, shoes) to create outfit
        shirt = random.choice(weather_clothing["shirts"])
        pants = random.choice(weather_clothing["pants"])
        shoes = random.choice(weather_clothing["shoes"])
        # custom dict for the 3 outfit suggestions
        outfit = {
            "Shirt": shirt,
            "Pants": pants,
            "Shoes": shoes
        }
        outfit_suggestions_from_weather.append(outfit)
    return outfit_suggestions_from_weather




# add Asa's fucntion & the try except
recommend_sizes()
print(date_weather("WeatherDataSet.csv"))
print(weather_filter("WeatherDataSet.csv"))

#  weather for the given date
try:
    weather = date_weather("WeatherDataSet.csv")
except ValueError as problem:
    print(f"Error getting weather: {problem}")
    weather = None

# If weather works then suggest outfits
if weather:
    try:
        outfit_suggestions = suggest_outfit_based_on_weather(weather)
        print("Outfit suggestions based on weather:")
        for outfit in outfit_suggestions:
            print(outfit)
    except ValueError as problem:
        print(f"Error suggesting outfits: {problem}")
else:
    print("Weather data unavailable, skipping outfit suggestions.")
