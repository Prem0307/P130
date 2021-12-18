import pandas as pd 
import csv 

df=pd.read_csv("total_stars.csv")
print(df.shape)


del df["Luminosity"]
del df["Star_name"]
del df["Radius"]
del df["Mass"]

print(df.shape)
print(list(df))

df.to_csv('final_stars.csv')

