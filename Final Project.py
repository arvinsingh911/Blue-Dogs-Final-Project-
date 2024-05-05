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
    

# filtering the data for the bar graph
# addd doc string
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

   

def parse_args():
    """
        Parses command-line arguments Smart Outfit Planner.

    This function uses ArgumentParser to parse command-line arguments \
        provided by the user.
    The arguments include:
    name: User's name (required)
    age: User's age (optional, must be a positive integer)
    Date: Date conditions (optional)
    occasion: Occasion for the outfit (optional)

    Returns:
        dict: A dictionary containing the parsed arguments.
            name: User's name (str)
            age: User's age (int)
            date: The date  (str or None)
            occasion: Occasion for the outfit (str or None)

    Raises:
        ValueError: If required arguments are missing or if age is \
            not a positive integer.
    """
    parser = argparse.ArgumentParser(description="Smart outfit planner")
    
    # The command line arguments 
    # User will enter name, age(int), date, occasion
    parser.add_argument("name",type = str, help = "The name of the user")
    parser.add_argument("age",type = int, help = "The age of the user")
    parser.add_argument("date",type = str, help = "The date")
    parser.add_argument("occasion",type = str, help = "Occasion for the outfit")
    
    if not args.name:
        raise ValueError('Name is required.')
    
    if args.age is not None and args.age <= 0:
        raise ValueError('Age must be a positive integer.')
    
    return {
        'name': args.name,
        'age': args.age,
        'date': args.date,
        'occasion': args.occasion
    }
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])


#Arvin here is my testing with the arg parse, fix yours and delete
"""AccessoriesDict = {1: "Sunglasses", 2: "Chain", 3: "Diamond Ring", #dictionary needed for random accessories
                   4: "Loop Earings", 5: "Apple Watch"}



def parse_args():
    parser = argparse.ArgumentParser(description="Smart outfit planner")

    parser.add_argument("-accessory", type=int, default = 0) #argument parser -accessory is need to be optional and not positional
    args = parser.parse_args()
    return args
    

    

    
    # if args.num_accessories is not None and args.num_accessories > 5:
    #     raise ValueError('You cant have more than five accessories')
    
    #return {

        #'accessory' : args.accessory
    #}
    
if __name__ == "__main__":
    args = parse_args()"""


class Outfit():
    """outfit class
    """
    #outfit class to be full developed later with clothing items/outfits
    #needs to add sections of clothing in here
    
    
    def __init__(self):
        """this function initializes the accessories list
        """
        self.accessories = [] #list creation for accessories
    

    def addAccessory(self, accessorynum = 0): #default accessories on an outfit is 0
        """Adds string "None" to accessory list in this instance of the 
        class. If the calling function has a second parameter that parameter
        is added to the accessory list instead of "None" as the default
        

        Args:
            accessory (str, optional): A string to be added to the list of 
            accessories in this instance of the class. Defaults to "jewlery".
        """
        for i in range(accessorynum): #the user enters a number in the command line anywhere from 0 - 5 
            self.accessories.append(AccessoriesDict[random.randint(1, 5)]) 
        if accessorynum == 0: #if user never puts in a value the defualt is 0 but if they put 0 in still works the same
            self.accessories.append("None") #no ccessories paired with the outfit so accesories is none
            
#testing  
myoutfit = Outfit() #outfit is not paired to outfit class
myoutfit.addAccessory(args.accessory) #calls the function
print(myoutfit.accessories) #prints the function





# Asa Agyemangs function for outfit suggetsions based on weather type
def suggest_outfit_based_on_weather(weather_data):
    weather = weather_data["Weather"].iloc[0]
    with open("weathertoclothing.json", "r", encoding="utf-8") as weather_for_clothing_file:
        clothing_data = json.load(weather_for_clothing_file)
    if weather in clothing_data:
        weather_clothing = clothing_data[weather]
    else:
        raise ValueError(" No weather found for this date ")
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







# init needs to include parameter for list 

# Assuming you have already called the date_weather function and stored its result in weather_data
outfit_suggestion = suggest_outfit(date_weather)
print("Recommended outfit of the day:", outfit_suggestion)

def choose_random_outfit(json_file):
    """Randomly choose's clothing items from a JSON file and prints the outfit

    Args:
    json_file (str): The path to the JSON file containing three dictionaries: \
        'shirts', 'pants', and 'shoes'
        
    Side Effects:
        Prints to the user a potential outfit
    """
    with open(json_file, "r", encoding = "utf-8") as file:
        data = json.load(file)
    
    shirt = random.choice(data['shirts'])
    pants = random.choice(data['pants'])
    shoes = random.choice(data['shoes'])
    
    print("The outfit created based upon the clothes within your closet is: \
        Shirt: {shirt} Pants: {pants} Shoes: {shoes}")

# Example usage (can delete this and the comment below if needed)
# choose_random_outfit('clothes.json')


