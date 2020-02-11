# 5. Zapoznaj się z danymi dotyczącymi ofiar katastrofy Titanica. W oparciu o artykuł zawarty na stronie: 
#   https://stackabuse.com/pandas-library-for-data-visualization-in-python/ wykonaj analizę pliku z danymi. 
#   Przedstaw dane w postaci tabeli, sporządź histogram wieku ofiar, odpowiedz na pytanie - 
#   co mogło mieć wpływ na przeżycie pasażerów (płeć, wiek, status posłeczny na podstawie klasy biletu).


#   Poczatkowo, nalezy zapoznac sie z danymi jakie wystepuja w zbiorze oraz opisac je: 

#    Data Dictionary
#    Variable	Definition	Klucz
#    survival	Przezycie	0 = Nie, 1 = Tak
#    pclass	Klasa biletu	1 = pierwsza klasa, 2 = druga klasa, 3 = trzecia klasa
#    sex	Plec	
#    Age	Wiek w latach	
#    sibsp	Liczba rodzenstwa/malzonkow na pokladzie
#    parch	Liczba rodzicow/dzieci na pokladzie
#    ticket	Numer biletu
#    fare	Oplata
#    cabin	Number kabiny	
#    embarked	Port w ktorym rozpoczeto podroz	C = Cherbourg, Q = Queenstown, S = Southampton


#    Variable Notes
#    pclass: Wskaznik statusu spoleczno-ekonomicznego
#    1st = Gorny podklad
#    2nd = Srodkowy poklad
#    3rd = Dolny poklad
#    
#    age: Jezeli wiek jest mniejszy od 1 jest on przedstawiony w postaci ulamka. Jezeli wiek jest szacowany, jest on przedstawiony w formie xx.5
#    
#    sibsp: Zbior danych okresla zwiazki rodzinne dzieki tej zmiennej
#    Sibling =brat, siostra, brat przyrodni, siostra przyrodnia
#    Spouse = maz, zona (kochankowie, oraz osoby zareczone zostaly pominiete)
#    
#    parch: Zbior danych okresla zwiazki rodzinne dzieki tej zmiennej
#    Parent = matka, ojciec
#    Child = corka, syn, pasierbica, pasierb
#    Niektore dzieci podrozowaly z opienkunka, w takiej syuacji ilosc zwiazkow rodzinnych wynosila 0.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def interpolation(training_data):
    # Interpolacja jest uzywana aby oszacowac brakujace wartosci w zbiorze. Na potrzeby metody zbior zostal podzielony na 5 podzbiorow: Miss, Master, Mrs, Mr oraz Other
    # Podzial ten zostal wykonany na podstawie formy grzeczosciowej w imieniu. 
    # Wszystkie elementy bez przedrostka, badz z przedrostkami nietypowymi, zostaly przydzielone do kategori "other". 
    # W ok. 20% pozycji brakuje zmiennej dla wieku. Z powodu szerokiego rozrzutu wieku i tego, ze brakuje okolo 20% danych, 
    # wyliczenie sredniej z calego zbioru i interpolacja przy jej pomocy dalaby nam wynik niekorzystny. 
    # Uogolniajac, mozna przyjac ze mlode kobiety niezamezne nosily przydomek Miss, za to kobiety starsze zamezne Mrs. Analogiczne dla mezczyzn. 
    # Na tej podstawie wyliczamy srednia wieku dla kazdego ze zbiorow i ta wartoscia uzupelniam brakujace elementy. 
    
    miss_data = training_data[training_data['name'].str.contains("Miss.")]
    miss_data_median = miss_data["age"].median(skipna=True)
    
    master_data = training_data[training_data['name'].str.contains("Master.")]
    master_data_median = master_data["age"].median(skipna=True) 
    
    mrs_data = training_data[training_data['name'].str.contains("Mrs.")]
    mrs_data_median = mrs_data["age"].median(skipna=True)
    
    mr_data = training_data[training_data['name'].str.contains("Mr.")]
    mr_data_median = mr_data["age"].median(skipna=True)
    
    other_data_median = training_data["age"].median(skipna=True)
    

    training_data.loc[(training_data['name'].str.contains("Miss.")) & (training_data['age'].isnull()), 'age'] = miss_data_median
    training_data.loc[(training_data['name'].str.contains("Master.")) & (training_data['age'].isnull()), 'age'] = master_data_median
    training_data.loc[(training_data['name'].str.contains("Mrs.")) & (training_data['age'].isnull()), 'age'] = mrs_data_median
    training_data.loc[(training_data['name'].str.contains("Mr.")) & (training_data['age'].isnull()), 'age'] = mr_data_median
    
    training_data["age"].fillna(other_data_median, inplace=True)
    
    
    # Ok 80% wpisow dla zmiennej 'Cabin' jest niedostepnych. Jako, ze sa to dane nieistotne statystycznie dla ponizszej analizy, zostaly one wykluczone ze zbioru. 
    training_data.drop('cabin', axis=1, inplace=True)
    
    # Dla zmiennej 'Embarked' brakuje tylko 2 wpisow. Zostaly one uzupelnione najczesciej wystepujacym miejscem dolaczenia na statek. 
    embarked_mode = training_data.mode()['embarked'][0]
    training_data["embarked"].fillna(embarked_mode, inplace=True)

    

def barvalues(ax, x, y):
    for i in ax.patches:
        ax.text(i.get_x()+x, i.get_height()+y, \
                str(i.get_height()), fontsize=15,
                    color='black')


def plotting(training_data):
    ##########################################################
    # Analiza przezycia z podzialem na plec i klase
    survivors = training_data[training_data['survived'] == 1]
    survivors.dropna(subset=['sex', 'pclass'])
    ax = survivors.groupby(['sex', 'pclass'])['survived'].agg('sum').unstack().plot(kind="bar", title='Ocaleni: status i plec')
    barvalues(ax, .025, 5)
    
    # Ze zbioru 'survived' zostaly wyciagniete jedynie elementy ktore wskazywaly na przezycie. Tworzony jest podzbior plci od klasy z wykluczeniem N/A
    # Uzyta zostala stworzona pozyzej funkcja 'barvalues', ktora przedstawia na wykresie wartosci liczbowe dla kazdej z kolumn
    
    ##########################################################
    # Analiza przezycia z podzialem na wiek i plec
    survived = 'Osoby, ktore przezyly'
    not_survived = 'Osoby, ktore nie przezyly'
    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 5))
    women = training_data[training_data['sex']=='female']
    men = training_data[training_data['sex']=='male']
    
    ax = sns.distplot(women[women['survived']==1].age.dropna(), bins=18, label = survived, ax = axes[0], kde =False)
    ax = sns.distplot(women[women['survived']==0].age.dropna(), bins=40, label = not_survived, ax = axes[0], kde =False)
    ax.legend()
    ax.set_title('Kobiety')
    ax = sns.distplot(men[men['survived']==1].age.dropna(), bins=18, label = survived, ax = axes[1], kde = False)
    ax = sns.distplot(men[men['survived']==0].age.dropna(), bins=40, label = not_survived, ax = axes[1], kde = False)
    ax.legend()
    ax.set_title('Mezczyzni')
    
    # Z uzyciem funkcji subplots stworzone zostaly dwa osobne wykresy z podzialem na plec. 
    # Ze zbioru zostaly wyciagniete wszystkie warosci dla kobiet ktore przezyly, oraz ktore nie przezyly, oraz zostaly przestawione na wykresie z pominieciem wartosci N/A
    # Analogiczny zabieg zostal wykonany dla zbioru mezczyzn
    
    #########################################################
    # Wspolczynnik przezycia z podzialem na plec
    survived = training_data[training_data['survived']==1]
    survived.dropna(subset=['sex'])
    
    not_survived = training_data[training_data['survived']==0]
    not_survived.dropna(subset=['sex'])
    
    
    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 5))  
    
    ax = survived.sex.value_counts().plot(kind='bar', alpha=1.0, color=['darkblue', 'red'], ax = axes[0])
    barvalues(ax, .15, 10)

    
    ax.set_title('Ocaleni')
    ax = not_survived.sex.value_counts().plot(kind='bar', alpha=1.0, color=['darkblue', 'red'], ax = axes[1])
    ax.set_title('Nieocaleni')
    barvalues(ax, .15, 10)
    
    # Stworzone zostaly dwa wykresy dla osob ktore ocalaly z katastrofy oraz nieocalonych, z podzialem na plec i z pominieciem wartosci N/A

    ##########################################################    
    # Ogolny podzial pasazerow z podzialem na miejsce rozpoczecia podrozy    
    all_embarked = training_data
    all_embarked.dropna(subset=['embarked'])
    
    # Podzial ocalonych pasazerow z podzialem na miejsce rozpoczecia podrozy
    survivors_embarked = training_data[training_data['survived'] == 1]
    survivors_embarked.dropna(subset=['embarked'])    
    
    
    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 5))  
    
    # Wykres dla wszystkich pasazerow
    ax = all_embarked.embarked.value_counts().plot(kind='bar', alpha=1.0, color=['lightblue', 'green', 'orange'], ax = axes[0])
    ax.set_title("Wszyscy pasazerowie")
    barvalues(ax, .1, 10)
    
    # Wykres dla ocalalych pasazerow
    ax = survivors_embarked.embarked.value_counts().plot(kind='bar', alpha=1.0, color=['lightblue', 'green', 'orange'], ax = axes[1])
    ax.set_title("Ocaleni a miejsce rozpoczecia")
    barvalues(ax, .1, 10) 
    
    # Dla wszystkich powyzszych zbiorow, pominiete zostaly wartosci N/A

