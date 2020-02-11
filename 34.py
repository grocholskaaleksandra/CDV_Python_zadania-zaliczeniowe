# 34. Utwórz klasę Kwadrat z konstruktorem ustalającym jego bok oraz metodami: wyświetlającymi wartość tego boku, obliczającymi pole i obwód figury

class Kwadrat :
    
    def __init__(self, bok):
        self.bok = bok
        print ("Bok kwardatu wynosi: {}".format(self.bok))
        
        
    def pole(self):
        pole = self.bok**2
        print ("Pole kwadratu wynosi: {}".format(pole))
        
    def obwod (self):
        obwod = 4*self.bok
        print ("Obwod kwadratu wynosi: {}".format(obwod))
    
def main():
    print("Podaj dlugosc boku do obliczenia pola i obwodu kwadratu!")
    
    wartosc = input("Dlugosc boku: ")
    
    try:
        wartosc = float(wartosc)
        bok = Kwadrat(wartosc)
        bok.pole()
        bok.obwod() 
    
    except ValueError:
        print("Podaj liczbe a nie slowo!")
      
if __name__== "__main__":
   main()