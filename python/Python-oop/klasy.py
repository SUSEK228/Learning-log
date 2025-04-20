#Ćwiczenie programowania obiektowego w pythonie
from car import Car
class Car:
    def __init__(self, model, year, color, for_sale): # za chwile wyjasnie
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
car1 = Car("A6", 2020, "black", False)
car2 = Car("Mustang", 1995, "red", True)    # przypisywanie
print(car1.model)   # wyswietlewnie 