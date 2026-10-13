
class Country:
    pass

Country1 = Country()
Country2 = Country()
Country3 = Country()

print(Country1,Country2,Country3)

Country1.name = "Namibia"
Country1.city = "Windhoek"
Country1.population = 3000000

Country2.name = "Lesotho"
Country2.city = "Unknown"
Country2.population = "Unkown"

Country3.name = "Botswana"
Country3.city = "Gaborone"
Country3.population = "Unkown"

print("Country Details: ",Country1.name," City: ",Country1.city,"population: ",Country1.population)
print("Country Details: ",Country2.name," City: ",Country2.city,"population: ",Country2.population)
print("Country Details: ",Country3.name," City: ",Country3.city,"population: ",Country3.population)
