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

top_corr = (
    df.select_dtypes(include='number')
      .corr()['NET_WT']
      .abs()
      .sort_values(ascending=False)
      .head(15)
)

top_corr.plot(kind='barh')
plt.savefig(
    "Charts/06_Top_NET_WT_Correlations.png",
    dpi=300,
    bbox_inches="tight"
)
plt.title("Top Variables Correlated with NET_WT")
plt.tight_layout()
plt.show()

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

plt.figure(figsize=(10, 6))
plt.axis('off')

kpi_text = f"""
SUGARCANE SEASON 14 OVERVIEW

Total Transactions : {len(df):,}

Total Net Weight   : {df['NET_WT'].sum():,.2f} Tons

Average Net Weight : {df['NET_WT'].mean():.2f} Tons

Total Gross Weight : {df['GROSS_WT'].sum():,.2f} Tons

Total Empty Weight : {df['EMPTY_WT'].sum():,.2f} Tons

Unique Cultivators : {df['CULTIVATOR_ID'].nunique()}

Unique Harvesters  : {df['HARVEST_ID'].nunique()}

Unique Transporters: {df['TRANSPORTER_ID'].nunique()}

Unique Vehicles    : {df['VEHICLE_NO'].nunique()}
"""

plt.text(
    0.02,
    0.98,
    kpi_text,
    fontsize=14,
    va="top",
    family="monospace"
)

plt.title("Season KPI Overview", fontsize=18, weight="bold")

plt.savefig("Charts/01_Season_KPI_Overview.png", dpi=300, bbox_inches="tight")

plt.show()

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

# ==========================================================
# STEP 21 - MONTHLY PRODUCTION
# ==========================================================

df["MONTH"] = df["DOCUMENT_DT"].dt.month_name()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_production = (
    df.groupby("MONTH")["NET_WT"]
      .sum()
      .reindex(month_order)
      .dropna()
)

monthly_production = (
    df.groupby("MONTH")["NET_WT"]
      .sum()
)

print("\n==============================")
print("MONTHLY PRODUCTION")
print("==============================")

print(monthly_production)

plt.figure(figsize=(10,5))

monthly_production.plot(kind="bar", color="teal")

plt.title("Monthly Sugarcane Production")

plt.xlabel("Month")

