import numpy as np


# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()
def column_swap(input_array: np.array) -> np.array:
    return_array = np.array(input_array[:, [1, 0]])
    return return_array


#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek
# Pl Be: [7,8,9], [9,8,7]
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön
def compare_two_array(input_array1: np.array, input_array2: np.array) -> np.array:
    if input_array1.shape == input_array2.shape:
        return np.where(np.equal(input_array1, input_array2))[0]
    return False


#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!
def get_array_shape(input_array: np.array) -> str:
    if len(input_array.shape) == 3:
        return f"sor: {input_array.shape[0]}, oszlop: {input_array.shape[1]}, melyseg: {input_array.shape[2]}"
    elif len(input_array.shape) == 2:
        return f"sor: {input_array.shape[0]}, oszlop: {input_array.shape[1]}, melyseg: 1"
    else:
        return input_array.shape

print(get_array_shape(np.array([[1,2,3], [4,5,6]])))
