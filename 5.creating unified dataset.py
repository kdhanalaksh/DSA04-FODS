import pandas as pd
import numpy as np
num_customers = 1000
customer_demographics = pd.DataFrame({
    'customer_id': range(1, num_customers + 1),
    'age': np.random.randint(18, 70, num_customers),
    'gender': np.random.choice(['Male', 'Female'], num_customers),
    'location': np.random.choice(['City', 'Suburb', 'Rural'], num_customers)
})
user_activity_logs = pd.DataFrame({
    'customer_id': np.random.randint(1, num_customers + 1, num_customers * 10),
    'timestamp': pd.date_range(start='2022-01-01', end='2022-01-31', periods=num_customers * 10),
    'page_views': np.random.randint(1, 100, num_customers * 10),
    'interaction_duration': np.random.randint(1, 300, num_customers * 10)
})
customer_support = pd.DataFrame({
    'customer_id': np.random.randint(1, num_customers + 1, num_customers // 10),
    'support_tickets': np.random.randint(1, 5, num_customers // 10),
    'satisfaction_score': np.random.randint(1, 6, num_customers // 10)
})

# Merge datasets on 'customer_id'
merged_data = pd.merge(customer_demographics, user_activity_logs, on='customer_id', how='left')
merged_data = pd.merge(merged_data, customer_support, on='customer_id', how='left')

# Clean the merged dataset (handle missing values, outliers, etc.)
# For simplicity, let's assume that no significant cleaning is required for this example.

# Explore the data
print("Unified Dataset Information:")
print(merged_data.info())
print("\nUnified Dataset Descriptive Statistics:")
print(merged_data.describe())

# Exclude non-numeric columns for correlation analysis
numeric_columns = merged_data.select_dtypes(include=[np.number]).columns
numeric_data = merged_data[numeric_columns]

# Analyze factors influencing customer satisfaction
correlation_matrix = numeric_data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# You can further analyze and visualize the data to identify key factors influencing customer satisfaction.



