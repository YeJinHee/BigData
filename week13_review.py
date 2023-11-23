import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print(titanic.isnull().sum())

#print(titanic.head())
#print(titanic.describe())
#print(titanic.info())
#print(titanic.tail())
#print(titanic())
