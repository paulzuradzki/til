## Simple Linear Regression with Python `statsmodels` vs R lm() function


### Python

```python
import statsmodels.api as sm

cars = sm.datasets.get_rdataset(dataname="cars", package="datasets")
cars_df = cars.data

##########################################################################
# using statsmodels API
    # statsmodels does not include intercept by default using this method
    # use statsmodels.api.add_constant()
##########################################################################
Y = cars_df['dist']
X = cars_df['speed']
X = sm.add_constant(X)
cars_model = sm.OLS(Y, X)

##########################################################################
# using statsmodels R-style "formula" API
##########################################################################
cars_model = smf.ols(formula='dist ~ speed', data=cars_df)
results = cars_model.fit()

print(results.summary())
print()
print(f"pvalues:\n{results.pvalues}")
```

Model Summary
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   dist   R-squared:                       0.651
Model:                            OLS   Adj. R-squared:                  0.644
Method:                 Least Squares   F-statistic:                     89.57
Date:                Fri, 10 Jun 2022   Prob (F-statistic):           1.49e-12
Time:                        19:31:00   Log-Likelihood:                -206.58
No. Observations:                  50   AIC:                             417.2
Df Residuals:                      48   BIC:                             421.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    -17.5791      6.758     -2.601      0.012     -31.168      -3.990
speed          3.9324      0.416      9.464      0.000       3.097       4.768
==============================================================================
Omnibus:                        8.975   Durbin-Watson:                   1.676
Prob(Omnibus):                  0.011   Jarque-Bera (JB):                8.189
Skew:                           0.885   Prob(JB):                       0.0167
Kurtosis:                       3.893   Cond. No.                         50.7
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

pvalues:
Intercept    1.231882e-02
speed        1.489836e-12
dtype: float64
```

### R
```r
# set up linear model
cars_lm = lm(dist ~ speed, data = cars)

summary(cars_lm)$coefficients
#               Estimate Std. Error   t value     Pr(>|t|)
# (Intercept) -17.579095  6.7584402 -2.601058 1.231882e-02
# speed         3.932409  0.4155128  9.463990 1.489836e-12

# select by p-value by label
summary(cars_lm)$coefficients['speed', 'Pr(>|t|)']  # -> [1] 1.489836e-12

# select p-value by row-column position
summary(cars_lm)$coefficients[2, 4]                 # -> [1] 1.489836e-12
```


`> (summary(cars_lm))`
```
Call:
lm(formula = dist ~ speed, data = cars)

Residuals:
    Min      1Q  Median      3Q     Max 
-29.069  -9.525  -2.272   9.215  43.201 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) -17.5791     6.7584  -2.601   0.0123 *  
speed         3.9324     0.4155   9.464 1.49e-12 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 15.38 on 48 degrees of freedom
Multiple R-squared:  0.6511,	Adjusted R-squared:  0.6438 
F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
```
