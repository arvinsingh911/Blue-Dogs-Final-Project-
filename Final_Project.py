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
    parser = argparse.ArgumentParser(description="Smart outfit planner")
    
    # The command line arguments 
    # User will enter name, age(int), weather, occasion
    parser.add_argument("name",type = str, help = "The name of the user")
    parser.add_argument("age",type = int, help = "The age of the user")
    parser.add_argument("weather",type = str, help = "The current weather \
        conditions")
    parser.add_argument("occasion",type = str, help = "Occasion for the outfit")
    
    if not args.name:
        raise ValueError('Name is required.')
    
    if args.age is not None and args.age <= 0:
        raise ValueError('Age must be a positive integer.')
    
    return {
        'name': args.name,
        'age': args.age,
        'weather': args.weather,
        'occasion': args.occasion
    }
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])


class Outfit():
    
    #needs to add sections of clothing in here
    
    
    def __init__(self):
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
