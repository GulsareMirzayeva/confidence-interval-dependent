"""
Problem (EN):
We want to calculate the 95% confidence interval for the mean difference in paired samples (before/after weights) 
to see if a weight loss program was statistically effective.

Solution:
- Read Excel file
- Compute differences (Before - After)
- Calculate mean, standard deviation, standard error
- Use t-distribution to find critical value
- Build confidence interval and interpret result

Nəticə və öyrəndiklərim:
- Paired samples üçün fərq üzərində hesablama apardım
- t-paylanması və standart səhv anlayışlarını tətbiq etdim
"""


import pandas as pd
import numpy as np
from scipy import stats

# Read Excel file
df = pd.read_excel("data/weight_data.xlsx", engine='openpyxl', skiprows=13, usecols="B:E", header=0)
# print(df.head())

# Calculate the difference (before-after)
# print(df.columns.tolist())
df.rename(columns={
    "Weight before (lbs)": "Before",
    "Weight after (lbs)": "After"
}, inplace=True)

df["Difference"] = df["Before"] - df["After"]

# Compute sample statistics
mean_diff = df["Difference"].mean()
std_diff = df["Difference"].std(ddof=1)
n = len(df)

# print(mean_diff)
# print(std_diff)

# Compute t-critical value for 95% confidence 
# PPF - Percent point function
t_crit = stats.t.ppf(1 - 0.05 / 2, df=n-1)

# Compute standard error of the mean difference
std_error = std_diff / np.sqrt(n)

# Calculate confidence interval
lower = mean_diff - t_crit * std_error
upper = mean_diff + t_crit * std_error

# Output results
print(f"Mean difference: {mean_diff:.2f}")
print(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]")

# Result interpretation
# The average weight loss was 20.02 lbs.
# We are 95% confident that the true mean weight loss lies between 15.12 lbs and 24.93 lbs.
# Since the interval does not contain 0, the program had a statistically significant effect.
