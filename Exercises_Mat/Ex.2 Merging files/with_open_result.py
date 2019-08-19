# 1) Stwórz plik file_3, który będzie łączył file 2 i file 1 tak, by file 1 był u góry, a file 2 na dole)
# 2) usuń kolumnę z liczbami
# 3) wyczyść tekst ze średników, myślników, okrągłych nawiasów

import pandas as pd

invo_1 = pd.read_csv("file_1.csv", sep=";", names=('text', 'number'), encoding='utf8')
invo_2 = pd.read_csv("file_2.csv", sep=";", names=('text', 'number'), encoding='utf8')

file_3 = invo_1.append(invo_2)
del file_3['number']

file_3['text'] = file_3['text'].str.replace('[\'\",\(,\),\—,]*', '', regex=True)

file_3.to_csv('file_3.csv', header=False, index=False)
