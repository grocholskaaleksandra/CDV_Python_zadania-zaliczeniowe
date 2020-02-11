# 26. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie trzeci moment centralny (skośność)

import numpy 

def skosnosc (liczby, ilosc_liczb):
    srednia = sum(liczby)/ilosc_liczb
    odchylenie = numpy.std(liczby)
    obliczenia =[]
    
    for i in range(ilosc_liczb):
        obliczenia_elementow = ((liczby[i]-srednia)**3)
        obliczenia.append(obliczenia_elementow)
        
    skosnosc = sum(obliczenia)/(ilosc_liczb*(odchylenie**3))
    return (skosnosc)

def main():
    decyzja = 't'
    
    while decyzja == 't':
        
        ilosc_liczb = int(input("Ile liczb chcesz wprowadzic?: "))
        
        liczby = []
        for i in range (1,ilosc_liczb+1):
            liczby1 = float(input("Wprowadz liczby: "))
            liczby.append(liczby1)
        
        print("Skosnosc wynosi",(skosnosc(liczby, ilosc_liczb)))
        
        decyzja = input("Czy wykonac ponownie? t/n? ")
        
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print("Koniec dzialania programu")

if __name__=="__main__":
    main()
