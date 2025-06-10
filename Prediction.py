import pandas as pd
import statsmodels.api as sm

# Example dataset (patient features and costs)

data = {
    'age': [25, 35, 52, 36, 23, 43, 52, 48, 35, 40],
    'gender': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1], # 0 = Female, 1 = Male
    'has_condition': [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    'costs': [200, 450, 500, 220, 180, 470, 300, 520, 210, 480]
}

df = pd.DataFrame(data)

# Define predictors and target
X = df[['age', 'gender', 'has_condition']]
X = sm.add_constant(X) # add intercept term
y = df['costs']

# Fit regression model
model = sm.OLS(y, X).fit()

# Summary output
print(model.summary())

