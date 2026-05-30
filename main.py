import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/household_power_consumption.csv")
df["Global_active_power"] = pd.to_numeric(
    df["Global_active_power"],
    errors="coerce"
)
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean data
df_clean = df.dropna()

print("\nOriginal Shape:", df.shape)
print("Cleaned Shape:", df_clean.shape)

# First graph
plt.figure(figsize=(10,5))
plt.plot(df_clean["Global_active_power"].head(1000))

plt.title("Global Active Power Consumption")
plt.xlabel("Sample Number")
plt.ylabel("Power (kW)")

plt.savefig("figures/power_consumption.png")
plt.show()

# Second graph
plt.figure(figsize=(8,5))

df_clean["Global_active_power"].hist(bins=50)

plt.title("Distribution of Global Active Power")
plt.xlabel("Power (kW)")
plt.ylabel("Frequency")

plt.savefig("figures/power_distribution.png")
plt.show()