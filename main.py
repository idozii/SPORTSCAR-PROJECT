import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datapath = 'data/Elite Sports Cars in Data.csv'
data = pd.read_csv(datapath)

# Categorical: Brand, Model, Country, Fuel_Type, Drivetrain, Transmission, Popularity, Market_Demand, Modification
# Numerical: Year, Engine_Size, Condition, Horsepower, Torque, Weight, Top_Speed, Acceleration_0_100, Fuel_Efficiency, CO2_Emissions, Price, Mileage, Safety_Rating, Number_of_Owners, Insurance_Cost, Production_Units, Log_Price, Log_Mileage
# Null in Modification

# Data Cleaning
## Fill missing values with most frequent
data['Modification'] = data['Modification'].fillna('Unknown')

## Format Year
data['Year'] = data['Year'].astype(int)

## Format condition if used is 0 and new is 1
data['Condition'] = data['Condition'].str.lower()
data['Condition'] = data['Condition'].apply(lambda x: 1 if x == 'new' else 0)

print(data.head())
print(data.info())
print(data['Fuel_Type'])