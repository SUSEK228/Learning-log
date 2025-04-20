#Ćwiczenie programowania obiektowego w pythonie

#from klasy import Car
from klasy import Animal,Cat,Ryba,Dog
#from klasy import Vehicle
#from klasy import Motorbike

from klasy import Figura,Kolo,Kwadrat,Trojkat,Paczka
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

#polimorfizm
'''
figury = [Kolo(3),Kwadrat(4),Trojkat(2,3),Paczka(2,"karton")]
for i in figury:
    print(f"{i.pole()} cm^2")
    '''
    
#Duck typing

zwierzeta=[Dog("Max"),Cat("Kitek")]
for i in zwierzeta:
    print(f"{i.sound()}")