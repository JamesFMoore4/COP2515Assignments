
class Gem:

    def __init__(self, name, num_carats):
        self.__name = name
        self.__pricePerCarat = 0
        self.__setPrice()
        self.__num_carats = num_carats


    def __setPrice(self):
        low_name = self.__name.lower()
        if low_name == "tanzanite":
          self.__pricePerCarat = 1200.00
        elif low_name == "opal":
          self.__pricePerCarat = 9500.00
        elif low_name == "beryl":
          self.__pricePerCarat = 10000.00
        elif low_name == "musgravite":
          self.__pricePerCarat = 35000.00
        elif low_name == "alexandrite":
          self.__pricePerCarat = 7000.00
        elif low_name == "emerald":
          self.__pricePerCarat = 305000
        elif low_name =="ruby":
          self.__pricePerCarat = 1180000.00
        elif low_name == "diamond":
          self.__pricePerCarat = 1190000.00
        elif low_name == "jadeite":
          self.__pricePerCarat = 3000000.00
        else:
          self.__pricePerCarat = 0.00

    def getName(self):
        return self.__name

    def getNumCarats(self):
        return self.__num_carats

    def getPricePerCarat (self):
        return self.__pricePerCarat

    def calcCost(self):
        cost = self.__pricePerCarat * self.__num_carats
        return cost

  
  

class PreciousGems (Gem):

    def __init__(self, name, num_carats):
        Gem.__init__(self, name, num_carats)
        self.__color = ""
        self.__setColor()

    def __setColor(self):
        low_name = self.getName().lower()
        if low_name == "tanzanite":
            self.__color = "Royal Blue"
        elif low_name == "opal":
            self.__color = "Black"
        elif low_name == "beryl":
            self.__color = "Red"
        elif low_name == "musgravite":
            self.__color = "Grey"
        elif low_name == "alexandrite":
            self.__color = "Purple"
        elif low_name == "emerald":
            self.__color = "Green"
        elif low_name == "ruby":
            self.__color = "Red"
        elif low_name == "diamond":
            self.__color = "Pink"
        elif low_name == "jadeite":
            self.__color = "Dark Green"
        else:
            self.__color = "Not Precious Gem"

    def __str__(self):
        return "\n" + self.getName() + " (" + self.__color + \
        ") @ ${:,.2f}".format(self.getPricePerCarat()) \
        + " per carat: Cost of "+ "{:.2f}".format(self.getNumCarats()) \
        +" carats = "+ "${:,.2f}".format(self.calcCost())
    
  
  

          
