import pandas as pd


file_path = "data/experiment_02-selected-columns.csv"
data = pd.read_csv(file_path)

print("Original dataset shape:", data.shape)

data = data.drop_duplicates()


print("\nMissing values:")
print(data.isnull().sum())

data = data.fillna(data.median(numeric_only=True))


output_file = "data/cleaned_cnc_data.csv"
data.to_csv(output_file, index=False)

print("\nPreprocessing completed!")
print("Cleaned dataset shape:", data.shape)
print("Saved as:", output_file)