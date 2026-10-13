class Car:
    pass

# Below we create three cars from our class of car
car1 = Car()
car2 = Car()
car3 = Car()
print(car1,car2,car3)

# Below we give our dufferent objects some attributes.

car1.brand ="Toyota"
car1.model = "camry"

print("Car1:",car1.brand,car1.model)

car2.brand = "Honda"
car2.model = "Civic"
print("Car2:",car2.brand,car2.model)

car3.brand = "Volkswagen"
car3.model = "Golf"
car3.year = 2025
car3.colour = "Red colour"
car3.owner =" Car Owner : Oscar Hawanga"
print("Car3:",car3.brand,car3.model,car3.year,car3.colour,car3.owner)