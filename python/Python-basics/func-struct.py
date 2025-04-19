
def hello():
    print("witaj")
def dodaj(a,b):
    return a+b
def przywitaj(imie="Pawel"): # argumenty domyślne
    print(f"hello: {imie}!")    
def produkt(cena,nazwa): # rozne kolejnosci argumentow
        print(f"cena: {cena}, nazwa: {nazwa}")
def mnozenie(*liczba): # dowolna liczba argumentow
    wynik=1
    for i in liczba:
        wynik *= i
    print(wynik)
    
hello()

x=dodaj(5,3)
print(x)

przywitaj()
przywitaj("Kasia")

produkt(20,"jablko")
produkt(nazwa="jablko",cena=20)

mnozenie(1,2,3,4,5)

#struktury 
 
 #lista
owoce=["jablko","banan","gruuszka"]
owoce.append("czeresnia")   #dodaj na koniec
owoce.remove("banan")       #usun dany element
owoce[0]="ananas"           #zmien dany element
print(owoce[2])             #wyswietl dany element
print(len(owoce))           #jaka dlugosc listy


#slownik

produkt = {
    "nazwa":"jablko",
    "cena": 20,
    "kategoria":"jedzenie"
}

produkt["nazwa"]="gruszka"  #zmiana wartosci
produkt["stan"]="nowy"      #dodanie nowej pary
print(produkt["nazwa"])     # dostep do danych


#zbior 
#od razu w kolejnosci aflabaetycznej

owoce={"jablko","gruszka","banan"}
owoce.add("banan")
owoce.add("pomarancza")
owoce.remove("jablko")
print(owoce)

print("mandarynka" in owoce)    #sprawdz czy istnieje

# krotka / taka lista ale niemodyfilkowalna

wspolrzedne = (10,20,30,40)
print(wspolrzedne[1])