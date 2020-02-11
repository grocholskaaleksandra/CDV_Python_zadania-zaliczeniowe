# 7. Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika zdanie i wyświetli w kolejnych wierszach litery tego 
# zdania w odwróconej kolejności

def main():
    decyzja = 't'
    while decyzja == 't':

        zdanie = input("Wprowadz zdanie: ")
        
        for i in zdanie [::-1]:
            print(i)
            
        decyzja = input("\nCzy wykonac ponownie? t/n? ")

        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie? t/n? ")


    print ("Koniec dzialania programu")

if __name__=="__main__":
    main()