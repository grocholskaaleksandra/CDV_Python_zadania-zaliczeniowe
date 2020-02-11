# 31. Korzystając z instrukcji np.random.choice oraz reshape z pakietu numpy stworzyć funkcję generują macierz kwadratową stopnia N wypełnioną wartościami 0 i 255 w losowy sposób

import numpy

def main():
    decyzja = 't'
    while decyzja == 't':
        
        N_random = numpy.random.choice(range(1,100))
        
        print (numpy.random.choice([255, 1], N_random*N_random, p=[0.5, 0.5]).reshape(N_random, N_random))

        decyzja = input("Czy wykonac ponownie? t/n? ")

    print ("Koniec dzialania programu")

if __name__== "__main__":
   main()