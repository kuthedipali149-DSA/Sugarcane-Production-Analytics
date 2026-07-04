import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# STEP 1 - LOAD DATASET
# ==========================================================

df = pd.read_excel("Dataset/WEIGHBRIDGE DATA1.xlsx")

# ==========================================================
# STEP 2 - BASIC DATASET INFORMATION
# ==========================================================

# Uncomment whenever you need them

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

# ==========================================================
# STEP 3 - MISSING VALUE ANALYSIS
# ==========================================================

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

# Uncomment to view missing values
# print(missing)

# Missing value percentage
missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)

# Uncomment to view percentage
# print(pd.DataFrame({
#     "Missing Values": missing,
#     "Percentage": missing_percentage
# }))

# Completely empty columns
empty_cols = df.columns[df.isnull().all()]

# Uncomment if needed
# print("Completely Empty Columns")
# print(list(empty_cols))
# print("Number of completely empty columns:", len(empty_cols))

# ==========================================================
# STEP 4 - REMOVE COLUMNS WITH MORE THAN 95% MISSING VALUES
# ==========================================================

threshold = len(df) * 0.95

df = df.dropna(axis=1, thresh=threshold)

# Uncomment if needed
# print("Shape after dropping columns:", df.shape)

# ==========================================================
# STEP 5 - DUPLICATE CHECK
# ==========================================================

df = df.drop_duplicates()

# Uncomment if needed
# print("Shape after removing duplicates:", df.shape)
# print("Duplicate rows remaining:", df.duplicated().sum())

# ==========================================================
# STEP 6 - DATA TYPES
# ==========================================================

numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

# Uncomment if needed
# print("Number of Numerical Columns:", len(numerical_cols))
# print("Number of Categorical Columns:", len(categorical_cols))

# ==========================================================
# STEP 7 - TARGET VARIABLE ANALYSIS (NET_WT)
# ==========================================================

# Uncomment if needed
# print(df["NET_WT"].describe())

# ==========================================================
# STEP 8 - OUTLIER ANALYSIS
# ==========================================================

Q1 = df["NET_WT"].quantile(0.25)
Q3 = df["NET_WT"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["NET_WT"] < lower_limit) |
    (df["NET_WT"] > upper_limit)
]

# Uncomment if needed
# print("Q1:", Q1)
# print("Q3:", Q3)
# print("IQR:", IQR)
# print("Lower Limit:", lower_limit)
# print("Upper Limit:", upper_limit)
# print("Number of Outliers:", len(outliers))

# Uncomment if needed
# print(outliers[[
#     "DOCUMENT_NO",
#     "VEHICLE_NO",
#     "NET_WT",
#     "GROSS_WT",
#     "EMPTY_WT"
# ]])

# ==========================================================
# STEP 9 - HISTOGRAM
# ==========================================================

# Uncomment when required

# plt.figure(figsize=(8,5))
# plt.hist(df["NET_WT"], bins=30)
# plt.title("Distribution of Net Weight")
# plt.xlabel("Net Weight")
# plt.ylabel("Frequency")
# plt.show()

# ==========================================================
# STEP 10 - BOXPLOT
# ==========================================================

# Uncomment when required

# plt.figure(figsize=(6,4))
# plt.boxplot(df["NET_WT"])
# plt.title("Boxplot of Net Weight")
# plt.show()

# ==========================================================
# STEP 11 - CORRELATION
# ==========================================================

correlation = df[numerical_cols].corr()["NET_WT"].sort_values(ascending=False)

# Uncomment if needed
# print(correlation)

# ==========================================================
# STEP 12 - SINGLE VALUE COLUMNS
# ==========================================================

single_value_cols = [
    col for col in df.columns
    if df[col].nunique() == 1
]

# Uncomment if needed
# print(single_value_cols)
# print("Total:", len(single_value_cols))

df = df.drop(columns=single_value_cols)

# Uncomment if needed
# print("Shape after removing single-value columns:", df.shape)

