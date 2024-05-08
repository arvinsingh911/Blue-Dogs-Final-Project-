import pandas as pd
from pathlib import Path
import re
import sys
import matplotlib.pyplot as plt
import random
import json
import random
from random import sample

global globstr 
globstr = "("
def recommend_sizes():
    """
    Recommends clothing sizes based on user's weight and body type. This function 
    prompts the user to enter their weight in pounds and their body type 
    (Slim/Average/Muscular). It then calculates and suggests the appropriate 
    clothing sizes (top, pants, and shoes) based on the input.
    
    Raises:
        ValueError: If weight is not a positive number or body type is not one 
        of 'Slim', 'Average', or 'Muscular'.
    
    """
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
recommend_sizes()

# Arvins Function that recomends what clothign type you should be looking for based on your heigth in inches 
def height_suggestions():
    """
    Suggests clothing styles, sizes, and accessories based on the user's height.
    
    Returns:
        str: A suggestion for clothing styles, sizes, and accessories based on height.
        
    Raises:
        ValueError: If number inputted is negative
    """
    while True:
        try:
            height = int(input("Enter your height in inches: "))
            if height <= 0:
                raise ValueError("Height must be a positive integer.")

            suggestion = ""
            if height < 60:
                suggestion = "Petite sizes and shorter hemlines may be more flattering. Consider small accessories like dainty jewelry."
            elif 60 <= height < 65:
                suggestion = "Standard sizes and regular hemlines are likely suitable. Accessories of moderate size and length are versatile."
            elif 65 <= height < 70:
                suggestion = "Standard sizes and regular hemlines are likely suitable. Accessories of moderate size and length are versatile. For bottoms, consider petite or short lengths."
            elif 70 <= height < 75:
                suggestion = "Tall sizes and longer hemlines may provide a better fit. Bold accessories and statement pieces can complement your height."
            elif height >= 75:
                suggestion = "Tall sizes and longer hemlines may provide a better fit. Bold accessories and statement pieces can complement your height. For bottoms, consider tall lengths."

            return suggestion
        except ValueError as e:
            print(f'Error: {e}')
            
print(height_suggestions())

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
    global globstr
    user_input = input("Input a date from April 2024 as M/D/YYYY, ie. 4/1/2024 ")
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
    globstr += user_input + ", "
    if len(df_date) > 0:
        weather = df_date.iloc[0]["Weather"]
        return weather
    else:
        print("Check the format of your date") 
    

# filtering the data for the bar graph
# addd doc string
def weather_filter(filepath):
    """
    Groups the occurrences of the weather for hot, warm, cold, cool and 
    windy and graphs a bar plot to show the number of occurreces for each weather 
    type.

    Args:
        string file path to the csv file 

    Side effects:
        Creates a bar graph that shows the occurrences of each weather type

    Returns:
        Returns a new data frame that shows that counts the number of occurrences 
        of each weather type
    
    """

    df = pd.read_csv(filepath)
    df_counts = df.groupby("Weather").count().reset_index()
    df_counts = df_counts.rename(columns={"Date":"Number of Days"}) #changes the 2nd colunm name from Date to Number of Days 
    # creates a new df w/ the counts of the occurences of each weather type
    # used the reset_index method, so that this df can have a default numbered index 
    # before the reset_index function the weather colunm was the index and a series 
    df_counts.plot.bar(x = "Weather", y="Number of Days")
    plt.show()
    return df_counts

#print(weather_filter("WeatherDataSet.csv"))

# Asa Agyemangs function for outfit suggetsions based on weather type
def suggest_outfit_based_on_weather (weather):
    '''
    Suggest a set of outfits based on the weather of a specific day 
    
    Takes the weather condition from the function above as input and suggest three 
    outfits based on clothing data from ('weathertoclothing.json') file which 
    is selected randomly
    
    Arguments : weather (str) A string version of weather condition 
    
    Returns: list[dict]: A list of dicts where each represents component of an outfit 
    
    Rasies: ValueError: If weather condiiton is not found in the json file then 
    no outfit will be created
    '''
    global globstr
    with open("weathertoclothing.json", "r", encoding="utf-8") as weather_for_clothing_file:
         clothing_data = json.load(weather_for_clothing_file)
    if weather not in clothing_data:
        raise ValueError(" No outfits can be created for this type of weather! ")
    # list of randomized outfits
    outfit_suggestions_from_weather = []
    for i in range(3):
        #randomized items from (shirt, pants, shoes) to create outfit
        shirt = random.choice(clothing_data[weather]["shirts"])
        pants = random.choice(clothing_data[weather]["pants"])
        shoes = random.choice(clothing_data[weather]["shoes"])
        # custom dict for the 3 outfit suggestions
        outfit = {
            "Shirt": shirt,
            "Pants": pants,
            "Shoes": shoes
         }
        globstr += f'Outfit {i + 1}: '
        globstr += f'Shirt:{shirt} '
        globstr += f'Pants:{pants} '
        globstr += f'Shoes:{shoes}, '
        outfit_suggestions_from_weather.append(outfit)
    return (outfit_suggestions_from_weather) 
    
    
weather = date_weather("WeatherDataSet.csv")
print(weather)
#print(date_weather("WeatherDataSet.csv"))
print(weather_filter("WeatherDataSet.csv"))

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

# Dictionary for random accessory selection
AccessoriesDict = {1: "Sunglasses", 2: "Chain", 3: "Diamond Ring", 4: 
    "Loop Earrings", 5: "Apple Watch"}

