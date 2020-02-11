# 1. Utwórz program do nauki obcych słówek. Program powinien posiadać interfejs tektowy, w którym użytkownik wskazuje plik ze słówkami do nauki. 
#Następnie program importuje dane i wprowadza je do słownika. W kolejnym etapie program przepytuje uzytkownika z wiedzy zawartej w pliku ze słówkami. 
#Program powinien wyliczać za ile dni użytkownik powinien powtórzyć naukę - jeśli odpowiedział dobrze - za 7 dni, jeśli źle - za 0 dni. 
#Program tworzy nowy plik, który będzie zawierać informacje na temat daty ostatniej sesji nauki, id przerobionych słówek oraz za ile dni należy odbyć powtórkę.
#Program dodatkowo ma importować log z poprzedniej sesji aby odpytywać użytkownika z zaplanowanej powtórki.

import random
import csv
import pandas as pd
from datetime import datetime
from datetime import date
from os import path

def main():
    #Okreslenie formatu daty ma DD/MM/YYYY
    date_format = "%d/%m/%Y"
    #Zapisanie do zmiennej dzisiejszej daty - potrzebne w momencie obliczania roznicy pomiedzy dniem dzisiejszym a dniem ostatniej powtorki
    dzisiaj = date.today()
    #Data w formacie YYYY/MM/DD
    dzisiaj = dzisiaj.strftime(date_format)
    #Data w formacie DD/MM/YYYY
    dzisiaj = datetime.strptime(str(dzisiaj), date_format)
    odpowiedzi_lista = []
    #Ponizsze jest naglowkiem naszego pliku do powtorek. Pozniejsze wartosci rowniez beda dopisywane w taki sposob zeby zostac odczytane przez plik w formacie .csv (comma delimitted)
    odpowiedzi_lista.append("Angielski,Polski,Kiedy_Powtorzyc,Data_Wprowadzenia")
    odpowiedz_powtorka = ""
    
    #Spytanie uzytkownika czy chce zrobic sobie powtorke. Petla dopoki nie zostanie wpisany jeden z przedstawionych znakow
    while odpowiedz_powtorka != "y" and odpowiedz_powtorka != "n" and odpowiedz_powtorka != "z":
        print("\n--------------------------------------------------\nCzy chcesz zrobić powtórkę z poprzedniej lekcji?\nWcisnij 'z' zeby zakonczyc.")
        odpowiedz_powtorka = input("Twoja odpowiedz (y/n) (aby zakonczyc wpisz 'z'): ")    
        if odpowiedz_powtorka == "z":
            break
        elif odpowiedz_powtorka != "y" and odpowiedz_powtorka != "n":
            print("Zły znak!")
    
    #Sciezka jezeli zostanie wybrana chcec powtorzenia ostatnio zapisanych odpowiedzi
    if odpowiedz_powtorka == "y":
        
        print("Podaj sciezke do pliku z powtorka wraz z jego nazwa i rozszerzeniem.\nPrzyklad: C:\ Users\ odpowiedzi.csv")
        powtorka_sciezka = input("Sciezka: ")
        
        #Sprawdzenie czy plik z podanej sciezki istnieje. Jezeli nie to program zostanie zamkniety.
        if path.exists(powtorka_sciezka) == False:
            print("Brak tego pliku w podanej sciezce!\nZegnam!")
            exit()
        else:
            #Odczytanie pliku .csv z podanej sciezki
            powtorka_data = pd.read_csv(powtorka_sciezka)
        
            #Sprawdzenie czy cokolwiek jest w pliku. Jak nie ma nic to sie zegnamy
            if len(powtorka_data.index) == 0:
                print("\nBrak slowek do powtorzenia!\nZegnaj!")
            
            #Jezeli cos jest w pliku to robimy petle przez wszystkie dostepne wiersze
            for index, row in powtorka_data.head().iterrows():
            
                #Wyciagamy date wprowadzenia do pliku danego wiersza i ustalamy od razu jej format
                data_wprowadzenia = datetime.strptime(row['Data_Wprowadzenia'], date_format)
                roznica_dni = dzisiaj - data_wprowadzenia
                
                #Jezeli wartosc z kolumny Kiedy Powtorzyc rowna sie roznicy dni pomiedzy dzisiaj a data wprowadzenia to ten wiersz zostanie pokazany uzytkownikowi do powtorki
                if int(row['Kiedy_Powtorzyc']) == int(roznica_dni.days):
                    wyswietlanie = "{}"
                    print ("\n--------------------------------------------------\nSlowko: ",(wyswietlanie.format(row['Angielski'])))
                    odpowiedz = input("Twoja odpowiedz (aby zakonczyc wpisz 'z'): ")
                    
                    if odpowiedz == "z":
                        break
                    
                    #Przyrownaj odpowiedz uzytkownika do wartosci z kolumny Polski
                    if odpowiedz == (row['Polski']):
                        print ("Odpowiedz poprawna!")
                    else:
                        print ("Odpowiedz nieprawidlowa")
                        print("Poprawna odpowiedz to: ", (row['Polski'] + "\n"))
                        
                else:
                    print("Nie ma zaplanowanej powtorki na dzis!")
    
    #Sciezka jezeli uzytkownik nie wybral powtorki     
    elif odpowiedz_powtorka == "n":
        
        print("Podaj sciezke do pliku z cwiczeniem wraz z jego nazwa i rozszerzeniem.\nPrzyklad: C:\ Users\ Slowka.csv")
        cwieczenia_sciezka = input("Sciezka: ")
    
        #Sprawdzenie czy plik z podanej sciezki istnieje. Jezeli nie to program zostanie zamkniety.
        if path.exists(cwieczenia_sciezka) == False:
            print("Brak tego pliku w podanej sciezce!\nZegnam!")
            exit()
        else:
            #Otwarcie pliku .csv z danymi do cwiczen
            slowka = csv.reader(open(cwieczenia_sciezka))
            #Zapisanie zawartosci plku w dictonary dzieki czemu slowka po angielsku beda kluczem a po polsku beda ich wartosciami
            slowka_dict = dict(slowka)
            
            #Pomimo pomieszania - shuffle - tylko slowek po angielsku ich odpowiedniki w polskim zostana na miejscu dzieki uzyciu slownika
            slowka_ang = list(slowka_dict.keys())
            random.shuffle(slowka_ang)
            
            #Petla po wszystkich wierszach
            for keyword in slowka_ang:
                
                wyswietlanie = "{}"
                print ("\n--------------------------------------------------\nSlowko: ",(wyswietlanie.format(keyword)))
                odpowiedz = input("Twoja odpowiedz (aby zakonczyc wpisz 'z'): ")
                
                if odpowiedz == "z":
                    print("Zegnaj!")
                    break
                
                #Zapisanie wiersza ktory bedzie wrzucony do pliku do powtorki tak zeby odpowiadal formatowi plikow .csv (comma delimited)
                if odpowiedz == (slowka_dict[keyword]):
                    print ("\nOdpowiedz poprawna!")
                    odpowiedzi_lista.append(keyword + "," + slowka_dict[keyword] + "," + "7" + "," + dzisiaj.strftime(date_format))
                else:
                    print ("Odpowiedz nieprawidlowa")
                    print("Poprawna odpowiedz to: ", (slowka_dict[keyword]) + "\n")
                    odpowiedzi_lista.append(keyword + "," + slowka_dict[keyword] + "," + "0" + "," + dzisiaj.strftime(date_format))
                    
            #Jezeli plik z powtorkami nie istnieje to zostanie stworzony automatycznie 
            csv.writer(open("odpowiedzi.csv", "w"))
            #Otworz plik z odpowiedziami
            with open('odpowiedzi.csv', mode='w') as log_odpowiedzi:
                csv.writer(log_odpowiedzi, quoting=csv.QUOTE_ALL)
                #Wpisz po kolei kazdy wiersz/komorke z tablicy z odpowiedziami
                for wiersz in odpowiedzi_lista:
                    log_odpowiedzi.write(wiersz)
                    log_odpowiedzi.write("\n")
                log_odpowiedzi.close()    
    else:
        print("Zegnaj.")

if __name__== "__main__":
   main()