plt.ylabel("Net Weight (Tons)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 22 - SHIFT WISE PRODUCTION
# ==========================================================

shift_summary = (
    df.groupby("IN_SHIFT_CODE")
      .agg(
          Total_Production=("NET_WT", "sum"),
          Total_Trips=("DOCUMENT_NO", "count"),
          Average_Load=("NET_WT", "mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print("\n==============================")
print("SHIFT WISE PRODUCTION")
print("==============================")

print(shift_summary)

plt.figure(figsize=(8,5))

shift_summary["Total_Production"].plot(
    kind="bar",
    color="steelblue"
)

plt.title("Shift-wise Sugarcane Production")

plt.xlabel("Shift")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "Charts/04.1Shift_Wise_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# STEP 23 - CANE QUALITY ANALYSIS
# ==========================================================

quality_analysis = (
    df.groupby("CANE_QUALITY_NAME")["NET_WT"]
      .agg(["sum", "count", "mean"])
      .sort_values(by="sum", ascending=False)
)

print("\n==============================")
print("CANE QUALITY ANALYSIS")
print("==============================")

plt.figure(figsize=(12,6))

quality_analysis["sum"].plot(
    kind="barh",
    color="darkorange"
)

plt.title("Sugarcane Production by Cane Quality")

plt.xlabel("Total Net Weight (Tons)")
plt.ylabel("Cane Quality")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 24 - PLANTATION AREA ANALYSIS
# ==========================================================

print("\n==============================")
print("PLANTATION AREA ANALYSIS")
print("==============================")

# Summary Statistics
print(df["PLANTATION_AREA"].describe())

print("\nNumber of Unique Plantation Areas:")
print(df["PLANTATION_AREA"].nunique())

print("\nTop 20 Plantation Area Values:")
print(df["PLANTATION_AREA"].value_counts().head(20))

# Check abnormal values
print("\nRecords with Plantation Area > 100")

print(
    df[df["PLANTATION_AREA"] > 100][
        [
            "DOCUMENT_NO",
            "CULTIVATOR_NAME",
            "PLANTATION_AREA",
            "NET_WT",
            "CANE_VARIETY_NAME",
            "CULTIVATOR_VILLAGE_NAME"
        ]
    ]
)

# Create filtered dataset for analysis
plantation_df = df[df["PLANTATION_AREA"] < 100].copy()

# Correlation
print("\nCorrelation with NET_WT")

print(
    plantation_df[
        ["PLANTATION_AREA", "NET_WT"]
    ].corr()
)

# Scatter Plot
plt.figure(figsize=(10,6))

plt.scatter(
    plantation_df["PLANTATION_AREA"],
    plantation_df["NET_WT"],
    alpha=0.4
)

plt.title("Plantation Area vs Net Weight")

plt.xlabel("Plantation Area")

plt.ylabel("Net Weight (Tons)")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Charts/08_Plantation_Area_vs_Net_Weight.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Plantation Summary
plantation_summary = (
    plantation_df.groupby("PLANTATION_AREA")
    .agg(
        Total_Production=("NET_WT", "sum"),
        Average_Load=("NET_WT", "mean"),
        Total_Trips=("DOCUMENT_NO", "count")
    )
    .sort_index()
)

print("\nPlantation Area Summary")

print(plantation_summary)
# ==========================================================
# STEP 25 - ZONE WISE PRODUCTION
# ==========================================================

zone_summary = (
    df.groupby("ZONE_NAME")
      .agg(
          Total_Production=("NET_WT", "sum"),
          Total_Trips=("DOCUMENT_NO", "count"),
          Average_Load=("NET_WT", "mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print("\n==============================")
print("ZONE WISE PRODUCTION")
print("==============================")

print(zone_summary)

plt.figure(figsize=(12,6))

zone_summary["Total_Production"].plot(
    kind="barh",
    color="steelblue"
)

plt.title("Zone-wise Sugarcane Production")

plt.xlabel("Total Net Weight (Tons)")

plt.ylabel("Zone")

plt.tight_layout()

plt.savefig(
    "Charts/09_Zone_Wise_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nHighest Average Load Zone")

print(
    zone_summary.sort_values(
        "Average_Load",
        ascending=False
    ).head(5)
)

print(df["CULTIVATOR_TALUKA_NAME"].value_counts())

# ==========================================================
# STEP 26 - TALUKA WISE PRODUCTION
# ==========================================================

taluka_summary = (
    df.groupby("CULTIVATOR_TALUKA_NAME")
      .agg(
          Total_Production=("NET_WT", "sum"),
          Total_Trips=("DOCUMENT_NO", "count"),
          Average_Load=("NET_WT", "mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print("\n==============================")
print("TALUKA WISE PRODUCTION")
print("==============================")

print(taluka_summary)

plt.figure(figsize=(12,8))

taluka_summary["Total_Production"].plot(
    kind="barh",
    color="darkgreen"
)

plt.title("Taluka-wise Sugarcane Production")

plt.xlabel("Total Net Weight (Tons)")
plt.ylabel("Taluka")

plt.tight_layout()
plt.savefig(
    "Charts/10_Taluka_Wise_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTop 5 Talukas by Average Load")

print(
    taluka_summary.sort_values(
        "Average_Load",
        ascending=False
    ).head(5)
)

print(df["CULTIVATOR_VILLAGE_NAME"].value_counts().head(20))

# ==========================================================
# STEP 27 - VILLAGE WISE PRODUCTION
# ==========================================================

village_summary = (
    df.groupby("CULTIVATOR_VILLAGE_NAME")
      .agg(
          Total_Production=("NET_WT", "sum"),
          Total_Trips=("DOCUMENT_NO", "count"),
          Average_Load=("NET_WT", "mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print("\n==============================")
print("TOP 20 VILLAGES")
print("==============================")

print(village_summary.head(20))

top10_village = village_summary.head(10)

plt.figure(figsize=(12,6))

top10_village["Total_Production"].sort_values().plot(
    kind="barh",
    color="forestgreen"
)

plt.title("Top 10 Villages by Sugarcane Production")

plt.xlabel("Total Net Weight (Tons)")
plt.ylabel("Village")

plt.tight_layout()
plt.savefig(
    "Charts/11_Top10_Village_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

efficient_villages = village_summary[
    village_summary["Total_Trips"] >= 50
]

print("\nTop 10 Efficient Villages")

print(
    efficient_villages
    .sort_values("Average_Load", ascending=False)
    .head(10)
)
print(df["DISTANCE_RANGE"].value_counts())

# ==========================================================
# STEP 28 - DISTANCE RANGE ANALYSIS
# ==========================================================

distance_summary = (
    df.groupby("DISTANCE_RANGE")
      .agg(
          Total_Production=("NET_WT", "sum"),
          Total_Trips=("DOCUMENT_NO", "count"),
          Average_Load=("NET_WT", "mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print("\n==============================")
print("DISTANCE RANGE ANALYSIS")
print("==============================")

print(distance_summary)

plt.figure(figsize=(12,6))

distance_summary["Total_Production"].plot(
    kind="bar",
    color="royalblue"
)

plt.title("Production by Distance Range")

plt.xlabel("Distance Range")

plt.ylabel("Total Net Weight (Tons)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Charts/19_Distance_Range_Analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.figure(figsize=(12,6))

distance_summary["Average_Load"].plot(
    kind="bar",
    color="darkgreen"
)

plt.title("Average Load by Distance Range")

plt.xlabel("Distance Range")

plt.ylabel("Average Net Weight (Tons)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Charts/18_Distance_Range_Average_Load.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(df["CANE_TYPE_NAME"].value_counts())
cane_type_summary = (
    df.groupby("CANE_TYPE_NAME")
      .agg(
          Total_Production=("NET_WT","sum"),
          Total_Trips=("DOCUMENT_NO","count"),
          Average_Load=("NET_WT","mean")
      )
      .sort_values("Total_Production", ascending=False)
)

print(cane_type_summary)

plt.figure(figsize=(8,5))

cane_type_summary["Total_Production"].plot(
    kind="bar",
    color=["forestgreen","goldenrod","tomato"]
)

plt.title("Production by Cane Type")
plt.xlabel("Cane Type")
plt.ylabel("Total Production (Tons)")

plt.tight_layout()

plt.savefig(
    "Charts/18_Cane_Type_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(df["PLANTATION_TYPE"].value_counts(dropna=False))


# ==========================================================
# STEP 30 - EXECUTIVE BUSINESS DASHBOARD
# ==========================================================

print("\n")
print("=" * 60)
print("             EXECUTIVE BUSINESS DASHBOARD")
print("=" * 60)

# Overall KPIs
print(f"Season Transactions      : {len(df):,}")
print(f"Total Production (Tons)  : {df['NET_WT'].sum():,.2f}")
print(f"Average Load (Tons)      : {df['NET_WT'].mean():.2f}")

print(f"\nUnique Cultivators       : {df['CULTIVATOR_NAME'].nunique():,}")
print(f"Unique Harvesters        : {df['HARVEST_NAME'].nunique():,}")
print(f"Unique Transporters      : {df['TRANSPORTER_NAME'].nunique():,}")
print(f"Unique Vehicles          : {df['VEHICLE_NO'].nunique():,}")

print("\n" + "-" * 60)

# -----------------------------
# Top Zone
# -----------------------------
top_zone = zone_summary["Total_Production"].idxmax()
top_zone_prod = zone_summary.loc[top_zone, "Total_Production"]

print(f"Top Zone                 : {top_zone}")
print(f"Zone Production          : {top_zone_prod:,.2f} Tons")

print()

# -----------------------------
# Top Harvester
# -----------------------------
top_harvester = top_harvesters.index[0]
top_harvester_prod = top_harvesters.iloc[0]

print(f"Top Harvester            : {top_harvester}")
print(f"Production               : {top_harvester_prod:,.2f} Tons")

print()

# -----------------------------
# Top Cultivator
# -----------------------------
top_cultivator = top_cultivators.index[0]
top_cultivator_prod = top_cultivators.iloc[0]

print(f"Top Cultivator           : {top_cultivator}")
print(f"Production               : {top_cultivator_prod:,.2f} Tons")

print()

# -----------------------------
# Most Productive Shift
# -----------------------------
best_shift = shift_summary["Total_Production"].idxmax()
best_shift_prod = shift_summary.loc[best_shift, "Total_Production"]

print(f"Most Productive Shift    : {best_shift}")
print(f"Shift Production         : {best_shift_prod:,.2f} Tons")

print()

# -----------------------------
# Best Plantation Area
# -----------------------------
best_area = plantation_summary["Total_Production"].idxmax()
best_area_prod = plantation_summary.loc[best_area, "Total_Production"]

print(f"Best Plantation Area     : {best_area} Acres")
print(f"Area Production          : {best_area_prod:,.2f} Tons")

print("=" * 60)
