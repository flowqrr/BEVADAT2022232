import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import capitalize

'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''


def csv_to_df(csv_file) -> pd.core.frame.DataFrame:
    df = pd.read_csv(csv_file)
    return df


df = csv_to_df('StudentsPerformance.csv')
# print(df)

'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''


def capitalize_columns(df_data) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_columns = {col: col.upper() for col in df.columns if 'e' not in col}
    new_df.rename(columns=new_columns, inplace=True)
    return new_df


# print(capitalize_columns(df).columns)

'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''


def math_passed_count(df_data) -> int:
    new_df = df_data.copy()
    return len(new_df[new_df['math score'] >= 50])


# print(math_passed_count(df))

'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''


def did_pre_course(df_data) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    return new_df[new_df['test preparation course'] != 'none']

# print(did_pre_course(df))

'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''
# def average_scores(df_data) -> pd.core.frame.DataFrame:
