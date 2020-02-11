# 25. Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie drugi moment centralny (wariancja)

def wariancja (liczby, ilosc_liczb):
    srednia = sum(liczby)/ilosc_liczb
    obliczenia =[]
    
    for i in range(len(liczby)+1):
        if i < len(liczby):
            obliczenia_elementow = ((liczby[i-1]-srednia)**2)/ilosc_liczb
            obliczenia.append(obliczenia_elementow)
            
    return (sum(obliczenia))
    
def main():
    decyzja = 't'
    
    while decyzja == 't':
        
        ilosc_liczb = int(input("Ile liczb chcesz wprowadzic?: "))
        
        liczby = [] 
        for i in range (1,ilosc_liczb+1):
            liczby1 = float(input("Wprowadz liczby: "))
            liczby.append(liczby1)
        
        print("Wariancja wynosi",(wariancja(liczby, ilosc_liczb)))
        
        decyzja = input("Czy wykonac ponownie? t/n? ")
        
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print("Koniec dzialania programu")

if __name__=="__main__":
    main()