import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datapath = 'data/Elite Sports Cars in Data.csv'
data = pd.read_csv(datapath)

# Data Cleaning
## Fill missing values with Unknown
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
## Brand (Ferrari highest, Lamborghini last)
brand = data['Brand'].value_counts()
brand.plot(kind='bar')
plt.savefig('visualize/single/brand.png')
plt.clf()

## Model
model = data['Model'].value_counts()
model.plot(kind='bar')
plt.savefig('visualize/single/model.png')
plt.clf()

## Country (Asia ~ Europe > US)
country = data['Country'].value_counts()
country.plot(kind='bar')
plt.savefig('visualize/single/country.png')
plt.clf()

## Year
year = data['Year'].value_counts()
year.plot(kind='bar')
plt.savefig('visualize/year.png')
plt.clf()

## Engine_Size
engine_size = data['Engine_Size'].value_counts()
engine_size.plot(kind='pie')
plt.savefig('visualize/engine_size.png')
plt.clf()

## Condition (New > Used)
condition = data['Condition'].value_counts()
condition.plot(kind='bar')
plt.savefig('visualize/condition.png')
plt.clf()

## Transmission (CVT > Automatic > DCT > Manual)
transmission = data['Transmission'].value_counts()
transmission.plot(kind='bar')
plt.savefig('visualize/transmission.png')
plt.clf()

## Market_Demand (Low > Medium > High)
market_demand = data['Market_Demand'].value_counts()
market_demand.plot(kind='bar')
plt.savefig('visualize/market_demand.png')
plt.clf()

## Popularity (Low > High > Medium)
popularity = data['Popularity'].value_counts()
popularity.plot(kind='bar')
plt.savefig('visualize/popularity.png')
plt.clf()

## Fuel_Type (Petrol > Diesel > Electric)
fuel_type = data['Fuel_Type'].value_counts()
fuel_type.plot(kind='bar')
plt.savefig('visualize/fuel_type.png')
plt.clf()

## Drivetrain (RWD > AWD > FWD)
drivetrain = data['Drivetrain'].value_counts()
drivetrain.plot(kind='bar')
plt.savefig('visualize/drivetrain.png')
plt.clf()

## Horsepower
horsepower = data['Horsepower'].value_counts()
horsepower.plot(kind='hist')
plt.savefig('visualize/horsepower.png')
plt.clf()

## Torque
torque = data['Torque'].value_counts()
torque.plot(kind='hist')
plt.savefig('visualize/torque.png')
plt.clf()

