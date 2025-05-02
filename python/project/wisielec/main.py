import sys
word = 'slowo'
length=len(word)

wisielec = 0 
zgadniete_literki = 0

odgatniete = ['_'] * length
odgatniete_litery = []
decyzja = input("Czy chccesz zagrac w grę? Nacisnij 1 by zagrac: ")

if decyzja == '1':
    while '_' in odgatniete:
        print(' '.join(odgatniete))
        print(f'liczba bledow:{wisielec}, max 6')
        user_word = input("Podaj literke: ")
        
        if user_word in odgatniete_litery:
            print("juz podales te literke!")
            continue
        
        if user_word in word:
            print("wystepuje ta literka")
            for i in range(length):
                if word[i] == user_word:
                    odgatniete[i]=user_word    
        else:
            print("nie wystepuje")
            wisielec += 1
            
        if wisielec >= 7:
            print("Przegrales")
            sys.exit()
        odgatniete_litery.append(user_word)
    print("Wygrales gre")
sys.exit()