# ==========================================================
# STEP 13 - SEASON OVERVIEW
# ==========================================================

print("\n==============================")
print("      SEASON OVERVIEW")
print("==============================")

print(f"Total Transactions : {len(df):,}")

print(f"Total Net Weight   : {df['NET_WT'].sum():,.2f}")

print(f"Average Net Weight : {df['NET_WT'].mean():.2f}")

print(f"Total Gross Weight : {df['GROSS_WT'].sum():,.2f}")

print(f"Total Empty Weight : {df['EMPTY_WT'].sum():,.2f}")

print(f"Unique Cultivators : {df['CULTIVATOR_NAME'].nunique()}")

print(f"Unique Harvesters  : {df['HARVEST_NAME'].nunique()}")

print(f"Unique Transporters: {df['TRANSPORTER_NAME'].nunique()}")

print(f"Unique Vehicles    : {df['VEHICLE_NO'].nunique()}")

# ==========================================================
# STEP 14 - TOP 10 HARVESTERS
# ==========================================================

top_harvesters = (
    df.groupby("HARVEST_NAME")["NET_WT"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n==============================")
print("TOP 10 HARVESTERS")
print("==============================")

print(top_harvesters)

# ==========================================================
# STEP 15 - BAR CHART OF TOP HARVESTERS
# ==========================================================

plt.figure(figsize=(12,6))

top_harvesters.plot(kind="bar")

plt.title("Top 10 Harvesters by Total Net Weight")

plt.xlabel("Harvester")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 16 - TOP 10 TRANSPORTERS
# ==========================================================

top_transporters = (
    df.groupby("TRANSPORTER_NAME")["NET_WT"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n==============================")
print("TOP 10 TRANSPORTERS")
print("==============================")

print(top_transporters)

# ==========================================================
# BAR CHART - TOP TRANSPORTERS
# ==========================================================

plt.figure(figsize=(12,6))

top_transporters.plot(kind="bar", color="orange")

plt.title("Top 10 Transporters by Total Net Weight")

plt.xlabel("Transporter")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

top_cultivators = (
    df.groupby("CULTIVATOR_NAME")["NET_WT"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

 # ==========================================================
 # BAR CHART - TOP CULTIVATORS
 # ==========================================================

plt.figure(figsize=(12,6))

top_cultivators.plot(kind="bar", color="green")

plt.title("Top 10 Cultivators by Total Net Weight")

plt.xlabel("Cultivator")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 18 - TOP 10 VILLAGES
# ==========================================================

top_villages = (
    df.groupby("CULTIVATOR_VILLAGE_NAME")["NET_WT"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n==============================")
print("TOP 10 VILLAGES")
print("==============================")

print(top_villages)

plt.figure(figsize=(12,6))

top_villages.plot(kind="bar", color="purple")

plt.title("Top 10 Villages by Total Net Weight")

plt.xlabel("Village")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 19 - CANE VARIETY ANALYSIS
# ==========================================================

top_varieties = (
    df.groupby("CANE_VARIETY_NAME")["NET_WT"]
      .sum()
      .sort_values(ascending=False)
)

print("\n==============================")
print("TOP CANE VARIETIES")
print("==============================")

print(top_varieties)

plt.figure(figsize=(12,6))

top_varieties.head(10).plot(kind="bar", color="brown")

plt.title("Top 10 Cane Varieties")

plt.xlabel("Cane Variety")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 20 - DAILY PRODUCTION
# ==========================================================

daily_production = (
    df.groupby("DOCUMENT_DT")["NET_WT"]
      .sum()
)

print("\n==============================")
print("DAILY PRODUCTION")
print("==============================")

print(daily_production)

plt.figure(figsize=(14,6))

daily_production.plot()

plt.title("Daily Sugarcane Production")

plt.xlabel("Date")

plt.ylabel("Net Weight (Tons)")

plt.tight_layout()

plt.show()