#
# Linh, 2025/10/22
# file: Linh_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy

# 1. Input
df = pd.read_csv("Correlataion_Analysis_Data.csv")

# 2. Process
# print(df.isnull().sum())
# corre, pvalue = stats.pearsonr(df['Marketing_Spend'],df['Sales_Revenue'])
# df[''].corr()

corr_matrix = df.iloc[:,1:6].corr()
print(corr_matrix.round(3))


# print(df.isnull().sum().sum())
# 3. Output
# print("Data loaded successfully")
# print(f"Data shape: {df.shape}")
# print(f"Corre: {corre:,.4f}")
# print(f"pvalue: {pvalue:.4e}")

print(sns.heatmap(corr_matrix))
plt.title("Linh is smart")
plt.tight_layout()
plt.show()