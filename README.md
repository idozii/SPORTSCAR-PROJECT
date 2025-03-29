# 🚗 Elite Sports Cars Data Analysis

This project analyzes data on elite sports cars, including data cleaning, exploration, visualization, and model training for regression, classification, and clustering.

## 📁 Project Structure

```plaintext
Elite Sports Cars Data Analysis/
├── 📂 data/
│   └── 📄 Elite Sports Cars in Data.csv
├── 📄 main.py
├── 📄 README.md
├── 📄 requirements.txt
├── 📂 visualize/
│   ├── 📂 classification/
│   │   ├── 🖼️ condition.png
│   │   └── 🖼️ popularity.png
│   ├── 📂 correlation/
│   │   └── 🖼️ correlation.png
│   ├── 📂 regression/
│   │   ├── 🖼️ linear_regression.png
│   │   └── 🖼️ random_forest_regressor.png
│   └── 📂 single/
│       ├── 🖼️ brand.png
│       ├── 🖼️ condition.png
│       ├── 🖼️ country.png
│       ├── 🖼️ drivetrain.png
│       ├── 🖼️ engine_size.png
│       ├── 🖼️ fuel_type.png
│       ├── 🖼️ horsepower.png
│       ├── 🖼️ market_demand.png
│       ├── 🖼️ model.png
│       ├── 🖼️ price.png
│       ├── 🖼️ top_speed.png
│       ├── 🖼️ torque.png
│       ├── 🖼️ transmission.png
│       ├── 🖼️ weight.png
│       └── 🖼️ year.png
```

## 📊 Data

The dataset `Elite Sports Cars in Data.csv` contains various features of elite sports cars, including:

- **Datetime**: Year
- **Categorical**: Brand, Model, Country, Condition, Modification, Fuel_Type, Drivetrain, Transmission, Popularity, Market_Demand
- **Numerical**: Engine_Size, Horsepower, Torque, Weight, Top_Speed, Acceleration_0_100, Fuel_Efficiency, CO2_Emissions, Price, Mileage, Safety_Rating, Number_of_Owners, Insurance_Cost, Production_Units, Log_Price, Log_Mileage

## 🧹 Data Cleaning

- Fill missing values in `Modification` with 'Unknown'
- Format `Year` using `pd.to_datetime`
- Encode categorical features using `LabelEncoder`

## 🔍 Data Exploration

Visualizations are saved in the `visualize/single/` directory:

- Brand distribution
- Model distribution
- Country distribution
- Year distribution
- Engine_Size distribution
- Condition distribution
- Transmission distribution
- Market_Demand distribution
- Popularity distribution
- Fuel_Type distribution
- Drivetrain distribution
- Horsepower distribution
- Torque distribution
- Weight distribution
- Top_Speed distribution
- Price distribution

## 📈 Correlation

A correlation heatmap is saved in `visualize/correlation/correlation.png`.

![Correlation Heatmap](visualize/correlation/correlation.png)

## 🧠 Model Training

### 📉 Regression

- Linear Regression
- Random Forest Regressor

Visualizations are saved in the `visualize/regression/` directory:

- Linear Regression results
![Linear Regression results](visualize/regression/linear_regression.png)
- Random Forest Regressor results
![Random Forest Regressor results](visualize/regression/random_forest_regressor.png)

### 📊 Classification

- Random Forest Classifier for Popularity
- Random Forest Classifier for Condition

Visualizations are saved in the `visualize/classification/` directory:

- Popularity classification results
![Popularity classification results](visualize/classification/popularity.png)
- Condition classification results
![Condition classification results](visualize/classification/condition.png)

### 🔍 Clustering

- KMeans clustering (implementation in progress)

## How to Run

1. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

2. Run the main script:

    ```sh
    python main.py
    ```

## 📜 License

This project is licensed under the MIT License.
