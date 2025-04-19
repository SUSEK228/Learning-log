#Ćwiczenia od podstaw do pętli

# komentarz
'''
komentarz blokowy
'''

# zmienne
a = 1 # zmienna bez zdefiniowania typu typu 
b=2.5   # float 
c= "alala" # string
czy=True # bool

# wyswietlanie
print(a) 
print(f"liczba to: {a}") # wyswietlanie z wtrąceniem 

# instrukcje warunkowe 

if a > 5:
    print("wieksza")
elif a < 5:
    print( "mniejsza")
else:
    print("rowna")
    
    
if czy:
    print("true")
    
# Typecasting / zmiana typu

x = 3.5
print(type(x)) # wyswietlanie typu

x=int(x)
print(type(x)) # zamiana typu



# pętle 

for i in range (5):
    print (i)
    i+=1
    
    
for i in range (1,10,2): # od, do, krok
        print(i)
    
lista = ["ksiazka", "oko", "lizak"] # jazda  po liscie
for x in lista:
  print(x)

for x in "Pablo": # jazda po stringu
        print(x)
        
for x in range(6): # uzycie continue i break
    if x == 3:
        continue
    elif x==5:
        break
    print(x)
    
    
# while

i=0
while True:
    i+=1
    print(i)
    if i==2:
        break
    
s=3
zgad=0
while True:
    zgad = int(input("zgadnij liczbe od 0 do 10:\n "))
    if zgad ==s:
        print("udalo sie")
        break
    
    






