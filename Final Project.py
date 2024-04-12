import pandas as pd
import argparse
import sys

#function takes in data & tells user the weather
df_filepath = "C:/Users/Maryl/OneDrive - University of Maryland/INST326/Blue-Dogs-Final-Project-/WeatherDataSet.csv"
#pd.read_csv(data_filepath)


def date_weather(filepath):
    user_input = input("Input the date as M/D/YYYY, ie. 4/1/2024")
    try:
        pd.to_datetime(user_input, dayfirst = True, errors = 'raise')    
    except ValueError:
        print("Format is incorrect. Ensure you are using the M/D/YYYY")

    df = pd.read_csv(filepath) #loads the dataframe
    #date_column = df.loc[:"Date"] #acesses the data in the date column
    
    df_date = df.loc[df["Date"]==user_input] #filers just the row of data where the user_input = date
    if df_date.isin([user_input]):#get this checked
        weather = df_date.loc[0] #get this checked
        #add a conidtion, if ture extract the weather from the row, else send a message

        #df_date = df.loc[df["Date"]==user_input] #cretes a dataset of just the row
        #weather = df_date.at[0,0]

    else:
        print("Check the format of your date") #should this be a return or try/except?
    
    return weather
     
    #weather_column = dataset_weather.loc[:"Weather"]


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


class Outfit():
    
    #needs to add sections of clothing in here
    
    
    def __init__(self,):
        self.accessories = [] #list creation
    
    #custom arugment
    #this function takes in an outfit and adds 
    def addAcessories(self, *args):
        #loop through the arguments
        for accessory in args:
            self.accessories.append(accessory) #append each acessory
    
    
    #Sort the accessories by the length of the jewlery n
    #def sortAccessories(self):
        #return sorted(self.accessories, key=len)
            
  
#testing  
myoutfit = Outfit()
myoutfit.addAcessories("Sunglasses","Ear-Rings", "Chain")
print(myoutfit.sortAccessories())
print(myoutfit.accessories)
 
 # craeet a var for this list to be incorpiated into object
 
# outside the class and make a new instance of outfit class 
def suggest_outfit(date_weather):
    
    weather = date_weather["Weather"].iloc[0] 
    # This should extract the current weather info for the day user inputs
    
    # Linked conditional statements for suggesting clothing 
    
    # how do I have it pull from the clothing class? 
    
    # clothing words in string should be general but maybe each will be a key to 
    # more specifc values like ex) 
    
    # Tops : Longsleeve,Short sleeve,Crop Top,Sleeveless,Graphic Tee xyz
    # Bottoms : Blue Jeans, Jean shorts, Biker shorts, Gym shorts, Sweatpants, Leggings
    # Accessories : Sunglasses, Headband, Overhead headphones, Gold earrings/necklace
    # Shoes: Low top sneakers, High top sneakers, Uggs, Nike slides, Crocs, Birkenstocks
    
    #  dictionary 
    # include this in outfit class / as apart of the outfit class 
    # when you create a new outfit object as an instance of the class my function can process through my if/else stateemntts 
    '''rainy day accesories 
    rainy day shoes 
    raiiny day bottoms 
    raininy day xyz '''
#rain.math.choice(5)
# if raniny in date_weather: 
# outfit1=outfit

    if 'rainy' in date_weather :
        return ['Raincoat', 'Waterproof boots', 'Umbrella']
    elif 'hot' in date_weather:
        return ['Shorts', 'T-shirt', 'Sunglasses', 'Slides']
    elif 'cold' in date_weather:
        return ['Sweater', 'Sweatpants', 'Scarf', 'Beanie', 'Gloves']
    elif 'warm' in date_weather:
        return ['Shirt', 'Shorts', 'Sunglasses' , 'Sneakers']
    elif 'windy' in date_weather:
        return ['Hoodie', 'Sweatpants', 'Fluffy Socks', 'Crocs']
    else:
        return ['Weather is unpredictable. Dress accordingly.']

# init needs to include parameter for list 

# Assuming you have already called the date_weather function and stored its result in weather_data
outfit_suggestion = suggest_outfit(date_weather)
print("Recommended outfit for the day:", outfit_suggestion)


