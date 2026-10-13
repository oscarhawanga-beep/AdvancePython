class Farmer:
    def __init__(self):
        self.name ="John"
        self.liters = 50

    def farmer_info(self):
        print("The name of farmer is: ", self.name)
        print("The number of liters the farmer provided: ",self.liters)

farmer1 = Farmer()
farmer1.farmer_info()