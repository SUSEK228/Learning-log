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
        self.bok=promien
    
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
        

        
