## 📈 OLS Regression: Predicting Healthcare Costs

## 🧾 Source Code

You can view the full regression model implementation in [`Prediction.py`](./Prediction.py).


### 📊 Objective  
I built an Ordinary Least Squares (OLS) regression model to **predict patient healthcare costs** based on the following features:
- `age` (numeric)
- `gender` (0 = Female, 1 = Male)
- `has_condition` (0 = No, 1 = Yes)

---

### 🧪 Results Summary

| Metric              | Value     |
|---------------------|-----------|
| R-squared           | 0.993     |
| Adjusted R-squared  | 0.990     |
| F-statistic         | 300.9     |
| p-value (overall)   | < 0.001   |
| Observations (n)    | 10        |

---

### 📌 Coefficient Table

| Feature         | Coefficient | p-value | Interpretation |
|-----------------|-------------|---------|----------------|
| Intercept       | 76.86       | 0.022   | Base cost when all other features are 0. |
| `age`           | 4.16        | 0.001   | Each additional year increases cost by ~$4.16. **Statistically significant.** |
| `gender`        | 14.68       | 0.328   | Male patients cost ~$14.68 more, **not statistically significant**. |
| `has_condition` | 214.10      | <0.001  | Patients with a condition cost ~$214 more. **Strong, significant effect.** |

---

### 🧠 Interpretation

- The model explains **99.3% of the variance in healthcare costs**, suggesting an excellent fit for this dataset.
- **Age** and **medical condition status** are **strong, significant predictors** of healthcare costs.
- **Gender** does not appear to significantly impact cost in this sample.
- The model is statistically significant overall, with an F-statistic p-value < 0.001.

---

### ⚠️ Limitations

- The dataset is small (n=10), so results should be interpreted with caution.
- With more data, results may generalize better, and variable significance could change.

