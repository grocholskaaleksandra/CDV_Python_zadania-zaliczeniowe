#14. Utworzyć skrypt z interfejsem tekstowym, który będzie zwracać wiersz n-tego rzędu z trójkąta Pascala 
#(użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta)

def silnia(cyfra):
    if cyfra == 1 or cyfra == 0:
        return 1
    wynik = cyfra * silnia(cyfra-1)
    return wynik 

def Newton (pierwsza,druga):
    if druga == 0 or druga == pierwsza:
        return 1
    elif druga >= pierwsza:
        return print("k musi byc mniejsze od n")
    wynik = silnia(pierwsza)/(silnia(druga)*silnia(pierwsza-druga))
    return wynik

def trojkat (wiersz):
    lista = []
    for i in range (wiersz+1):
        for j in range (i+1):
            newton = int(Newton(i,j))
            lista.append(newton)
        print(lista)
        lista.clear()
        
def main():

    decyzja = 't'
    while decyzja == 't':

        n = input("Wprowadz n-ty rzad trojkatu Pascala: " )
        
        try:
           n = int(n)
           trojkat(n)
    
        except ValueError:
          try:
            n = float(n)
            trojkat(n)
    
          except ValueError:
              print("Podaj liczbe a nie slowo!")
            
        decyzja = input("Czy wykonac ponownie? t/n?: ")
    
        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")

    print ("Koniec dzialania programu")

if __name__== "__main__":
    main()