# 19. Korzystając ze słownika, utwórz funkcję, która będzie zwracać liczbę dni danego miesiąca w roku

def dzien (rok, miesiac, przestepny, rok_slownik):
    if przestepny == 'n':
        print("W roku {} miesiac {} ma {} dni".format(rok, miesiac, rok_slownik[miesiac]))
    else:
        if miesiac == "Luty" or miesiac == "luty":
            print("W roku {} miesiac {} ma {} dni".format(rok, miesiac, rok_slownik[miesiac]+1))
        else:
            print("W roku {} miesiac {} ma {} dni".format(rok, miesiac, rok_slownik[miesiac]))
    return

def main():
    rok_slownik = dict([
            ('Styczen', 31),
            ('Luty', 28),
            ('Marzec', 31),
            ('Kwiecien', 30),
            ('Maj', 31),
            ('Czerwiec', 30),
            ('Lipiec', 31),
            ('Sierpien', 31),
            ('Wrzesien', 30),
            ('Pazdziernik', 31),
            ('Listopad', 30),
            ('Grudzien', 31)
            ])

    decyzja = 't'
    while decyzja == 't':
        
        rok = int(input("Wprowadz rok: "))
        miesiac = input("Wprowadz miesiac: ")
        
        if rok%400 == 0 and rok%100 == 0:
            przestepny = 't'
        elif rok%100 == 0 and rok%4 == 0:
            przestepny = 'n'
        elif rok%4 == 0:
            przestepny = 't'
        else:
            przestepny = 'n'
        
        
        dzien(rok, miesiac, przestepny, rok_slownik)

        decyzja = input("Czy wykonac ponownie? t/n? ")
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print("Koniec dzialania programu")

if __name__=="__main__":
    main()