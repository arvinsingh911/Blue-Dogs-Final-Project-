import pandas as pd

#function takes in data & tells user the weather
df_filepath = "C:/Users/Maryl/Downloads/WeatherDataSet.csv"
#pd.read_csv(data_filepath)


def date_weather(filepath):
    user_input = input("Input the date as M/D/YYYY, ie 4/1/2024")
    try:
        pd.to_datetime(user_input, dayfirst = True, errors = 'raise')    
    except ValueError:
        print("Format is incorrect. Ensure you are using the M/D/YYYY")

    df = pd.read_csv(filepath) #loads the dataframe
    #date_column = df.loc[:"Date"] #acesses the data in the date column
    
    df_date = df.loc[df["Date"]==user_input] #filetrs just the row of data where the user_input = date
    if df_date.isin([user_input]):#get this checked
        weather = df_date.loc[0] #get this checked
        #add a conidtion, if ture extract the weather from the row, else send a message

        #df_date = df.loc[df["Date"]==user_input] #cretes a dataset of just the row
        #weather = df_date.at[0,0]

    else:
        print("Check the format of your date") #should this be a return or try/except?
    
    return weather
     



    weather_column = dataset_weather.loc[:"Weather"]

    


    #acess the colunm weateher, assocaited to the date
    #then return that weather


 