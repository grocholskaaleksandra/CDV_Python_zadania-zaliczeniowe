# 23. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie dominanta (moda). Skorzystaj z obiektu Counter i jego metody most_common z pakietu collections

import collections

def main():
    decyzja = 't'
    while decyzja == 't':
        
        ilosc_liczb = int(input("Ile liczb chcesz wprowadzic?: "))
        lista = []
        
        for i in range (1, ilosc_liczb+1):
            liczby = float(input("Wprowadz liczbe: "))
            lista.append(liczby)
            
        dominanta = collections.Counter(lista).most_common(1)
        print ("Dominanta w zbiorze jest: {}". format(dominanta[0]))
        
        decyzja = input("Czy wykonac ponownie? t/n? ")
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print ("Koniec dzialania programu")

if __name__=="__main__":
    main()