import numpy as np
import pandas as pd
from semopy import Model

# --- データの生成 (ご提示のコード) ---
np.random.seed(42)
n = 10000
z2 = np.random.normal(0, 1, n)
z5 = np.random.normal(0, 1, n)
z6 = np.random.normal(0, 1, n)
z1 = 0.6 * z2 + np.random.normal(0, 1, n)
x = 0.6 * z1 + 0.6 * z5 + np.random.normal(0, 1, n)
z3 = 0.5 * x + np.random.normal(0, 1, n)
y = 1.0 * x + 0.6 * z2 + 0.6 * z3 + 0.6 * z6 + np.random.normal(0, 1, n)
z4 = 0.7 * x + 0.7 * y + np.random.normal(0, 1, n)

df = pd.DataFrame({'X':x, 'Y':y, 'Z1':z1, 'Z2':z2, 'Z3':z3, 'Z4':z4, 'Z5':z5, 'Z6':z6})

# --- semopyによるパス解析 ---

# 1. モデルの定義 (真のDAGを記述)
# 演算子 '~' は回帰関係（因果の方向）を示します
desc = """
    Z1 ~ Z2
    X ~ Z1 + Z5
    Z3 ~ X
    Y ~ X + Z2 + Z3 + Z6
    Z4 ~ X + Y
"""

# 2. モデルのインスタンス化と推定
model = Model(desc)
model.fit(df)

# 3. 推定結果の表示
# Estimateカラムが推定されたパス係数です
estimates = model.inspect()
print(estimates[['lval', 'op', 'rval', 'Estimate', 'Std. Err', 'z-value', 'p-value']])