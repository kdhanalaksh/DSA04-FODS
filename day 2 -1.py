import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame with weather data
# Assuming the DataFrame is already available and named 'weather_data'
# Here's a sample DataFrame creation:
weather_data = pd.DataFrame({
    'Date': pd.date_range(start='2020-01-01', end='2024-12-31', freq='D'),
    'Temperature': np.random.randint(-10, 35, size=1826),  # Random temperature data for 5 years
    'Precipitation': np.random.randint(0, 30, size=1826)    # Random precipitation data for 5 years
})

# Preprocess data if needed (e.g., handle missing values)
# For demonstration, assuming no missing values in this sample data

# Visualize average temperature trends over different seasons
weather_data['Month'] = weather_data['Date'].dt.month
weather_data['Season'] = weather_data['Month'].apply(lambda month: 'Winter' if month in [12, 1, 2]
                                                     else 'Spring' if month in [3, 4, 5]
                                                     else 'Summer' if month in [6, 7, 8]
                                                     else 'Fall')

average_temp_season = weather_data.groupby('Season')['Temperature'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=average_temp_season, x='Season', y='Temperature', palette='coolwarm')
plt.title('Average Temperature Trends Over Different Seasons')
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.show()

# Identify and visualize patterns or anomalies in precipitation
plt.figure(figsize=(10, 6))
sns.lineplot(data=weather_data, x='Date', y='Precipitation')
plt.title('Precipitation Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.show()

# Plot temperature distributions and highlight extreme weather events
plt.figure(figsize=(10, 6))
sns.histplot(weather_data['Temperature'], kde=True, color='skyblue')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.axvline(x=weather_data['Temperature'].mean(), color='red', linestyle='--', label='Mean Temperature')
# You can add more lines or annotations to highlight extreme events
plt.legend()
plt.show()
