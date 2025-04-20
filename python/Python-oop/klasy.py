#klasy
from abc import ABC , abstractmethod
class Car:
    
    wheels = 4
    ilosc = 0
    przebieg=0
    
    def __init__(self, model, year, color, for_sale): # konstrutor
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        Car.ilosc +=1
        
    def drive(self):
        print(f"Prowadzisz {self.color} {self.model}")
        Car.przebieg +=10
        
    def stop(self):
        print(f"zatrzymales {self.color} {self.model}")
        
    def opis(self):
        print(f"Samochod to: {self.model}\nrok: {self.year}\nkolor: {self.color}\nDostepny: {self.for_sale}")

class Animal:
    alive=True
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
       print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def sound(self):
        print("Hau")


class Cat(Animal):
    def sound(self):
        print("Miau")  
      


class  Predator(Animal):
    def hunt(self):
        print("This animal is Predator")

class Prey(Animal):
    def flee (self):
        print("This animal is fleeing")
        
class Ryba(Prey, Predator):
    pass

class Telefon:
    alive=False
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Ring ring")

# klasa abstrakcyjna
class Vehicle(ABC):
    
    #@abstractmethod
    def go(self):
        pass
    
    #@abstractmethod
    def stop(self):
        pass
    
class Motorbike(Vehicle):
    def go(self):
        print("You drive a MotorBike")
    def stop(self):
        print("You stopped a Motorbike")

class Bus(Vehicle):
    def go(self):
        print("You drive a Bus")
    def stop(self):
        print("You stopped a Bus")


class Osoba:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko

class Student:
    def __init__(self,imie,nazwisko,uczelnia):
        super().__init__(imie,nazwisko)
        self.uczelnia=uczelnia
        
        
class Figura:
    @abstractmethod
    def pole(self):
        pass
    
    
class Kolo(Figura):
    def __init__(self,promien):
        self.promien=promien
    
    def pole(self):
        return 3.14*self.promien**2


class Kwadrat(Figura):
    def __init__(self,bok):
        self.bok=bok
    def pole(self):
        return self.bok ** 2
        
class Trojkat(Figura):
    def __init__(self,podstawa,wysokosc):
        self.podstawa=podstawa
        self.wysokosc=wysokosc
    def pole(self):
        return self.podstawa*self.wysokosc/2
        
class Paczka(Kwadrat):
    def __init__(self, bok, material):
        super().__init__(bok)
        self.material=material

        
class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower

class Wheel:
    def __init__(self,size):
        self.size=size
        
class Carobj:
    def __init__(self,model,horsepower,wheelsize):
        self.model=model
        self.engine=Engine(horsepower)
        self.wheels= [Wheel(wheelsize) for wheel in range(4)]
    
    def info(self):
        return f"{self.model} {self.engine.horsepower}(KM) {self.wheels[0].size}"

class Firma:
    class Pracownik:
        def __init__(self,imie,stanowisko):
            self.imie=imie
            self.stanowisko=stanowisko
        
        def get_details(self):
            return f"{self.imie} {self.stanowisko}"
    
    def __init__(self,nazwa_firmy):
        self.nazwa_firmy=nazwa_firmy
        self.pracownicy = []
        
    def dodaj_pracownika(self, imie, stanowisko):
         nowy_pracownik = self.Pracownik(imie,stanowisko)
         self.pracownicy.append(nowy_pracownik)

    def lista_pracownikow(self):
        return [i.get_details() for i in self.pracownicy]
#statyczne metody naleza do klasy ogolnie nie uzywaja danych z klasy, sa niezalezne

'''
Magic methods:
-    __str__        zwracamy stringi z danych elementow klasy
-    __eq__         porownuje obiekty
-    __lt__         znak <  w stosunku do obiektow
-    __gt__         znak > w stosunku do obiektow
-    __add__        mozna dododawac dane z obiektow
-    __contains__   sprawdzanie czy obiekt zawiera dany element (True/False)
-    __getitem__    zwracanie wybranego klucza
-    __del__        destruktor obiektu

Property Decorators:
@property - pozwala traktowac metode jako atrybut (m nie trzeba uzywac nawiasow)
@cos.setter - pozwala na modyfikacje pola
@deleter - taki destruktor w c++ tylko ze usuwasz jakies kopnkretne dane a nie caly obiekt


Poziomy Dostępu:
np.
self.test       - public
self._test      - protected
self.__test     - private

'''