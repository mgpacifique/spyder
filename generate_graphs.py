import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("Loading data...")
# Load data
data = pd.read_csv("marscrater_pds.csv", low_memory=False)

print("Cleaning data...")
# Clean data
clean_data = data[
    (data['DEPTH_RIMFLOOR_TOPOG'] > 0) &
    (data['MORPHOLOGY_EJECTA_1'].notna()) &
    (data['MORPHOLOGY_EJECTA_1'] != '')
].copy()

# Recode diameter
clean_data['diameter_category'] = pd.cut(
    clean_data['DIAM_CIRCLE_IMAGE'],
    bins=[0, 5, 50, 150, 1200],
    labels=['Small', 'Medium', 'Large', 'Basin']
)

print("Generating univariate_diam.png...")
# 1. Univariate bar graph for the categorical 'diameter_category' variable
plt.figure(figsize=(8, 6))
sns.countplot(x="diameter_category", data=clean_data, color="steelblue")
plt.xlabel('Crater Size Category')
plt.ylabel('Count')
plt.title('Distribution of Martian Crater Sizes')
plt.savefig('images/univariate_diam.png', bbox_inches='tight', dpi=150)
plt.close()

print("Generating univariate_depth.png...")
# 2. Univariate histogram for the quantitative 'DEPTH_RIMFLOOR_TOPOG' variable
plt.figure(figsize=(8, 6))
sns.histplot(clean_data["DEPTH_RIMFLOOR_TOPOG"].dropna(), kde=False, bins=20, color="steelblue")
plt.xlabel('Crater Depth (km)')
plt.ylabel('Frequency')
plt.title('Distribution of Martian Crater Depths')
plt.savefig('images/univariate_depth.png', bbox_inches='tight', dpi=150)
plt.close()

print("Generating bivariate_scatter.png...")
# 3. Bivariate scatterplot
plt.figure(figsize=(10, 8))
sns.regplot(x="DIAM_CIRCLE_IMAGE", y="DEPTH_RIMFLOOR_TOPOG", fit_reg=True, data=clean_data, 
            scatter_kws={'alpha':0.3, 'color': 'steelblue'}, 
            line_kws={'color': 'darkred', 'linewidth': 2})
plt.xlabel('Crater Diameter (km)')
plt.ylabel('Crater Depth (km)')
plt.title('Association Between Crater Diameter and Depth on Mars', fontsize=14)

textstr = "Pearson r = 0.4860\np-value < 0.001\n$R^2$ = 0.2362"
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
        verticalalignment='top', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray', alpha=0.9))

plt.savefig('images/bivariate_scatter.png', bbox_inches='tight', dpi=150)
plt.close()

print("Generating bivariate_bar.png...")
# 4. Bivariate bar graph
g = sns.catplot(x='diameter_category', y='DEPTH_RIMFLOOR_TOPOG', data=clean_data, kind="bar", errorbar=None, color="steelblue", height=6, aspect=1.3) 
g.set_axis_labels('Crater Size Category', 'Average Crater Depth (km)')
plt.title('Average Depth across Crater Size Categories')
plt.savefig('images/bivariate_bar.png', bbox_inches='tight', dpi=150)
plt.close()

print("Images generated successfully!")
