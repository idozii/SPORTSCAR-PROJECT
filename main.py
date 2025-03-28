import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datapath = 'data/Elite Sports Cars in Data.csv'
data = pd.read_csv(datapath)

# Data Cleaning
## Fill missing values with most frequent
data['Modification'] = data['Modification'].fillna('Unknown')

## Format Year
data['Year'] = data['Year'].astype(int)

## Format condition
### 0: Used, 1: New
data['Condition'] = data['Condition'].str.lower()
data['Condition'] = data['Condition'].apply(lambda x: 1 if x == 'new' else 0)

## Format Fuel_Type
### 0: petrol, 1: diesel, 2: electric
data['Fuel_Type'] = data['Fuel_Type'].str.lower()
data['Fuel_Type'] = data['Fuel_Type'].apply(lambda x: 0 if x == 'petrol' else (1 if x == 'diesel' else 2))

## Format Drivetrain
### 0: RWD, 1: AWD, 2: FWD
data['Drivetrain'] = data['Drivetrain'].str.lower()
data['Drivetrain'] = data['Drivetrain'].apply(lambda x: 0 if x == 'rwd' else (1 if x == 'awd' else 2))

## Format Transmission
### 0: CVT, 1: Automatic, 2: DCT, 3: Manual
data['Transmission'] = data['Transmission'].str.lower()
data['Transmission'] = data['Transmission'].apply(lambda x: 0 if x == 'cvt' else (1 if x == 'automatic' else (2 if x == 'dct' else 3)))

## Format Popularity
### 0: Low, 1: Medium, 2: High
data['Popularity'] = data['Popularity'].str.lower()
data['Popularity'] = data['Popularity'].apply(lambda x: 0 if x == 'low' else (1 if x == 'medium' else 2))

## Format Market_Demand
### 0: Low, 1: Medium, 2: High
data['Market_Demand'] = data['Market_Demand'].str.lower()
data['Market_Demand'] = data['Market_Demand'].apply(lambda x: 0 if x == 'low' else (1 if x == 'medium' else 2))

# Categorical: Brand, Model, Country, Modification
# Numerical: Year, Engine_Size, Condition, Transmission, Market_Demand, Popularity, Fuel_Type, Drivetrain, Horsepower, Torque, Weight, Top_Speed, Acceleration_0_100, Fuel_Efficiency, CO2_Emissions, Price, Mileage, Safety_Rating, Number_of_Owners, Insurance_Cost, Production_Units, Log_Price, Log_Mileage
# Null in Modification

# Data Exploration
## Brand
brand = data['Brand'].value_counts()
