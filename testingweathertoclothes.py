import pandas as pd
from pathlib import Path
import re
import argparse
import sys
import json
import random
import matplotlib.pyplot as plt

#function takes in data & tells user the weather
df_filepath = Path(__file__).parent / "WeatherDataSet.csv"

def date_weather(filepath):
    """
    Determines the weather for a date in April 2024, based on the user inputted date.
        Args: 
            string filepath to the csv file

        Raises:
            ValueError: User inputted date does not match the M/D/YYYY format 
        
        Raises:
            ValueError: User inputed date is not in the CSV dataframe

        Returns:
            string of the weather correpsonding to the date in the csv file
    """
    user_input = input("Input a date from April 2024 as M/D/YYYY, ie. 4/1/2024")
    try:
        date_pattern = r"(?P<month>\d{1})(?P<slash1>\/)(?P<day>\d{1,2})(?P<slash2>\/)(?P<year>\d{4})"
        match = re.search(date_pattern,user_input)
               
    except: 
        raise ValueError("Format is incorrect. Ensure you are using the M/D/YYYY")

    #call date weather function with file path in my function to call it
    month = int(match.group("month"))
    day = int(match.group("day"))
    year =int(match.group("year"))

    if month != 4 or day < 1 or day > 30 or year != 2024:
        raise ValueError ("Ensure that the date entered as a date in April 2024")
    df = pd.read_csv(filepath) #loads the dataframe
    
    df_date = df.loc[df["Date"]==user_input] #filters just the row of data where the user_input = date
    if len(df_date) > 0:
        weather = df_date.iloc[0]["Weather"]
        return weather
    else:
        print("Check the format of your date") 
    
def suggest_outfit_based_on_weather(weather):
        with open("weathertoclothing.json", "r", encoding="utf-8") as weather_for_clothing_file:
            clothing_data = json.load(weather_for_clothing_file)
        if weather in clothing_data:
            weather_clothing = clothing_data[weather]
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
        return (outfit_suggestions_from_weather) 

