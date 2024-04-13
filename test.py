class Outfit():
    """outfit class
    """
    #outfit class to be full developed later with clothing items/outfits
    #needs to add sections of clothing in here
    
    
    def __init__(self):
        """this function initializes the accessories list
        """
        self.accessories = [] #list creation
    
    #custom arugment #new optional parameters
    #this function takes in an outfit and adds 
    def addAcessory(self, accessory="jewlery"):
        """Adds accessory "jewlery" to accessory list in this instance of the 
        class. If the calling function has a second parameter that parameter
        is added to the accessory list instead of "jewlery" as the default
        

        Args:
            accessory (str, optional): A string to be added to the list of 
            accessories in this instance of the class. Defaults to "jewlery".
        """
        #loop through the arguments
        self.accessories.append(accessory) #append each acessory
        #extend
    
    
    #Sort the accessories by the length of the jewlery n
    #def sortAccessories(self):
        #return sorted(self.accessories, key=len)
            
  
#testing  
myoutfit = Outfit()
myoutfit.addAcessory()
myoutfit.addAcessory("Sunglasses")
print(myoutfit.accessories)

