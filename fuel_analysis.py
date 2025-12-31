import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#display the dataset 
petrol = pd.read_csv('petrolprices.csv', delimiter = ';')
petrol.head()

#setting year and month as index columns 
petrol = petrol.set_index(['Year','Month'])
petrol

#creating a price difference column 
petrol['Price Difference'] = petrol['Diesel'] - petrol['Petrol']
petrol

#I used loc function to display on data from the 2023 year 
petrol2023 = petrol.loc[2023]
petrol2023

#I used loc function to display on data from the 2023 year 
petrol2024 = petrol.loc[2024]
petrol2024

#displaying data only for the 2023 year and removing the price difference column as the quesion paper required 
petrol2023.drop(columns = 'Price Difference').plot(kind = 'line')

petrol2024.drop(columns = 'Price Difference').plot(kind = 'line')

petrol.drop(columns = 'Price Difference').plot(kind = 'line')

petrol['Price Difference'].plot(kind = 'line')
