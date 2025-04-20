#Ćwiczenie programowania obiektowego w pythonie

#from klasy import Car
from klasy import Animal,Cat,Ryba,Dog,Telefon
#from klasy import Vehicle
#from klasy import Motorbike

from klasy import Figura,Kolo,Kwadrat,Trojkat,Paczka,Engine,Wheel,Carobj,Firma
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
'''
zwierzeta=[Dog("Max"),Cat("Kitek"),Telefon("Iphone")]
for i in zwierzeta:
    i.sound()
    print(i.alive)
'''
#composition
'''
car =Carobj(model="A6",horsepower=210,wheelsize=15)
car2=Carobj(model="e36",horsepower=190,wheelsize=14)
print(car.info())
'''

#nested classes
firma1 = Firma("BINBASH")
firma1.dodaj_pracownika(imie="Pablo",stanowisko="Spawacz")
firma1.dodaj_pracownika(imie="Wiktor",stanowisko="Manager")
firma1.dodaj_pracownika(imie="Marek",stanowisko="Kasjer")

firma2 = Firma("CMD")
firma2.dodaj_pracownika(imie="Asia",stanowisko="Manager")
firma2.dodaj_pracownika(imie="Kasia",stanowisko="Sekretarka")
firma2.dodaj_pracownika(imie="Malgosia",stanowisko="Robotnik")
for i in firma1.lista_pracownikow():
    print(i)
for i in firma2.lista_pracownikow():
    print(i)