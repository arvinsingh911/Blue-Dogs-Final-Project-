import pandas as pd
from pathlib import Path
import re

#function takes in data & tells user the weather
df_filepath = Path(__file__).parent / "WeatherDataSet.csv"




def date_weather(filepath):
    """
    
    args: filepath to the 
    """
    #add doc string for the fucntion 
    user_input = input("Input a date from April 2024 as M/D/YYYY, ie. 4/1/2024")
    try:
        date_pattern = r"(?P<month>\d{1})(?P<slash1>\/)(?P<day>\d{1,2})(?P<slash2>\/)(?P<year>\d{4})"
        match = re.search(date_pattern,user_input)
           
    except:
        raise ValueError("Format is incorrect. Ensure you are using the M/D/YYYY")

     # check to make sure that date is in the range, use logicical epxresions if, else etc.
    month = int(match.group("day"))
    day = int(match.group("day"))
    year =int(match.group("year"))

    if month != 4 | day < 1 |day > 30 | year != 2024:
        raise ValueError ("Ensure that the date entred as a date in April 2024")
    

    df = pd.read_csv(filepath) #loads the dataframe
    #date_column = df.loc[:"Date"] #acesses the data in the date column
    
    df_date = df.loc[df["Date"]==user_input] #filers just the row of data where the user_input = date
    if len(df_date) > 0:
        weather = df_date.at[0,"Weather"]
        return weather
        #select the vlaue at 1st row & the 2nd colunm 
        #save that vlaue to weather variable
    else:
         print("Check the format of your date.")

    
    



 