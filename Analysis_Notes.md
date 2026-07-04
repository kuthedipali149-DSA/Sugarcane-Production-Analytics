# Sugarcane Season Analytics Project

## Dataset Information

- Dataset Name: WEIGHBRIDGE DATA1.xlsx
- Total Records: 40,480
- Original Columns: 307

---

# STEP 1 – Load Dataset

## Objective

Load the sugarcane weighbridge dataset into a pandas DataFrame for analysis.

## Code Used

```python
import pandas as pd

df = pd.read_excel("WEIGHBRIDGE DATA1.xlsx")
```

## Learning

- `pd.read_excel()` reads Excel files into a DataFrame.
- A DataFrame is the primary data structure used for analysis in pandas.

---

# STEP 2 – Basic Dataset Understanding

## Objective

Understand the structure of the dataset.

## Functions Used

- `df.head()`
- `df.shape`
- `df.columns`
- `df.info()`
- `df.describe()`

## Learning

These functions help us understand:

- Number of rows and columns
- Column names
- Data types
- Memory usage
- Statistical summary of numerical columns

---

# STEP 3 – Missing Value Analysis

## Objective

Identify missing values in the dataset.

## Code

```python
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
```

## Findings

- Initially, many columns contained missing values.
- 59 columns were completely empty (100% missing).

## Learning

Missing value analysis helps determine:

- Which columns are useful
- Which columns should be removed
- Overall data quality

---

# STEP 4 – Remove Highly Missing Columns

## Objective

Remove columns having more than 95% missing values.

## Code

```python
threshold = len(df) * 0.95

df = df.dropna(axis=1, thresh=threshold)
```

## Result

- Columns reduced from **307** to **248**.

## Learning

Columns with extremely high missing values usually add little value and increase noise.

---

# STEP 5 – Duplicate Analysis

## Objective

Identify and remove duplicate records.

## Code

```python
df = df.drop_duplicates()
```

## Findings

- Duplicate rows found: **0**

## Learning

Duplicate removal avoids biased analysis.

---

# STEP 6 – Data Types

## Objective

Understand numerical and categorical variables.

## Findings

- Numerical Columns: **91**
- Categorical Columns: **124**

## Learning

Numerical columns are used for calculations.

Categorical columns are used for grouping and business analysis.

---

# STEP 7 – Target Variable Analysis

## Objective

Study the distribution of NET_WT.

## Findings

- Count: 40,480
- Mean: 10.97 tons
- Maximum: 44.66 tons

## Learning

The target variable tells us the distribution of sugarcane weight received.

---

# STEP 8 – Outlier Detection

## Objective

Identify abnormal weight records.

## Method

Interquartile Range (IQR)

## Formula

Lower Limit

Q1 − (1.5 × IQR)

Upper Limit

Q3 + (1.5 × IQR)

## Findings

- Outliers Found: **8**

These records had unusually high net weights.

## Learning

Outliers should always be investigated before making business decisions.

---

# STEP 9 – Histogram

## Objective

Visualize the distribution of NET_WT.

## Learning

Histogram helps determine:

- Distribution
- Skewness
- Concentration of observations

---

# STEP 10 – Box Plot

## Objective

Visualize outliers graphically.

## Learning

A box plot shows:

- Median
- Quartiles
- Outliers
- Spread of data

---

# STEP 11 – Correlation Analysis

## Objective

Find variables strongly related to NET_WT.

## Findings

Highest positive correlations:

- NET_WEIGHT_HARVEST
- NET_WEIGHT_TRPT
- CANE_WT
- BINDING_MAT_WT

## Learning

Correlation helps understand relationships between numerical variables.

---

# STEP 12 – Remove Single Value Columns

## Objective

Remove columns containing only one unique value.

## Findings

Single-value columns removed: **38**

## Learning

Columns with only one value provide no useful information for analysis.

---

# STEP 13 – Season Overview

## Objective

Understand the overall scale of the sugarcane season.

## Results

- Total Transactions: **40,480**
- Total Net Weight: **444,241.98 tons**
- Average Net Weight: **10.97 tons**
- Total Gross Weight: **683,493.56 tons**
- Total Empty Weight: **231,751.14 tons**
- Unique Cultivators: **4,517**
- Unique Harvesters: **294**
- Unique Transporters: **301**
- Unique Vehicles: **734**

## Business Insights

- More than **444 thousand tons** of sugarcane were received.
- A total of **40,480** weighbridge transactions occurred.
- **4,517 cultivators** supplied sugarcane.
- **294 harvesters** participated in harvesting.
- **301 transporters** transported sugarcane.
- **734 vehicles** were involved during the season.

