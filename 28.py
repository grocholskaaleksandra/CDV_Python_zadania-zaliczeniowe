# 28. Utwórz funkcję, która jako argument będzie przyjmować dwie listy o równej liczbie elementów,
# a jej wynikiem będzie współczynnik korelacji

def korelacja (lista_pierwsza, lista_druga, ilosc_elementow):
    obliczenia_licznik_xy = []
    licznik_x = sum(lista_pierwsza)
    licznik_y = sum(lista_druga)
    x2_mianownik = []
    x_mianownik = ((sum(lista_pierwsza))**2)
    y2_mianownik = []
    y_mianownik = ((sum(lista_druga))**2)
    
    for i in range (ilosc_elementow):
        xy = lista_pierwsza[i]*lista_druga[i]
        x2 = (lista_pierwsza[i]**2)
        y2 = (lista_druga[i]**2)
        obliczenia_licznik_xy.append(xy)
        x2_mianownik.append(x2)
        y2_mianownik.append(y2)
        
    licznik = (ilosc_elementow*(sum(obliczenia_licznik_xy)))-(licznik_x*licznik_y)
    mianownik = ((ilosc_elementow*(sum(x2_mianownik)))-(x_mianownik))*((ilosc_elementow*(sum(y2_mianownik)))-(y_mianownik))
    wynik = licznik/(mianownik**0.5)
    return (wynik)

def main():
    decyzja = 't'
    
    while decyzja == 't':
        
        ilosc_elementow = int(input("Jaka liczbe elementow chcesz wprowadzic?: "))
        
        lista_pierwsza = []
        lista_druga = []
        
        for i in range (1,ilosc_elementow+1):
            liczby_pierwsza = float(input("Wprowadz liczby dla listy pierwszej: "))
            lista_pierwsza.append(liczby_pierwsza)
            
        for i in range (1,ilosc_elementow+1):
            liczby_druga = float(input("Wprowadz liczby dla listy drugiej: "))
            lista_druga.append(liczby_druga)
            
        print("Wspolczynnik korelacji wynosi: ", (korelacja(lista_pierwsza, lista_druga, ilosc_elementow)))
        
        decyzja = input("Czy wykonac ponownie? t/n? ")
        
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print("Koniec dzialania programu")



if __name__=="__main__":
    main()