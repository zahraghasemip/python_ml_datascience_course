import pandas as pd

# Create a sample DataFrame with car data
data = {
    'Manufacturer': ['Toyota', 'Ford', 'Toyota', 'Ford', 'BMW', 'BMW'],
    'Model': ['Corolla', 'F-150', 'Camry', 'Mustang', 'X5', '3 Series'],
    'Year': [2020, 2019, 2021, 2018, 2020, 2021],
    'Horsepower': [132, 290, 203, 450, 335, 255],
    'MPG': [30, 20, 28, 15, 21, 26],
    'Price': [20000, 30000, 24000, 45000, 60000, 42000]
}

cars = pd.DataFrame(data)

# Display the columns of the DataFrame
print("Columns in the 'cars' DataFrame:")
print(cars.columns)

# Display the first few rows of the DataFrame
print("\nFirst 5 rows of the 'cars' DataFrame:")
print(cars.head())

# Group the data by 'Manufacturer'
cars_groups = cars.groupby('Manufacturer')

# Calculate the mean of the numeric columns within each group
cars_grouped_mean = cars_groups.mean(numeric_only=True)

# Display the grouped mean data
print("\nMean of numeric columns for each group:")
print(cars_grouped_mean)