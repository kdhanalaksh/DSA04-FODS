import pandas as pd
import numpy as np
from scipy.stats import t

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("DAY4_5.csv")

# Specify the product category you're interested in
product_category = "Your desired product category"

# Check data types
print(df['reviews_rating'].dtype)

# Inspect data for the specified product category
print(df[df['categories'] == product_category])

# Verify filtering
category_reviews = df[df['categories'] == product_category]['reviews_rating']
print("Number of reviews for the specified category:", len(category_reviews))

# Calculate sample statistics
sample_mean = category_reviews.mean()
sample_std = category_reviews.std()
n = len(category_reviews)

# Specify the desired confidence level
confidence_level = 0.95

# Calculate the critical value from the t-distribution
critical_value = t.ppf((1 + confidence_level) / 2, n - 1)

# Calculate the standard error of the mean
standard_error = sample_std / np.sqrt(n)

# Calculate the margin of error
margin_of_error = critical_value * standard_error

# Calculate the lower and upper bounds of the confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Print or display the confidence interval
print("Confidence Interval for Population Mean Rating ({}%):".format(int(confidence_level * 100)))
print("Lower Bound: {:.2f}".format(lower_bound))
print("Upper Bound: {:.2f}".format(upper_bound))