def addAccessory(accessorynum=0):
    """This function asks the users if they would like accessories to pair with
    their suggested outfits. The default is 0 which means no accessories are 
    added to the suggested outfit, this means the user could skip input or enter
    0 and the default would be returned. The user could enter any number from 
    1-5, which would result in that number of accessoried being added to their
    outfit, and is randomly ordered and assigned making this function use
    optional parameters.

    Args:
        accessorynum (int, optional): number of accessories to be added to the 
        suggested outfits which can range from 1-5 or even 0. Defaults to 0.

    Returns:
        list: returns a list of accessories to be paired with outfits
    """
    global globstr
    accessories = []
    if accessorynum == "" or int(accessorynum) == 0:
        accessories.append("No accessories added")
    else:
        list = [1,2,3,4,5]
        nums = sample(list, int(accessorynum))
        for num in nums:
            accessories.append(AccessoriesDict[num])
    
    globstr += 'Accesories: '
    for accessory in accessories:
        globstr += accessory + ' '
    globstr += ')'
    return accessories

accessorieslist = addAccessory(input("Enter how many accessories you want added to your outfit 1-5, or enter 0 or nothing if you dont want accessories: "))
print(accessorieslist)

def clothing_store_suggestions ():
    ''' 
    Suggets clothing stores based on the users style prefernces 
    
    This function will prompt the user to select a style prefernce from a set of
    valid choices then based on what the user chooses a list of stores will return
    if its found they associate with the set style (also it will be orgnized by 
    how pricy it is in terms of dollar signs)
    
    Arguments : No arguments but interacts with the user through input prompts 
    Returns: Prints stores orgnizaed by least to most expensive in console 
    Raises: Value Error If user selects an invlaid style preferance 
    
    
    '''
    
    stores_for_styles = {
        "Preppy" :[("Zara", "$" ),("Express" ,"$$" )],
        "Sophisitcated" :[("Ralph Lauren" ,"$$$" ),("White House Black Label" ,"$$$" )],
        "Comfy" :[("Uniqlo" ,"$" ),("My Comfort Online" , "$$")],
        "Vintage" :[( "Goodwill "," $" ),(" Buffulo Exchange" ,"$ " )],
        "Y2K" :[( " Hot Topic "," $" ),(" Dolls Kill " ,"$ " )],
        "Trendy" :[( "H&M "," $" ),("Urban Outfitters " ,"$$ " )], 
        "Indescribable" :[( "H&M "," $" ),("Urban Outfitters " ,"$$ " ), 
        ( " Hot Topic "," $" ),(" Dolls Kill " ,"$ " ), ("Ralph Lauren" ,"$$$" ),("White House Black Label" ,"$$$" ),                   
        ("Zara", "$" ),("Express" ,"$$" ) ],  
    }
    
    
    valid_style_choices = set(stores_for_styles.keys())
    style_preference = input("What's your style preference? (Preppy, Sophisticated, Comfy, Vintage, Y2K, Trendy,Indescribable):").title()
    
    if style_preference not in valid_style_choices:
        print("Uh Uh Uh! Please choose from Preppy, Sophisticated, Comfy, Vintage, Y2K, Trendy, Indescribable ")
        return
        
    stores = stores_for_styles[style_preference]
    store_suggestions= [f"{store_name} {cost_indicator}" for store_name, cost_indicator in stores]
    
    store_suggestions.sort(key=lambda s: s.count('$'))
    
    print(f"Here is your personalized store selection based on your {style_preference} style: ")
    for suggestion in store_suggestions: 
        print (suggestion)
    
    print ("Thank you so much for using BRAH FIX YOUR FIT! Have a nice day and see you next time! ")
    
clothing_store_suggestions ()







def checkAddToFile():
    """This function asks the user if they would like to save their outfit to 
    outfit logs (which is a different file), if the user enters "yes", then the
    string containing date and outfit make up will be appended to the different
    file. If the user enters "no" or anything else, the date and outfit make up are not saved to
    a different file.
    """
    check = input("Would you like to save this outfit to outfit logs? Enter yes if so, enter no or anything else if not ")
    if check == 'yes':
        print("Ok, saving outfit to file.")
        file1 = open("Saved.txt", "a")
        #appends new items to a file
        file1.writelines(globstr + "\n")
        #writes new lines to the file which contains the glob str which contains the date, outfits, accesories and adds a new line
    else:
        print("Ok, not saving outfit to file.")
  

def readFromFile():
    """This function asks the user if they would like to see an outfit from a 
    past date, if the user enters "yes" the user then has to enter the date
    they want to choose an outfit from. The function then reads the file where
    the outfits are stored and uses sequence unpacking to breakdown the
    information. The user is then asked which out of the three outfits saved
    they would like to see, and that outfit and its accessories are returned.
    If the answers anything other than yes, the program essentially ends.
    If the user enters a date where no outfit is saved, program also ends
    """
    want2Read = input("Would you like to see an outfit from a past date? Enter yes if so, enter no or anything else if not: ")
    if want2Read != 'yes':
        #program ends
        print('ok thanks for using our program ;(')
        return
    date2Read = input("What date would you like to read from: ")
    #reads each line from file
    with open('Saved.txt', 'r') as file:
    # Iterates over each line in the file
        for line in file:
            # Processes each line here
            squp = tuple(map(str, line.split(', ')))
            date, o1, o2, o3, accessories = squp # sequence unpacking
            if(date == "(" + date2Read):
                #asks what outift they want to see
                outfitNum = input("which outfit would you like to see? (Enter a number 1-3): ")
                if outfitNum == '1':
                    print(o1)
                    print(accessories)
                    return
                elif outfitNum == '2':
                    print(o2)
                    print(accessories)
                    return
                elif outfitNum == '3':
                    print(o3)
                    print(accessories)
                    return

                print("invalid input")
                return
        print("No such date found in the file.")


checkAddToFile()
readFromFile()


