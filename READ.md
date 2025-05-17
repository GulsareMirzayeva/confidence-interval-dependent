# 📊 Confidence Interval for Paired Samples (Weight Loss Case Study)

## 🧩 Problem

The 365 team designed a 12-week weight loss program. We are given before-and-after weight data for 10 individuals.  
Our goal is to determine whether the program had a **statistically significant** effect on weight.

We do this by calculating a **95% confidence interval** for the **mean difference** in paired samples.

---

## 📊 Methodology

- The dataset is stored in an Excel file.
- We calculate the difference in weight for each participant.
- Then we compute:
  - Sample mean of the differences
  - Sample standard deviation
  - Standard error
  - t-critical value (from t-distribution)
  - Confidence interval using the formula:

\[
\bar{d} \pm t_{\alpha/2, n-1} \cdot \frac{s_d}{\sqrt{n}}
\]

---

## 💻 Tools Used

- Python 3.13
- Libraries: `pandas`, `numpy`, `scipy`, `openpyxl`

---

## ⚙️ How to Run

1. Install required libraries:

```bash
pip install -r requirements.txt
```


Run the script:

```bash
python main.py
```
> 📁 Make sure the Excel file is placed in the `/data` folder.
