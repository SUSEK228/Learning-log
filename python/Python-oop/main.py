#Ćwiczenie programowania obiektowego w pythonie

#from klasy import Car
#from klasy import Dog
#from klasy import Cat
#from klasy import Ryba
#from klasy import Vehicle
#from klasy import Motorbike

from klasy import Figura,Kolo,Kwadrat,Trojkat
'''
car1 = Car("A6", 2020, "black", False)
car2 = Car("Mustang", 1995, "red", True)    # przypisywanie
#car1.drive()
#car1.drive()
#car1.drive()
#car2.stop()
#print(Car.wheels)
#print(Car.przebieg)
#car1.opis()

'''
'''
dog = Dog("Pies")
kotek = Cat("Kicia")
print(dog.name)
dog.eat()
kotek.sleep()
dog.sound()
kotek.sound()
'''
'''
rybka = Ryba("Okon")
rybka.hunt()
rybka.eat()
'''
#vehicle = Motorbike()
#vehicle.stop()

figury = [Kolo(3),Kwadrat(4),Trojkat(2,3)]
for i in figury:
    print(f"{i.pole()} cm^2")