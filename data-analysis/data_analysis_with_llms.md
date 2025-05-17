# Data Analysis with LLMs: A Comprehensive Guide for Digital Health

## Overview

This section is designed for digital health professionals who are experienced in data analysis and statistics (especially in medical/scientific contexts), but are not expert coders. Here, you'll learn how to leverage Large Language Models (LLMs) to generate R and Python code for your analyses, review and run the code, and interpret the results—specifically tailored for digital health data and workflows.

---

## Why Use LLMs for Data Analysis in Digital Health?
- **Automate code writing:** Let the LLM write R/Python code for your statistical analyses.
- **Bridge the gap:** Focus on your analytical expertise, not on coding syntax.
- **Speed up workflows:** Quickly generate, modify, and rerun analyses.
- **Learn by example:** See how code is structured for different analyses.
- **Handle complex, real-world data:** EHR, wearable, and clinical trial data often require custom code—LLMs can help.

---

## Typical Digital Health Data Types
- **Electronic Health Records (EHR):** Patient demographics, diagnoses, medications, lab results, visit history
- **Wearable Device Data:** Heart rate, steps, sleep, activity, continuous glucose monitoring
- **Clinical Trial Data:** Randomized groups, outcomes, adverse events, longitudinal measurements
- **Patient-Reported Outcomes:** Surveys, symptom diaries, quality of life scores
- **Imaging and Sensor Data:** DICOM files, time series, signals

---

## Common Analyses in Digital Health
- Descriptive statistics and cohort characterization
- Longitudinal data analysis (repeated measures, time series)
- Survival analysis (time-to-event, e.g., hospitalization, death)
- Predictive modeling (risk scores, machine learning)
- Comparative effectiveness (RCTs, observational studies)
- Data visualization (trends, outliers, patient journeys)
- Missing data handling and imputation
- Subgroup and stratified analyses
- Adverse event monitoring

---

## Example LLM Prompts for Digital Health Data

### 1. EHR Data: Cohort Characterization
```
I have an EHR dataset with columns: patient_id, age, sex, diagnosis_code, medication, visit_date, lab_glucose. Generate Python code to:
- Summarize age and sex distribution
- List the top 10 most common diagnosis codes
- Calculate the mean and SD of lab_glucose by diagnosis_code
```

### 2. Wearable Data: Time Series Analysis
```
I have wearable data with columns: user_id, timestamp, heart_rate, steps. Generate R code to:
- Plot average daily heart rate over time for each user
- Detect days with unusually high step counts
```

### 3. Clinical Trial: Survival Analysis
```
I have trial data with columns: subject_id, treatment_group, event_time, event_status (1=event, 0=censored). Generate R code to:
- Perform Kaplan-Meier survival analysis by treatment group
- Plot survival curves with confidence intervals
- Test for differences using the log-rank test
```

### 4. Patient-Reported Outcomes: Longitudinal Analysis
```
I have survey data with columns: patient_id, visit_week, symptom_score. Generate Python code to:
- Plot symptom_score over time for each patient
- Fit a mixed-effects model to assess change over time
```

### 5. Predictive Modeling: Risk Score
```
I have a dataset with columns: age, sex, BMI, smoking_status, outcome (1=event, 0=no event). Generate Python code to:
- Fit a logistic regression model to predict outcome
- Output the odds ratios and 95% confidence intervals
- Plot the ROC curve and calculate AUC
```

### 6. Data Cleaning and Imputation
```
I have missing values in EHR data. Generate R code to:
- Show missingness by column
- Impute missing lab values using multiple imputation
```

---

## Advanced Workflows: Integrating LLMs into Digital Health Research

1. **Define your research question and data structure.**
2. **Use LLMs to generate code for data cleaning, analysis, and visualization.**
3. **Request code comments and explanations for transparency.**
4. **Iterate: Ask for code modifications, additional analyses, or alternative methods.**
5. **Document your workflow and code for reproducibility.**
6. **Validate results with your domain expertise and statistical knowledge.**
7. **Share code and results with collaborators (remove sensitive data).**

---

## Code Safety, Reproducibility, and Privacy
- **Always review LLM-generated code before running.**
- **Test on a sample or synthetic dataset first.**
- **Request code comments and explanations.**
- **Document all code and analysis steps.**
- **Never share real patient data with public LLMs.**
- **Use version control (e.g., Git) for code and analysis scripts.**
- **Consider using reproducible environments (e.g., RMarkdown, Jupyter Notebooks, Docker).**

