# Mars Crater Analysis

### Data Analysis and Interpretation Specialization — Wesleyan University via Coursera

> Investigating the association between Impact Crater Diameter and Depth  
> using the **Robbins Global Mars Crater Database** (384,343 craters, complete down to 1 km diameter).

🌐 **[Read the Full Research Blog Here](https://mgpacifique.github.io/marscrater_analysis/)**

---

## 🏆 Course Progress

### Course 1: Data Management and Visualization
**Status:** ✅ Completed | **Grade:** 96.87% (Certificate Earned 🎓)

| Assignment | Topic | Status | Blog Link |
|------------|-------|--------|-----------|
| Week 1 | Identifying a Research Question | ✅ Complete | [Introduction](https://mgpacifique.github.io/marscrater_analysis/index.html) |
| Week 2 | Data Management & Frequency Distributions | ✅ Complete | [Part 1 & 2](https://mgpacifique.github.io/marscrater_analysis/frequency_distribution.html) |
| Week 3 | Univariate Graphs | ✅ Complete | [Part 3](https://mgpacifique.github.io/marscrater_analysis/visualization.html) |
| Week 4 | Bivariate Graphs | ✅ Complete | [Part 3](https://mgpacifique.github.io/marscrater_analysis/visualization.html) |

### Course 2: Data Analysis Tools
**Status:** 🔄 In Progress

| Assignment | Topic | Status | Blog Link |
|------------|-------|--------|-----------|
| Week 1 | Hypothesis Testing (ANOVA) | ✅ Complete | [Part 4](https://mgpacifique.github.io/marscrater_analysis/anova.html) |
| Week 2 | Chi-Square Test of Independence | ✅ Complete | [Part 5](https://mgpacifique.github.io/marscrater_analysis/chi_square.html) |
| Week 3 | Pearson Correlation | ✅ Complete | [Part 6](https://mgpacifique.github.io/marscrater_analysis/pearson_correlation.html) |
| Week 4 | Exploring Statistical Interactions | 🔲 Upcoming | |

---

## Research Question & Hypothesis

**Research question:** *Are bigger Martian craters proportionally shallower than smaller ones?*

The question sits at the intersection of two topics:
- **Impact physics** — the geometry of craters follows well-established scaling laws (Melosh 1989), predicting that larger impacts produce proportionally shallower bowls.
- **Geological modification** — larger craters have existed longer on average and have had more time to be filled in by aeolian deposition, volcanic resurfacing, and ancient water activity.

**Hypothesis:** 
*Crater diameter (`DIAM_CIRCLE_IMAGE`) will be positively but sub-linearly associated with crater depth (`DEPTH_RIMFLOOR_TOPOG`) in the Robbins Mars crater database, such that larger craters are proportionally shallower than smaller craters. The depth-diameter scaling exponent derived from the full dataset will be lower than the 0.538 benchmark established by Tornabene et al. (2017) for best-preserved craters, reflecting the cumulative effect of billions of years of aeolian infilling, fluvial sedimentation, and volcanic resurfacing that preferentially reduces the measurable depth of larger, older craters.*

---

## Variables

**Variables selected from the Robbins codebook:**

| Variable | Type | Role |
|----------|------|------|
| `DIAM_CIRCLE_IMAGE` | Numeric (km) | Independent — crater size proxy |
| `DEPTH_RIMFLOOR_TOPOG` | Numeric (km) | Dependent — preservation proxy |
| `MORPHOLOGY_EJECTA_1` | Categorical | Context — ejecta preservation |

---

## Repository Structure

```text
spyder/
├── index.html                     ← Introduction & Literature Review
├── frequency_distribution.html    ← Part 1: Frequency Distributions
├── data_management.html           ← Part 2: Data Management
├── visualization.html             ← Part 3: Univariate & Bivariate Graphs
├── anova.html                     ← Part 4: ANOVA & Hypothesis Testing
├── chi_square.html                ← Part 5: Chi-Square Test of Independence
├── pearson_correlation.html       ← Part 6: Pearson Correlation
├── mars.py                        ← Initial Python exploration script
├── marscrater.ipynb               ← Full analysis notebook
├── generate_graphs.py             ← Script for generating Matplotlib visualizations
├── marscrater_pds.csv             ← Robbins crater database (raw data)
├── images/                        ← Hero + favicon images
└── README.md                      ← This file
```

---

*Pacifique Manzi · April 2026 · ALU / Coursera*
