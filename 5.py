# 5. Utwórz skrypt, który będzie komunikować, czy wprowadzona liczba jest dodatnia czy nie

def main():
    decyzja = 't'
    while decyzja == 't':

        try:
            liczba = float(input("Wprowadz liczbe: "))

            if liczba > 0:
                print ("Liczba jest dodatnia")
            elif liczba < 0:
                print ("Liczba jest ujemna")
            else: 
                print ("Liczba jest zerem")

        except ValueError:
            print("Podaj liczbe a nie slowo!")

        decyzja = input("Czy wykonac ponownie (t/n)?: ")

        while decyzja != "t" and decyzja != "n":
            decyzja = input("Czy wykonac ponownie (t/n)? ")

    print ("Koniec dzialania programu")

if __name__== "__main__":
   main()