---

## Ethical Considerations in Digital Health Data Analysis
- **Patient privacy:** De-identify data before sharing or analysis.
- **Bias and fairness:** Be aware of potential biases in data and models.
- **Transparency:** Document all analysis steps and code.
- **Clinical impact:** Validate findings before clinical application.
- **Regulatory compliance:** Follow relevant laws (e.g., HIPAA, GDPR).

---

## Glossary
- **EHR:** Electronic Health Record
- **AUC:** Area Under the Curve (for ROC analysis)
- **Kaplan-Meier:** A method for estimating survival probabilities
- **Mixed-effects model:** A statistical model for repeated measures/longitudinal data
- **Imputation:** Filling in missing data values
- **ROC Curve:** Receiver Operating Characteristic curve, used to evaluate classifiers
- **Log-rank test:** A statistical test to compare survival curves

---

## Useful Resources
- [R for Data Science (Book)](https://r4ds.had.co.nz/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Statistical Analysis with Python (SciPy)](https://scipy-lectures.org/)
- [Survival Analysis in R](https://cran.r-project.org/web/views/Survival.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [NIH All of Us Data & Tools](https://allofus.nih.gov/data-tools)
- [OHDSI (Observational Health Data Sciences and Informatics)](https://www.ohdsi.org/)
- [MIMIC-IV Clinical Database](https://physionet.org/content/mimiciv/)

---

## Case Studies: Real-World Digital Health Data Analysis with LLMs

### Why Case Studies?
Case studies provide concrete, real-world examples of how LLMs can be used to solve digital health data analysis problems. They help you:
- See the end-to-end workflow in action
- Understand how to structure prompts and interpret results
- Learn from practical challenges and solutions

### Case Study Template
Use this template to document your own digital health data analysis case studies:

**Title:** [Descriptive title of the case study]

**Background:**
- Brief description of the clinical or research context
- Data source and type (EHR, wearable, trial, etc.)

**Objective:**
- What question are you trying to answer?

**Data Description:**
- Key variables/columns
- Sample size and relevant characteristics

**Analysis Steps:**
1. Data cleaning/preparation
2. Descriptive statistics
3. Main analysis (e.g., regression, survival, prediction)
4. Visualization
5. Interpretation

**LLM Prompts Used:**
- List the prompts you gave to the LLM for each step

**Code Generated:**
- Paste or summarize the code provided by the LLM

**Results:**
- Key findings, tables, or plots

**Challenges & Solutions:**
- Any issues encountered and how you addressed them (with or without LLM help)

**Lessons Learned:**
- What worked well, what could be improved

---

### Example Case Study: Predicting Hospital Readmission Using EHR Data

**Title:** Predicting 30-Day Hospital Readmission from EHR Data

**Background:**
Hospital readmissions are costly and often preventable. Predicting which patients are at high risk can help target interventions.

**Objective:**
Develop a predictive model for 30-day readmission using EHR data and LLM-generated code.

**Data Description:**
- Source: De-identified EHR extract
- Variables: patient_id, age, sex, diagnosis_code, length_of_stay, prior_admissions, discharge_disposition, readmitted_30d (1/0)
- N = 5,000 admissions

**Analysis Steps:**
1. Data cleaning: Handle missing values, encode categorical variables
2. Descriptive stats: Summarize age, sex, readmission rate
3. Predictive modeling: Logistic regression for readmitted_30d
4. Visualization: ROC curve, feature importance
5. Interpretation: Odds ratios, model performance

**LLM Prompts Used:**
- "Generate Python code to clean EHR data, impute missing values, and encode categorical variables."
- "Write code to fit a logistic regression model predicting readmitted_30d."
- "Show how to plot the ROC curve and calculate AUC."
- "Explain how to interpret the odds ratios."

**Code Generated:**
- Data cleaning with pandas and scikit-learn
- Logistic regression with statsmodels
- ROC curve with scikit-learn

**Results:**
- AUC = 0.72
- Top predictors: prior_admissions, length_of_stay, discharge_disposition

**Challenges & Solutions:**
- Categorical variable encoding: LLM suggested one-hot encoding
- Missing data: LLM provided imputation code
- Model interpretation: LLM explained odds ratios and feature importance

**Lessons Learned:**
- LLMs can rapidly generate analysis code, but results must be validated
- Clear, specific prompts yield better code
- Iterative prompting helps refine analysis and troubleshoot issues

---

*Add your own case studies here as you experiment with LLMs in digital health!* 