import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# 1
def csv_to_df(csv_file: str) -> pd.core.frame.DataFrame:
    df = pd.read_csv(csv_file)
    return df


# df = csv_to_df('StudentsPerformance.csv')
# print(df)

'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# 2
def capitalize_columns(df_data) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_columns = {col: col.upper() for col in new_df.columns if 'e' not in col}
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

# 3
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

# 4
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

# 5
def average_scores(df_data) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    df_average_scores = new_df.groupby('parental level of education')[
        ['math score', 'reading score', 'writing score']].mean()
    return df_average_scores


# print(average_scores(df))

'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# 6
def add_age(df_data) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    np.random.seed(42)
    new_df['age'] = np.random.randint(low=18, high=67, size=len(df_data))
    return new_df


# print(add_age(df))

'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# 7
def female_top_score(df_data) -> tuple:
    new_df = df_data.copy()
    female_df = new_df[new_df['gender'] == 'female']
    top_female = female_df.loc[(female_df[['math score', 'reading score', 'writing score']].sum(axis=1)).idxmax()]
    return (top_female['math score'], top_female['reading score'], top_female['writing score'])


# print(female_top_score(df))

'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# 8
def add_grade(df_data) -> pd.core.frame.DataFrame:
    def calculate_grade(score):
        percentage = score / 300 * 100
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'

    new_df = df_data.copy()
    new_df['grade'] = new_df[['math score', 'reading score', 'writing score']].sum(axis=1).apply(calculate_grade)
    return new_df


# print(add_grade(df))

'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# 9
def math_bar_plot(df_data): # -> plt.Figure:
    new_df = df_data.copy()
    fig, ax = plt.subplots()
    new_df = new_df.groupby('gender')['math score'].mean()
    ax.bar(new_df.index, new_df.values)
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    return fig


# plot = math_bar_plot(df)
# plt.show()

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# 10
def writing_hist(df_data): # -> plt.Figure:
    new_df = df_data.copy()
    fig, ax = plt.subplots()
    ax.hist(new_df['writing score'])
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    return fig

# plot = writing_hist(df)
# plt.show()

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# 11
def ethnicity_pie_chart(df_data): # -> plt.Figure:
    new_df = df_data.copy()
    ethnicity_counts = new_df['race/ethnicity'].value_counts()
    total_count = new_df.shape[0]
    ethnicity_percents = [count / total_count * 100 for count in ethnicity_counts.values]
    fig, ax = plt.subplots()
    ax.pie(ethnicity_percents, labels=ethnicity_counts.index.tolist(), autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig

# plot = ethnicity_pie_chart(df)
# plt.show()

