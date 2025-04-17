import pandas as pd
import numpy as np
import os

data= pd.read_csv('smartphones.csv')
data = data.dropna()
data = data.drop_duplicates()
data = data.reset_index(drop=True)


#brand name
brand_name= data['brand_name'].str.lower()
brand_name= brand_name.drop_duplicates()
brand_name= brand_name.reset_index(drop=True)
brand_name= brand_name.dropna()

print(brand_name)
company_name= input("Enter the company name: ")

#model name
model_name= data[(data['brand_name']==company_name)]
model_name= model_name.drop_duplicates()
model_name= model_name.reset_index(drop=True)
model_name= model_name.dropna()

print(model_name)

