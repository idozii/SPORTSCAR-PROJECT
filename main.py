import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datapath = 'data/Elite Sports Cars in Data.csv'
data = pd.read_csv(datapath)

# Categorical: Brand, Model, Country, Condition, Fuel_Type, Drivetrain, Transmission, Popularity, Market_Demand, Modification
# Numerical: Year, Engine_Size, Horsepower, Torque, Weight, Top_Speed, Acceleration_0_100, Fuel_Efficiency, CO2_Emissions, Price, Mileage, Safety_Rating, Number_of_Owners, Insurance_Cost, Production_Units, Log_Price, Log_Mileage
# Null in Modification

# Data Cleaning
## Fill missing values with most frequent
data['Modification'] = data['Modification'].fillna('Unknown')

##