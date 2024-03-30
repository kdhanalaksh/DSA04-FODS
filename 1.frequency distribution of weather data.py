weather_data = [
    'sunny', 'rainy', 'sunny', 'sunny', 'cloudy',
    'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy',
    'rainy', 'rainy', 'sunny', 'sunny', 'rainy'
]
frequency = {}
for weather in weather_data:
    frequency[weather] = frequency.get(weather, 0) + 1
most_common = max(frequency, key=frequency.get)
print("Frequency Distribution of Weather Conditions:")
for weather, count in frequency.items():
    print(f"{weather}: {count} occurrences")
print("\nThe most common weather type is:", most_common)
