# Module 03: Inferential Statistical Analysis

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-stats-8CAAE6?logo=scipy&logoColor=white) ![Level](https://img.shields.io/badge/Level-Beginner-2EA44F)

> Diploma in AI / Data Science · Term 1 · 8 sessions × 2 hours · [⬅ Term Home](../README.md)

Data scientists rarely see a whole population. They work with samples and must decide how far they can trust what the sample says. This module gives you that skill: describing data, reasoning with probability, measuring relationships, and testing ideas with confidence intervals, t, Z, chi-square and F tests, and ANOVA. Every concept is paired with short, commented Python scripts you can run and change.

## 🎯 What You Will Learn

- Describe data with measures of centre, spread and shape
- Use probability rules, Bayes' theorem, random variables and common distributions
- Explain the Central Limit Theorem and the standard error
- Measure relationships with Pearson and Spearman correlation and predict with regression
- Draw conclusions about populations with sampling, confidence intervals and hypothesis tests
- Choose and run chi-square, t, Z and F tests correctly
- Compare many groups with one-way/two-way ANOVA and understand MANOVA

## 📋 Prerequisites

- School-level maths (fractions, percentages, square roots)
- Basic Python: variables, lists, loops and running a `.py` file (Module 04 Sessions 01-03 cover this)
- No previous statistics knowledge is needed

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| Python 3.12 | run the example scripts | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| NumPy, pandas, SciPy | numbers, tables and statistical tests (`pip install numpy pandas scipy`) | [https://scipy.org/install/](https://scipy.org/install/) |
| VS Code + Python extension | editor | [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial) |
| Anaconda (optional) | Python plus all libraries and Jupyter in one installer | [https://www.anaconda.com/download](https://www.anaconda.com/download) |

> 💡 Run each script from inside its session folder, e.g. `cd Session-04-Practice-Lab-Statistics-Probability-and-Regression` then `python lab1_descriptive_report.py`, so that CSV files are found.

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to Statistics | [Open notes](./Session-01-Introduction-to-Statistics/README.md) |
| 02 | Introduction to Probability | [Open notes](./Session-02-Introduction-to-Probability/README.md) |
| 03 | Correlation and Regression | [Open notes](./Session-03-Correlation-and-Regression/README.md) |
| 04 | Practice Lab: Statistics, Probability and Regression | [Open notes](./Session-04-Practice-Lab-Statistics-Probability-and-Regression/README.md) |
| 05 | Hypothesis Testing, Sampling and Confidence Intervals | [Open notes](./Session-05-Hypothesis-Testing-Sampling-and-Confidence-Intervals/README.md) |
| 06 | Exact Sampling Distributions: Chi-Square, t, Z and F Tests | [Open notes](./Session-06-Exact-Sampling-Distributions-Chi-Square-t-Z-F-Tests/README.md) |
| 07 | Analysis of Variance: ANOVA and MANOVA | [Open notes](./Session-07-Analysis-of-Variance-ANOVA-and-MANOVA/README.md) |
| 08 | Practice Lab: Inference Tests and ANOVA | [Open notes](./Session-08-Practice-Lab-Inference-Tests-and-ANOVA/README.md) |

## 🚀 Module Mini-Project

**Student Performance Study** - act as the data analyst for a training institute:

1. Collect (or generate realistic) data for at least 60 students: batch, city, gender, study hours, attendance, mid-term and final marks.
2. Write a descriptive report: centre, spread, outliers and skewness of each numeric column.
3. Estimate P(pass), P(pass | batch) and fit a normal model to final marks.
4. Measure correlations and fit a regression model to predict final marks.
5. Build a 95% confidence interval for average final marks.
6. Test: (a) Morning vs Evening marks (t-test), (b) gender vs pass/fail (chi-square), (c) city vs marks (ANOVA + Tukey), (d) mid-term vs final for the same students (paired t-test).
7. Submit your scripts and a 2-page `REPORT.md` with every result written in plain language.

## 🔗 Resources (official documentation)

- [Python `statistics` module](https://docs.python.org/3/library/statistics.html)
- [SciPy statistical functions (`scipy.stats`)](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
