class Biblioteka:
    def __init__(self):
        self.ksiazki = []
        self.uzytkownicy =[]
        
    def dodaj_ksiazke(self,book):
        self.ksiazki.append(book)
        
    def dodaj_uzytkownika(self,user):
        self.uzytkownicy.append(user)
    
    def usun_uzytkownika(self,user):
        self.uzytkownicy.remove(user)
        
    def usun_ksiazke(self,book):
        self.ksiazki.remove(book)
        
    def wypozycz_ksiazke(self,book,user):
        if book.wypozyczona == True:
            print("Książka jest już wypożyczona")
        else:
            print(f"{user.imie}{user.nazwisko} wypozycza ksiazke {book.tytul}")
            book.wypozycz(user)
            
    def zwroc_ksiazke(self,book,user):
        if book.wypozyczona == False:
            print("Książka jest dostepna ( Nie wypozyczona przez nikogo)")
        elif book.wypozyczona == True and book.wypozyczona_przez==user:
            print(f"{user.imie} {user.nazwisko} zwraca ksiazke {book.tytul}")
            book.zwroc()
        else:
            print("Ta ksiazka nie nalezy do ciebie")
            
    def wyswietl_biblioteke(self):
        if not self.ksiazki:
            print("Biblioteka nie posiada zadnych ksiazek")
        else:
            print("Ksiazki w bibliotece: ")
            for i in self.ksiazki:
                status = "Wypozyczona" if i.wypozyczona else "Dostepna"
                print(f"- {i.tytul} {i.autor, i.rok} - {status}")
    
class Ksiazka:
    def __init__(self,tytul,autor,rok,wypozyczona=False,):
        self.tytul=tytul
        self.autor=autor
        self.rok=rok
        self.wypozyczona=wypozyczona
        self.wypozyczona_przez=None
        
    def wypozycz(self,user):
        self.wypozyczona=True
        self.wypozyczona_przez=user
        
    def zwroc(self,user):
        self.wypozyczona=False
        self.wypozyczona_przez=None

class Uzytkownik:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko