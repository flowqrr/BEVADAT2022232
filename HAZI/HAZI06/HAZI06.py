"""
1. Értelmezd az adatokat!!!

2. Írj egy osztályt a következő feladatokra:  
     - Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     - Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     - Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     - Dobjuk el a from és a to oszlopokat, illetve a nan-okat és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     - A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     - Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    - A késéeket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0 <= x 5  --> 0  
         5 <= x    --> 1  
    - Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    - Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    - Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik, ha 5 < x --> késik.
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál,
mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el.
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

HAZI06-
    -NJCleaner.py
    -HAZI06.py

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from NJCleaner import NJCleaner
from GYAK.GYAK06.GYAK06 import DecisionTreeClassifier

base_csv_path = "datasets/NJ_Transit+Amtrak.csv"
clean_csv_path = "datasets/NJ.csv"

nj_cleaner = NJCleaner(base_csv_path)
nj_cleaner.prep_df(clean_csv_path)

data = pd.read_csv(clean_csv_path)

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=4)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

# results = []

# for min_sample_split in range(1, 6):
#     for max_depth in range(1, 5):
#         classifier = DecisionTreeClassifier(min_samples_split=min_sample_split, max_depth=max_depth)
#         classifier.fit(X_train, Y_train)
#
#         Y_pred = classifier.predict(X_test)
#         intermediate_result = (min_sample_split, max_depth, accuracy_score(Y_test, Y_pred))
#         print(intermediate_result)
#         results.append(intermediate_result)
#
# print(results)
# print(max(results, key=lambda x: x[2]))
# with open("datasets/results.txt", 'w') as results_file:
#     sorted_results = sorted(results, key=lambda x: x[2], reverse=True)
#     for result_line in sorted_results:
#         results_file.write(', '.join(map(str, result_line)) + "\n")
