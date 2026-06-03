import numpy as np
import pandas as pd
import statsmodels.api as sm
from itertools import combinations

# 1. データ生成 (DGP)
np.random.seed(42)
n = 10000
z2 = np.random.normal(0, 1, n)
z5 = np.random.normal(0, 1, n)
z6 = np.random.normal(0, 1, n)
z1 = 0.6 * z2 + np.random.normal(0, 1, n)
x = 0.6 * z1 + 0.6 * z5 + np.random.normal(0, 1, n)
z3 = 0.5 * x + np.random.normal(0, 1, n)

y = x + 0.6 * z2 + 0.6 * z3 + 0.6 * z6 + np.random.normal(0, 1, n)
z4 = 0.7 * x + 0.7 * y + np.random.normal(0, 1, n) # 合流点

df = pd.DataFrame({'X':x, 'Y':y, 'Z1':z1, 'Z2':z2, 'Z3':z3, 'Z4':z4, 'Z5':z5, 'Z6':z6})

X_data = df[['X', 'Z2', 'Z6']]  # バックドア基準を満たす変数
m = sm.OLS(df['Y'], X_data).fit()

print("【バックドア基準を満たす変数での回帰結果】")
print(m.summary())