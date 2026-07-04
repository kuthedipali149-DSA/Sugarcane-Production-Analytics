# 🌾 Sugarcane Production Analytics – Season 14

## 📌 Project Overview

This project analyzes sugarcane weighbridge transaction data collected during Season 14. The objective is to identify production trends, operational performance, geographical patterns, and key business insights that can help improve sugar factory operations.

The project was developed using Python for data analysis and visualization.

---

# 🎯 Objectives

- Analyze seasonal sugarcane production.
- Measure harvesting and transportation performance.
- Study production across zones, villages, and talukas.
- Identify production patterns and operational trends.
- Detect data outliers and relationships between variables.
- Build an Executive Dashboard for management reporting.

---

# 📂 Dataset

The dataset contains **40,480 sugarcane transactions** with **248 columns**.

Major attributes include:

- Net Weight
- Gross Weight
- Empty Weight
- Cultivator
- Harvester
- Transporter
- Vehicle
- Village
- Taluka
- Zone
- Plantation Area
- Cane Variety
- Cane Quality
- Shift Information
- Distance Range
- Dates

---

# 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 📊 Analyses Performed

## 1. Season KPI Overview

- Total Transactions
- Total Production
- Average Net Weight
- Total Gross Weight
- Total Empty Weight
- Unique Cultivators
- Unique Harvesters
- Unique Transporters
- Unique Vehicles

---

## 2. Monthly Production Analysis

- Monthly production trend
- Seasonal production comparison

---

## 3. Daily Production Analysis

- Daily production variation

---

## 4. Shift-wise Production Analysis

- Production by operational shift
- Average production per shift

---

## 5. Harvester Analysis

- Top harvesters by production
- Production contribution

---

## 6. Transporter Analysis

- Top transporters by production

---

## 7. Cultivator Analysis

- Top cultivators by production

---

## 8. Cane Quality Analysis

- Production by cane quality

---

## 9. Cane Variety Analysis

- Production by cane variety

---

## 10. Plantation Area Analysis

- Production by plantation size
- Plantation size distribution

---

## 11. Zone Analysis

- Zone-wise production
- Average production
- Total trips

---

## 12. Taluka Analysis

- Taluka-wise production

---

## 13. Village Analysis

- Village-wise production

---

## 14. Distance Range Analysis

- Production across transport distance ranges

---

## 15. Correlation Analysis

- Feature correlation heatmap
- Top correlations with Net Weight

---

## 16. Outlier Detection

- Identification of abnormal production records

---

## 17. Executive Dashboard

Management summary including:

- Overall KPIs
- Best performing zone
- Top harvester
- Top cultivator
- Most productive shift
- Best plantation area

---

# 📈 Key Findings

- Over **444,000 tons** of sugarcane were analyzed.
- Factory Zone contributed the highest production.
- Production was concentrated within medium plantation sizes.
- Harvester performance varied significantly.
- Production differed across operational shifts.
- Transport distance influenced production patterns.
- A few cultivators contributed a major share of seasonal production.
- Outliers were detected and identified for further validation.

---

# 💼 Business Recommendations

- Allocate additional harvesting resources to high-producing zones.
- Monitor low-performing regions for operational improvements.
- Review unusually high-weight transactions.
- Encourage cultivation practices associated with higher production.
- Use dashboard reporting for continuous seasonal monitoring.

---

# 📁 Project Structure

```
Analytics_Season_14
│
├── analysis.py
├── README.md
├── Analysis_Notes.md
├── Business_Insights.md
├── Business_Recommendations.md
├── requirements.txt
│
├── Dataset
│
├── Charts
│   ├── 01_Season_KPI_Overview.png
│   ├── 02_Monthly_Production.png
│   ├── 03_Daily_Production.png
│   ├── 04_Shift_Wise_Production.png
│   ├── ...
│
└── Report
```

---

# ▶️ How to Run

1. Clone or download the project.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Place the dataset inside the project folder.

4. Run:

```bash
python analysis.py
```

---

# 👨‍💻 Author

**Dipali Kuthe**

Data Analytics & Machine Learning Project

Season 14 Sugarcane Production Analysis