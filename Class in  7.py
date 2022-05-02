import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


titanic =pd.read_csv("titanic.csv")
#pd.read_xlsx
print(titanic.head(5))
print(titanic.tail(5))
print(titanic.sample(5)) #randomly picks 5 rows

#id variables
print(titanic.dtypes) #dtypes tells if data is floating, object, intg
print(titanic.describe()) #it gives mean ,med, max, n for numeric values


#categorical data
print(titanic.name.value_counts())

#numeric data analysis
print(titanic['age'].median())

#scatter plot
x = titanic['age']
plt.xlabel ('age')
plt.ylabel ('frequency')
plt.hist(x)
plt.show


#histogram
x = titanic['age']
plt.xlabel ('age')
plt.ylabel ('frequency')
plt.hist(x) # plt.hist(x, bins = 15)
plt.show()

#bar diagram
x= titanic['sex']
y = titanic['age']
plt.bar(x,y, color ='red', width =0.1)
plt.show()