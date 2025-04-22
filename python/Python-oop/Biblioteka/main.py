from klasy import Ksiazka,Biblioteka,Uzytkownik

ks1 = Ksiazka("Sztuka wojny", "Sun Tzu", 200, False)
ks2 = Ksiazka("Wiedzmin", "Sapkowski",  1995, False)
ks3 = Ksiazka("Atomowe Nawyki", "Tomek", 2020, False)

Biblio = Biblioteka()

Biblio.dodaj_ksiazke(ks1)
Biblio.dodaj_ksiazke(ks2)
Biblio.dodaj_ksiazke(ks3)
Biblio.wyswietl_biblioteke()

user1 = Uzytkownik("Pablo", "Kulesza")
user2 = Uzytkownik("Konrad", " Mat")
Biblio.wypozycz_ksiazke(ks2,user1)
Biblio.zwroc_ksiazke(ks2,user2)
Biblio.wypozycz_ksiazke(ks2,user2)

