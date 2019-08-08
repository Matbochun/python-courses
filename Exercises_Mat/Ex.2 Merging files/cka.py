#!/usr/bin/env python
# coding: utf-8

'''
1) Stwórz plik file_3, który będzie łączył file 2 i file 1 tak, by file 1 był u góry, a file 2 na dole)
2) Usuń kolumnę z liczbami
3) Wyczyść tekst ze średników, myślników, okrągłych nawiasów
'''

import pandas as pd

df1 = pd.read_csv('file_1.csv', sep=';', names = ["Text", "Numbers"])
print(df1.head())

df2 = pd.read_csv('file_2.csv', sep=';', names = ["Text", "Numbers"])
print(df2.head())

# Deleting column with numbers in file_1
df1 = df1.drop(df1.columns[1], axis=1)
print(df1.head())

# Deleting column with numbers in file_2
df2 = df2.drop(df2.columns[1], axis=1)
print(df2.head())

# Merging files 1 and 2 into file 3
file3 = pd.concat([df1, df2], axis = 1, sort=True)
print(file3)




