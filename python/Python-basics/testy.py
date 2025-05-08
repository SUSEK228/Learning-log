'''
#lista
imiona = ["pawel", "maciek", "konrad"]
#dodaj
imiona.append("kolos")
imiona.insert(1,"chudy")
#usun
imiona.remove("maciek")
imiona.pop()
#wyswietl
print(imiona[0])
for imie in imiona:
    print(imie)
    
    
#słowniki
osoba = {"imie" : "Ania","wiek" : "20"}
#dodawanie i akutalizacja
osoba["miasto"] = "Warszawa"
osoba["wiek"] = "21"
#usuwanie
del osoba["miasto"]
# wyswietlanie
print(osoba["imie"])
for klucz, wartosc in osoba.items():
    print(klucz,wartosc)
    
#zbiory
kolory = {"czerwony","zielony","niebieski"}
kolory.add("żólty")
kolory.remove("czerwony")
for i in kolory:
    print(i)
    
#krotki
points = (10,20)
x,y=points
for i in points:
    print(i)
    
    
try:
    x=int(input("podaj liczbe: "))
    print(x)
except: # jak jest blad
    print("Blad")
else: # jak nie ma bledu
    print("Nie ma bledu")
finally: # niezaleznie od tego czy jest blad
    print("wykonano")
'''    
    

#działanie na plikach

#czytanie z pliku
'''
file = open("C:/Users/Pkule/Desktop/Github/Learing log/Learing-log/python/Python-basics/przyklad.txt", "r")
print(file.readable()) # sprawdza czy mozna odczytac
print(file.readline()) # odczytuje linie po kolej
print(file.readlines()) # a to w formie listy
print(file.readlines()[2]) # wybrane wiersze
for lines in file.readlines(): # czytanie lini po kolej w for
    print(lines)
file.close()'''

#zapisywanie do pliku
'''
file = open("C:/Users/Pkule/Desktop/Github/Learing log/Learing-log/python/Python-basics/tekst.txt", "w")
file.write('elo')
file.close()
'''

# dodawanie do pliku ( bez nadpisywania)
file = open("C:/Users/Pkule/Desktop/Github/Learing log/Learing-log/python/Python-basics/tekst.txt", "a")
file.write('\nelo zelo')
file.close()