# 16. Utwórz funkcję własną, która jako argument przyjmować będzie listę argumentów i wartości, 
# a jako wynik będzie wyświetlać sformatowany wykres (stosowny zakres, opis, kolory, legenda)


import pylab as pylab

def wykres (argumenty, ilosc_argumentow, ilosc_wartosci):
    
    for i in range (1, ilosc_argumentow+1): 
        wartosci = []
        print("Uwaga zaczynasz wprowadzac wartosci dla argumentu {}!".format(argumenty[i-1]))
        
        for j in range(1, ilosc_wartosci+1):
            liczby = float(input("Wprowadz wartosc: "))
            wartosci.append(liczby)
            
        print("W jakim kolorze chcesz przedstawic argument {} na wykreie?".format(argumenty[i-1]))
        kolor = input("Wybierz: r/g/b/c/m/y/k/w: ")
        (pylab.plot(wartosci, color=(kolor)))
        
        
    (pylab.legend(argumenty))
    pylab.title("Wykres uzytkowika: ")
    pylab.xlabel('Os X')
    pylab.ylabel('Os Y')


def main():
    decyzja = 't'
    while decyzja == 't':
        
        try:
            ilosc_argumentow = int(input("Ile argumentow chcesz wprowadzic?: "))
            ilosc_wartosci = int(input("Ile wartosci chcesz wprowadzic?: "))

        except ValueError:
            print("Podaj liczbe a nie slowo!")

        argumenty= []
        
        for i in range (1, ilosc_argumentow+1):
            cyfry = input("Wprowadz argument: ")
            argumenty.append(cyfry)
            
        wykres(argumenty, ilosc_argumentow, ilosc_wartosci)
        
        decyzja = input("Czy wykonac ponownie? t/n? ")
        
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print ("Koniec dzialania programu")

if __name__=="__main__":
    main()