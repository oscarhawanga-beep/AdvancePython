class Farmer:
    def __init__(self,name,liters):
        self.name = name
        self.liters = liters


farmer1 = Farmer("John",50)
farmer2 = Farmer("Mary",50)
farmer3 = Farmer("Joseph",50)

print("Famer 1: ",farmer1.name," Liters: ",farmer1.liters)
print("Famer 2: ",farmer2.name," Liters: ",farmer2.liters)
print("Famer 3: ",farmer3.name," Liters: ",farmer3.liters)