## Learning

Season Overview provides high-level KPIs that summarize the entire dataset before detailed business analysis.

---

# STEP 14 – Top Harvesters (In Progress)

## Objective

Identify the harvesters who supplied the highest quantity of sugarcane during the season.

## Method

- Group by `HARVEST_NAME`
- Sum `NET_WT`
- Sort in descending order
- Display the Top 10 harvesters

## Business Value

This analysis helps management identify the highest-performing harvesting contractors and evaluate their contribution to the total sugarcane supply.

# STEP 14 – Top 10 Harvesters

## Objective

Identify the harvesters who supplied the highest quantity of sugarcane.

## Method

Grouped the dataset by HARVEST_NAME and calculated the total NET_WT for each harvester. The results were sorted in descending order and the top 10 harvesters were selected.

## Findings

The highest-performing harvester supplied over 10,342 tons of sugarcane.

Top 10 harvesters were identified based on total sugarcane supplied.

## Business Value

This analysis helps management:

- Identify top-performing harvesting contractors.
- Measure contractor contribution.
- Support future contract decisions.
- Reward high-performing harvesters.

# STEP 16 – Top 10 Transporters

## Objective

Identify the transporters who transported the highest quantity of sugarcane during the season.

## Method

Grouped the dataset by TRANSPORTER_NAME and calculated the total NET_WT transported by each transporter. The results were sorted in descending order and the top 10 transporters were selected.

## Business Value

This analysis helps management:

- Identify high-performing transport contractors.
- Measure transporter contribution.
- Monitor transportation efficiency.
- Support future transportation contract decisions.

# STEP 17 – Top 10 Cultivators

## Objective

Identify the cultivators who supplied the highest quantity of sugarcane during the season.

## Method

Grouped the dataset by CULTIVATOR_NAME and calculated the total NET_WT supplied by each cultivator. The results were sorted in descending order and the top 10 cultivators were selected.

## Business Value

This analysis helps management:

- Identify the highest-producing farmers.
- Reward consistent suppliers.
- Strengthen relationships with key cultivators.
- Plan procurement strategies for future seasons.

# STEP 20 – Daily Production

## Objective

Analyze the total sugarcane received each day during the season.

## Method

Grouped the dataset by DOCUMENT_DT and calculated the total NET_WT for each day.

## Business Value

This analysis helps management:

- Monitor daily production.
- Identify peak and low production days.
- Understand seasonal production trends.
- Support daily operational planning.
# STEP 21 – Monthly Production

## Objective

Analyze sugarcane production month-wise.

## Method

Extracted the month from DOCUMENT_DT and calculated the total NET_WT for each month.

## Business Value

This analysis helps management:

- Compare monthly production.
- Identify the peak production month.
- Support production planning and resource allocation.

# STEP 22 – Shift-wise Production

## Objective

Compare sugarcane production across different working shifts.

## Method

Grouped the dataset by IN_SHIFT_CODE and calculated:
- Total NET_WT
- Number of Transactions
- Average NET_WT

## Business Value

This analysis helps management:

- Compare shift performance.
- Identify the busiest shift.
- Improve manpower planning.
- Optimize factory operations.

Observation:

• Shift C handled the highest total sugarcane production.
• Shift B recorded the maximum number of transactions but had the lowest average load per trip.
• Shift A achieved the highest average load per trip, indicating better loading efficiency.

# STEP 23 – Cane Quality Analysis

## Objective

Analyze sugarcane production based on cane quality.

## Method

Grouped the dataset by CANE_QUALITY_NAME and calculated:

- Total Production
- Number of Transactions
- Average Net Weight

## Business Value

This analysis helps management:

- Identify the most productive cane quality.
- Monitor quality-wise production.
- Support quality improvement programs.
- Guide future cultivation practices.

# STEP 24 – Plantation Area Analysis

## Objective

Analyze whether plantation area influences sugarcane production.

## Method

- Examined descriptive statistics of PLANTATION_AREA.
- Measured correlation with NET_WT.
- Visualized the relationship using a scatter plot.

## Business Value

This analysis helps determine whether larger plantation areas consistently produce more sugarcane and identifies unusually high- or low-performing plantations.

## Plantation Area Data Quality Observation

During analysis, four records were found with a plantation area of 161223.

Investigation showed that:
- All four records belonged to the same cultivator.
- The net weights were within the normal operating range.
- The value is inconsistent with all other plantation areas (1–32).

These records were treated as data entry/system anomalies and excluded only from plantation area analysis. The original dataset was left unchanged.

# STEP 24 – Plantation Area Analysis

