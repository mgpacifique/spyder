# Mars Crater Analysis
### Data Analysis and Interpretation — Wesleyan University via Coursera

> Investigating the association between Impact Crater Diameter and Depth  
> using the **Robbins Global Mars Crater Database** (384,343 craters, complete down to 1 km diameter).

---

## Course Progress

| Week | Topic | Status |
|------|-------|--------|
| 1 | Identifying a Research Question | ✅ Complete |
| 2 | Running Frequency Distributions | ✅ Complete |
| 3 | Univariate Graphs | 🔲 Upcoming |
| 4 | Bivariate Graphs | 🔲 Upcoming |
| 5 | Basic Linear Regression | 🔲 Upcoming |

---

## Week 1 — Research Question

**Research question:** *Are bigger Martian craters proportionally shallower than smaller ones?*

The question sits at the intersection of two topics:
- **Impact physics** — the geometry of craters follows well-established scaling laws (Melosh 1989), predicting that larger impacts produce proportionally shallower bowls.
- **Geological modification** — larger craters have existed longer on average and have had more time to be filled in by aeolian deposition, volcanic resurfacing, and ancient water activity.

**Hypothesis:** There is a positive association between `DIAM_CIRCLE_IMAGE` and `DEPTH_RIMFLOOR_TOPOG`, but the depth-to-diameter ratio *decreases* as diameter increases, indicating that large craters are systematically shallower than the scaling laws alone would predict.

**Variables selected from the Robbins codebook:**

| Variable | Type | Role |
|----------|------|------|
| `DIAM_CIRCLE_IMAGE` | Numeric (km) | Independent — crater size proxy |
| `DEPTH_RIMFLOOR_TOPOG` | Numeric (km) | Dependent — preservation proxy |
| `MORPHOLOGY_EJECTA_1` | Categorical | Context — ejecta preservation |

---

## Week 2 — Frequency Distributions

Full write-up: [`index.html`](index.html)  
Python code: [`mars.py`](mars.py) · [`marscrater.ipynb`](marscrater.ipynb)

### Key findings

**DIAM_CIRCLE_IMAGE (Diameter)**
- No missing data — every crater has a diameter.
- Extreme right-skew: **99.95 %** of craters are under 117 km.
- Two outliers exceed 1,000 km — likely Hellas Planitia and Argyre Planitia.
- Log-transformation will be required before any parametric analysis.

**DEPTH_RIMFLOOR_TOPOG (Depth)**
- **Structural missing data encoded as zero** — depth = 0 does not mean a flat crater, it means the crater was not measured.
- 84.7 % of records fall in the first bin (≤ 0.117 km), dominated by unmeasured craters.
- Working dataset after filtering `depth > 0`: ~76,800 craters.
- Maximum recorded depth: 4.95 km.

**MORPHOLOGY_EJECTA_1 (Ejecta type)**
- Majority of craters have no recorded ejecta morphology (NaN dominant).
- 156 unique labels — most are rare; only "Rd" appears with meaningful frequency (~27,000 craters).
- Variable is only usable on the preserved-crater subset; selection bias is severe across the full dataset.

---

## Dataset

**Robbins, S. J. (2019).** *Mars Global Crater Catalog.* NASA Planetary Data System.  
File: `marscrater_pds.csv` — 384,343 rows × 19 columns (16 MB).

> The catalog is complete for craters ≥ 1 km in diameter and represents the most comprehensive global crater inventory of Mars to date.

---

## Repository Structure

```
spyder/
├── index.html               ← Week 2 blog post (styled, with FA icons)
├── mars.py                 ← Initial Python exploration script
├── marscrater.ipynb        ← Full analysis notebook
├── marscrater_pds.csv      ← Robbins crater database (raw data)
├── images/                 ← Hero + favicon images
└── README.md               ← This file
```

---

## References

- Robbins, S. J. (2011). *Improving Lunar Crater Databases and Impact Chronologies.* University of Colorado.
- Melosh, H. J. (1989). *Impact Cratering: A Geologic Process.* Oxford University Press.
- Le Deit et al. (2013). *Sequence of infilling events in Gale Crater.* Journal of Geophysical Research.

---

*Pacifique Manzi · April 2026 · ALU / Coursera*
