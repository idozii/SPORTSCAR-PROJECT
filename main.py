import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

datapath = 'data/Elite Sports Cars in Data.csv'
data = pd.read_csv(datapath)

# Datetime: Year
# Categorical: Brand, Model, Country, Condition Modification, Fuel_Type, Drivetrain, Transmission, Popularity, Market_Demand, Modification
# Numerical: Engine_Size, Horsepower, Torque, Weight, Top_Speed, Acceleration_0_100, Fuel_Efficiency, CO2_Emissions, Price, Mileage, Safety_Rating, Number_of_Owners, Insurance_Cost, Production_Units, Log_Price, Log_Mileage
# Null in Modification

# Data Cleaning
## Fill missing values with Unknown
data['Modification'] = data['Modification'].fillna('Unknown')

## Format Year using pd.to_datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y', errors='coerce')

## Format Brand in Categorical Data using LabelEncoder
labelencoder = LabelEncoder()
data['Brand'] = labelencoder.fit_transform(data['Brand'])

## Format Model in Categorical Data using LabelEncoder
data['Model'] = labelencoder.fit_transform(data['Model'])

## Format Country in Categorical Data using LabelEncoder
data['Country'] = labelencoder.fit_transform(data['Country'])

## Format Modification in Categorical Data using LabelEncoder
data['Modification'] = labelencoder.fit_transform(data['Modification'])

## Format Condition in Categorical Data using LabelEncoder
data['Condition'] = labelencoder.fit_transform(data['Condition'])

## Format Fuel_Type in Categorical Data using LabelEncoder
data['Fuel_Type'] = labelencoder.fit_transform(data['Fuel_Type'])

## Format Drivetrain in Categorical Data using LabelEncoder
data['Drivetrain'] = labelencoder.fit_transform(data['Drivetrain'])

## Format Transmission in Categorical Data using LabelEncoder
data['Transmission'] = labelencoder.fit_transform(data['Transmission'])

## Format Popularity in Categorical Data using LabelEncoder
data['Popularity'] = labelencoder.fit_transform(data['Popularity'])

## Format Market_Demand in Categorical Data using LabelEncoder
data['Market_Demand'] = labelencoder.fit_transform(data['Market_Demand'])

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
plt.savefig('visualize/single/year.png')
plt.clf()

## Engine_Size
engine_size = data['Engine_Size'].value_counts()
engine_size.plot(kind='pie')
plt.savefig('visualize/single/engine_size.png')
plt.clf()

## Condition (New > Used)
condition = data['Condition'].value_counts()
condition.plot(kind='bar')
plt.savefig('visualize/single/condition.png')
plt.clf()

## Transmission (CVT > Automatic > DCT > Manual)
transmission = data['Transmission'].value_counts()
transmission.plot(kind='bar')
plt.savefig('visualize/single/transmission.png')
plt.clf()

## Market_Demand (Low > Medium > High)
market_demand = data['Market_Demand'].value_counts()
market_demand.plot(kind='bar')
plt.savefig('visualize/single/market_demand.png')
plt.clf()

## Popularity (Low > High > Medium)
popularity = data['Popularity'].value_counts()
popularity.plot(kind='bar')
plt.savefig('visualize/single/popularity.png')
plt.clf()

## Fuel_Type (Petrol > Diesel > Electric)
fuel_type = data['Fuel_Type'].value_counts()
fuel_type.plot(kind='bar')
plt.savefig('visualize/single/fuel_type.png')
plt.clf()

## Drivetrain (RWD > AWD > FWD)
drivetrain = data['Drivetrain'].value_counts()
drivetrain.plot(kind='bar')
plt.savefig('visualize/single/drivetrain.png')
plt.clf()

## Horsepower
horsepower = data['Horsepower'].value_counts()
horsepower.plot(kind='hist')
plt.savefig('visualize/single/horsepower.png')
plt.clf()

## Torque
torque = data['Torque'].value_counts()
torque.plot(kind='hist')
plt.savefig('visualize/single/torque.png')
plt.clf()

### Weight
weight = data['Weight'].value_counts()
weight.plot(kind='hist')
plt.savefig('visualize/single/weight.png')
plt.clf()

### Top_Speed
top_speed = data['Top_Speed'].value_counts()
top_speed.plot(kind='hist')
plt.savefig('visualize/single/top_speed.png')
plt.clf()

### Price
price = data['Price'].value_counts()
price.plot(kind='hist')
plt.savefig('visualize/single/price.png')
plt.clf()

## Correlation
correlation = data.corr()
plt.figure(figsize=(20, 20))
sns.heatmap(correlation, annot=True)
plt.savefig('visualize/correlation/correlation.png')
plt.clf()

# Data Preprocessing
## Drop columns
X = data.drop(columns=['Price', 'Year'])
y = data['Price']

## Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Standardize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Training for Regression
## Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred = lr_model.predict(X_test)

lr_mse = mean_squared_error(y_test, y_pred)
lr_mae = mean_absolute_error(y_test, y_pred)

sns.regplot(x=y_test, y=y_pred)
plt.savefig('visualize/regression/linear_regression.png')
plt.clf()

## Random Forest Regressor
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

rf_mse = mean_squared_error(y_test, y_pred)
rf_mae = mean_absolute_error(y_test, y_pred)

sns.regplot(x=y_test, y=y_pred)
plt.savefig('visualize/regression/random_forest_regressor.png')
plt.clf()

print(f'Linear Regression: MSE={lr_mse}, MAE={lr_mae}')
print(f'Random Forest Regressor: MSE={rf_mse}, MAE={rf_mae}')

# Model Training for Classification
## LabelEncoder for Price
labelencoder = LabelEncoder()
data['Price'] = labelencoder.fit_transform(data['Price'])

## Drop columns
X = data.drop(columns=['Price', 'Year'])
y = data['Price']

## Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