## Business Question

Does plantation area influence sugarcane production?

## Key Findings

- Plantation areas between 2 and 5 contributed the majority of total production.
- Larger plantation areas generally delivered higher average net weights per trip.
- Plantation area showed only a weak overall relationship with production, indicating that other agricultural and operational factors also influence yield.
- Four records with a plantation area value of 161223 were identified as data anomalies and excluded only from this analysis.

## Business Recommendation

Focus production planning primarily on medium-sized plantations, as they contribute the largest share of cane supply. For yield improvement, investigate additional factors such as cane variety, cultivation practices, irrigation, and harvesting efficiency rather than relying solely on plantation area.

# STEP 25 – Zone-wise Production Analysis

## Business Question

Which operational zone supplied the highest quantity of sugarcane during the season?

## Objective

Identify the highest and lowest performing operational zones.

## Method

Grouped records by ZONE_NAME and calculated:

- Total Production
- Total Trips
- Average Load per Trip

Created a horizontal bar chart to compare production across zones.

## Business Value

This analysis helps management allocate harvesting teams, transport vehicles, and factory resources more efficiently across operational zones.
# STEP 25 – Zone-wise Production Analysis

## Business Question

Which operational zone supplied the highest quantity of sugarcane during the season?

## Objective

Identify the highest and lowest performing operational zones.

## Method

Grouped records by ZONE_NAME and calculated:

- Total Production
- Total Trips
- Average Load per Trip

Created a horizontal bar chart to compare production across zones.

## Business Value

This analysis helps management allocate harvesting teams, transport vehicles, and factory resources more efficiently across operational zones.

# STEP 25 – Zone-wise Production Analysis

## Business Question

Which operational zone contributes the highest sugarcane production?

## Key Findings

- Factory Zone contributed the highest total production (180,461.43 tons).
- Factory Zone also recorded the highest number of trips (23,368).
- Kalaburagi achieved the highest average load per trip (19.66 tons).
- Factory Zone had the lowest average load (7.72 tons), indicating many small deliveries.

## Business Insights

- The Factory Zone is the primary production area but operates with many smaller loads.
- Kalaburagi and Basavakalyan appear to have more efficient transportation, with significantly higher average loads.
- Comparing total production and average load provides a better understanding of operational efficiency than either metric alone.

## Recommendation

Maintain harvesting capacity in the Factory Zone while studying the operational practices of high-efficiency zones to improve transport utilization and reduce logistics costs.

# STEP 26 – Taluka-wise Production Analysis

## Business Question

Which talukas contribute the highest sugarcane production during the season?

## Objective

Analyze sugarcane production at the taluka level to identify high-performing regions.

## Method

Grouped records by CULTIVATOR_TALUKA_NAME and calculated:

- Total Production
- Total Trips
- Average Load

Created a horizontal bar chart to compare taluka-wise production.

## Business Value

This analysis helps management identify the strongest production regions and supports planning for harvesting operations, farmer engagement, and transportation resources.

# STEP 28 – Distance Range Analysis

## Business Question

Does transport distance influence sugarcane production and average load?

## Objective

Analyze production and transportation efficiency across different transport distance ranges.

## Method

Grouped records by DISTANCE_RANGE and calculated:

- Total Production
- Total Trips
- Average Load

Created bar charts to compare production and average load by distance range.

## Business Value

This analysis helps identify whether transportation distance affects production efficiency and supports planning for vehicle allocation and transport optimization.

# STEP 28 – Distance Range Analysis

## Business Question

Does transport distance influence sugarcane production and average load?

## Objective

Analyze production and transportation efficiency across different transport distance ranges.

## Method

Grouped records by DISTANCE_RANGE and calculated:

- Total Production
- Total Trips
- Average Load

Created bar charts to compare production and average load by distance range.

## Business Value

This analysis helps identify whether transportation distance affects production efficiency and supports planning for vehicle allocation and transport optimization.

# STEP 28 – Distance Range Analysis

## Business Question

Does transport distance influence sugarcane production and transportation efficiency?

## Key Findings

- Most sugarcane production originated from farms located 11–30 km from the factory.
- The 16–20 km range contributed the highest total production.
- Average load generally increased with transport distance.
- The 6–10 km range showed an unusually low average load (2.71 tons), indicating possible operational differences or smaller vehicle usage.
- Distance ranges with very few trips showed high average loads but require cautious interpretation due to the small sample size.

## Business Recommendation

Focus transport planning on the 11–30 km range, as it contributes the largest share of production. Review transport operations in the 6–10 km range to determine whether vehicle utilization or delivery scheduling can be improved.
