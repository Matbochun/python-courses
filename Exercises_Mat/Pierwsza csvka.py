#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np

file = 'pierwsza_csvka.csv'
df = pd.read_csv(file)
print(df.columns)
print(df.head())


# In[ ]:


# 1.Dodaj nazwy kolumn ’Słowa / ByeBye / Liczby / Random / Pojemności`
df = pd.DataFrame(df, columns = ['Słowa', 'ByeBye', 'Liczby', 'Random', 'Pojemności'])
print(df.head())

# In[3]:

# 2.Usuń drugą kolumnę(ByeBye)
df = df.drop(columns='ByeBye')
print(df.head())

# In[4]:

# 3. Dla kolumny “Random” wpisz we wszystkie wiersze randomowe liczby 
# (np. Używając wbudowanej w pythona metody random)
import numpy as np
df['Random'] = np.random.randint(0,100,size=(len(df),1))
print(df.head())

# In[5]:

# 4. Dodaj kolumnę `l.p.`, która będzie pierwszą kolumną i będzie wskazywała indeksy poszczególnych wierszy
df['l.p'] = range(1, len(df) + 1)
df = df.set_index('l.p')
print(df.head())

#? Czy mogę połączyć dodawanie i ustawianie kolumny jako indeks w jednym kroku?
#? Czemu l.p jest niżej niż nazwy pozostałych kolumn?


# In[ ]:




