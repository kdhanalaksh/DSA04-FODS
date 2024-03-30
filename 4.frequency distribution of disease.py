disease_data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}
total_patients = sum(disease_data['DIAGNOSED_PATIENTS'])
frequency = {disease: patients / total_patients for disease, patients in zip(disease_data['DISEASE_NAME'], disease_data['DIAGNOSED_PATIENTS'])}
most_common = max(frequency, key=frequency.get)
print("Frequency Distribution of Diseases:")
for disease, patients in frequency.items():
    print(f"{disease}: {patients * 100:.2f}% of diagnosed patients")

print("\nThe most common disease is:", most_common)
