import copy

import numpy as np
from matplotlib import pyplot as plt

import torch as to
f = open("/Users/bart/python/Terminal_test/final_results.txt", "r")
zawartosc = f.read()
f.close()

zawartosc =  zawartosc.split('\n')

DC_size = list(zawartosc[0].split(','))
DC_size = [float(x) for x in DC_size]
#DC_size = to.tensor(DC_size)

DC_shift = list(zawartosc[1].split(','))
DC_shift = [float(x) for x in DC_shift]
#DC_shift = to.tensor(DC_shift)

size, shift = np.meshgrid(DC_size, DC_shift, indexing = 'ij')

result = copy.deepcopy(size)

def return_number_of_rides(header_size, size, shift):
    index_of_size = DC_size.index(size)
    index_of_shift = DC_shift.index(shift)
    number_of_line = header_size + index_of_size * len(DC_shift) + index_of_shift
    file_data = zawartosc[number_of_line].split(',')
    return file_data[4]


for i, n in enumerate(DC_size):
    for j, m in enumerate(DC_shift):
        result[i][j] = return_number_of_rides(3, n, m)

def normalize_2d(matrix):
    norm = np.max(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix

print(size)
print(shift)
print(result)
result = normalize_2d(result)

fig, ax = plt.subplots()
CS = ax.contour(size, shift, result, 20)
ax.clabel(CS, inline = 1, fontsize = 10)
ax.set_title('plot of deflection in lengh and thickness')
plt.show()

# to co chce teraz zrobic
# to przezucic te dane z pliku txt do jakiegas formatu danych
# jak juz bede cisnac dalej z tym to pytanie jak to przetwozyc
# w praktyce potrzebny mi jest format tego co sie dzieje przy wyswietlaniu czyli mam macierz
# z wynikami w okreslonym formacie
# mam macierz z jednym parametrem wejsciowym
# mam macierz z kolejnym parametrem wejsciowym
# idac po tych wejsciowych macierzach