def description(training_data):
    # Ponizsze funkcje to tekstowe i liczbowe opisy danych 
    
    # Przedstawienie pierwszych 10 wierszy ze zbioru danych
    print("\n----------------------------------------\nPierwsze kilka wierszy danych")
    print( training_data.head(10) )
    
    # Sprawdzenie wartosci dla kategorii.  
    print("\n----------------------------------------\nInformacje na temat kazdej z kolumn")
    training_data.info()
    # Kategorie wiek, kabina i miejsce rozpoczenia podrozy sa niekompletne
    
    # Opis statystyczny poszczegolnych kolumn. Zliczenie danych, wyliczenie sredniej, odchylenia standardowego, kwantyli, minimun i maksimun.
    print("\n----------------------------------------\nMatematyczny opis kazdej z kolumn")
    print(training_data.describe())
    
    # Opis statystyczny kolumn nienumerycznych. Zliczenie danych, unikalne wartosci, czestosi powtorek. 
    print("\n----------------------------------------\nStatystyczny opis kolumn nienumerycznych")
    print(training_data.describe(include=['object']))
    
    # Procentowe zestawienie brakujacych danych
    total = training_data.isnull().sum().sort_values(ascending=False)
    percent_1 = training_data.isnull().sum()/training_data.isnull().count()*100
    percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
    missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])
    print("\n----------------------------------------\nProcentowe zestawienie brakujacych/niebrakujacych danych")
    print(missing_data)


def main():

    training_data = pd.read_csv(r"C:\Users\wturcza\Downloads\python_\train.csv")

    training_data.columns = map(str.lower, training_data.columns)
    
    description(training_data)
    
    plotting(training_data)

    interpolation(training_data)
    
    description(training_data)

    plotting(training_data)



if __name__=="__main__":
    main()

    # Przedstawione wykresy dokladnie wskazuja ze, kobiety znajdujace sie na statku mialy o wiele wieksze prawdopodobienstwo przezycia od mezczyzn 
    # Wiadac, ze zasada, ktora zostala przedstawiona w filmie - "Women and children first" ma realne odzwierciedlenie w analizowanym zbiorze danych. 
    # Klasa spoleczna miala wysoki wplyw na przezywalnosc katastrofy. Osoby podrozujace w pierwszej klasie cechuja sie najwyszym wspolczynnikiem przezycia. 
    # Zaskakujaco, osoby podrozujace w klasie drugiej cechuja sie najnizsza przezywalnoscia. 
    # Male dzieci, ponizej 10 roku zycia cechuja sie wysoko przezywalnoscia katastrofy. Glownymi ofiarami katastrofy byli mezczyzni w wieku pomiedzy 18-35 lat. 
    # Miejsce rozpoczecia podrozy cechuje sie niska istostnoscia statystyczna. Mozna stwierdzic, iz miejsce rozpoczecia podrozy nie mialo wiekszego wplywu na przezywalnosc
    # - rozklad przezyc jest bardzo zblizony do poczatkowego zbioru danych zawierajacego wszystkich pasazerow. 
    
    # Nastepny pakiet wykresow przedstawia te same dane ktore zostaly poddane zabiegowi interpolacji. 
    # Interpolacja nie miala wplywu na wykres przedstawiajacy status spoleczny i plec z powodu braku wystepowania wartosci N/A
    # Na wykresie przestawiajacym przezycie z podzialem na wiek i plec nozemy zauwazyc znaczny wzrost ilosci wystepowan w wieku 20 lat dla kobiet i ok 30 lat dla mezczyzn 
    # Spowodowane jest to wyliczeniem sredniej ze zbiorow celem okreslenia sredniego wieku osob poleglych w katastrowie. Wszystkie wartosci N/A zostaly zastapione miara sredniej.
    # Objeta metoda, powoduje znaczny wzrost wartosci 31 lat dla mezczyzn, jednak ukazuje ona wartosci o wiele bardziej zblizone do rzeczywistosci, niz jezeli uzylibysmy sredniej dla calego zbioru danych.
    # Wartosc tak ukazuje miejsce koncentracji zbioru, oraz potwiedza wczesniej postawiona hipoteze o wysokiej smierelnosci osob w tym wieku. 
    # Interpolacja nie miala wplywu na trzeci wykres ocaleni vs. plec z powodu braku wystepowania wartosci N/A
    # W wykresie przedstawiajacym miejsce rozpoczecia podrozy, wszelkie wartosci N/A zostaly zastapione moda. Zabieg taki zostal podjety, poniewaz tylko 2 wartosci przedstawialy N/A
    # Wykres rozpoczecia podrozy nie ulegl dluzym zmianiom i nadal jest nieistotny statystycznie. 
    
    # Podsumowujac, z powyzszej analizy wynika, iz najwieksza szanse przezycia mialy kobiety podrozujace klasa I oraz dzieci. 
    # Najnizszym wskaznikiem przezycia cechuja sie mezczyzni w wieku 18-35 lat. 
    