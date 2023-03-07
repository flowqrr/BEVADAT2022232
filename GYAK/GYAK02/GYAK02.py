import numpy as np


# Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
# Paraméterei: mérete (tupel-ként), default mérete pedig legyen egy (2,2)
# Be: (2,2)
# Ki: [[0,0],[0,0]]
# create_array()
def create_array(size: tuple = (2, 2)) -> np.array:
    return np.zeros(size)


# Készíts egy függvényt ami a paraméterként kapott array-t főátlót feltölti egyesekkel
# Be: [[1,2],[3,4]]
# Ki: [[1,2],[3,1]]
# set_one()
def set_one(input_array: np.array) -> np.array:
    np.fill_diagonal(input_array, 1)
    return input_array


# Transzponáld a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()
def do_transpose(input_array: np.array) -> np.array:
    return np.transpose(input_array)


# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, alapértelmezetten
# Be: [0.1223, 0.1675], n = 2
# Ki: [0.12, 0.17]
# round_array()
def round_array(input_array: np.array = np.array([0.1223, 0.1675]), n: int = 2) -> np.array:
    return np.round(input_array, n)


# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 0 - False-ra az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()
def bool_array(input_array: np.array) -> np.array:
    return input_array == 1


# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()
def invert_bool_array(input_array: np.array) -> np.array:
    return input_array == 0


# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()
def flatten(input_array: np.array) -> np.array:
    return np.concatenate(input_array)
