import numpy as np

results = []

np.random.seed(42)

for a in [0, 1]:
    n = 1000
    
    # 外生変数
    z2 = np.random.normal(0, 1, n)
    z5 = np.random.normal(0, 1, n)
    z6 = np.random.normal(0, 1, n)
    z1 = 0.6 * z2 + np.random.normal(0, 1, n)
    
    # Xを介入によって固定
    x = np.full(n, a)  
    
    # 構造方程式に従って他の変数が決まる
    z3 = 0.5 * x + np.random.normal(0, 1, n)
    y = 1.0 * x + 0.6 * z2 + 0.6 * z3 + 0.6 * z6 + np.random.normal(0, 1, n)
    
    # 合流点
    z4 = 0.7 * x + 0.7 * y + np.random.normal(0, 1, n) 
    
    y_mean = np.mean(y)
    results.append({'X_val': a, 'Y_mean': y_mean})

# 因果効果の算出
ate = results[1]['Y_mean'] - results[0]['Y_mean']

print(f"X=0のときのYの平均: {results[0]['Y_mean']:.4f}")
print(f"X=1のときのYの平均: {results[1]['Y_mean']:.4f}")
print(f"真の総効果 (ATE): {ate:.4f}")