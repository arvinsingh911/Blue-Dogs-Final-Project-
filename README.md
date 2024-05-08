**How to run the program**
* In the terminal type python if using Windows or python3 if using Mac and then a space then type Final Project.py in quotes
* Size: Theres a question that prompts the user about their weight and body type, and based on certain categories itrecommend's sizing of shirts, pants, and shoes based upon the body weight and body type of the user
* Height: Theres a question that prompts the user about their height, and based on this itrecommend's and make's suggestions on what type of sizing in styles would look better on your person based upon your height. This is just a suggestion of sizes, accessories and what length the item of clothing should be such as large and tall, moderate size and petite. This is because differnt heights have different lenght requirments for sizing and fitting 
* Date input: There will be a question that asks the user what date they would like to know the weather. The user should enter a date in the month of April 2024
* Accessories: There will be a question that asks if user wants to add accessories to their outfit or not. If the user does want to add accessories they enter a number 1-5 (correlating to the number of accessories they want to add). If not, the user can enter 0 or hit enter and no accessories will be added to their outfit.
* Style Preference:
* Save outfit: There will be a question that asks the user if they would like to save their suggested outfits. The user can type yes to save the outfit, or the user can type no or anything else if they would not like the outfit saved
* Past outfit: There will then be a question that asks the user if they would like to see past saved outfits. The user can type yes, which will then prompt the user to enter a date of an outfit list that has already been saved (ie. saved outfits already in the Saved file). if the outfit is saved, then the user will be prompted to type an outfit number which results in an outfit correlating to the number and date to be shown to the user. Otherwise, the user can input no or anything else which ends the program.



**An explanation of the purpose of each file in the repository**
* WeatherDataSet.csv file
  -This file is a CSV file that is used to create a data frame for the weather in April. This CSV file will be used to get the
  corresponding weather for the date that is inputted for the date_weather function
  -This file also is needed for the weather_filter function. This function creates a new data frame that groups the weather
  types counts the occurrences of each weather type, based on the CSV file. Then the function plots the weather types vs the number of occurrences as a bar plot.
* Saved.txt file
  -This file is used by the checkAddToFile and readFromFile functions to help save and return outfits the user has created.
  

**How to use the program/interpret the output of the program**


Date input
* The program will allow the user to input the date and will return the weather for the corresponding date. This will allow the user to
  know the weather for the inputted date.

Bar Plot of weather occurrences
* The bar plot will allow the user to see how many days it is rainy, windy, warm, cool, cold, and hot for the month of April 2024.

Accessories input
* The program will allow the user to enter the number of accessories they want added to their outfit (1-5) if they want accessories added to their outfit. If the user enters 0 or hits enter the user can choose to add not accessories to their outfit. What option they went with is returned in the terminal for them to see (for example if they chose to add 2 accessories two random accessories added can be seen in the terminal.

Saveoutfit input
* The program will allow the user to type yes to save outfit, or the user can type no or anything else to not save the outfit. What option they went with is returned in the terminal for them to see (for example if they typed no, then the terminal out put would be "Ok, not saving to file).


**Attribution**

 Function/Method Name | Author | Techniques Demonstrated/Purpose |
|----------|----------|----------|
|Row 1, Col 1 | Arvin Singh| - f-strings containing expressions |
| Row 2, Col 1 | Arvin Singh | - conditional expressions |
| date_weather | Marylyn Uzoukwu | -Regular expressions and filtering operations on a pandas data frame|
| weather_filter | Marylyn Uzoukwu |-Data visualization and group by operations on a pandas data frame |
| addAccessory | Alexander Janco | -Optional parameters|
| readFromFile | Alexander Janco | -Sequence unpacking |
| Row 1, Col 1 | Asa Agyemang | Row 1, Col 3 |
| Row 2, Col 1 | Asa Agyemang | Row 2, Col 3 |















