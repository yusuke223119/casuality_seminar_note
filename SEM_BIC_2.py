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
# 真の直接効果を 1.0 に設定 (y = 1.0*x + ...)
y = 1.0 * x + 0.6 * z2 + 0.6 * z3 + 0.6 * z6 + np.random.normal(0, 1, n)
z4 = 0.7 * x + 0.7 * y + np.random.normal(0, 1, n) # 合流点

df = pd.DataFrame({'X':x, 'Y':y, 'Z1':z1, 'Z2':z2, 'Z3':z3, 'Z4':z4, 'Z5':z5, 'Z6':z6})

# 2. BICによる全モデル探索
candidates = ['X', 'Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']
results = []

for k in range(1, len(candidates) + 1):
    for combo in combinations(candidates, k):
        # モデルの構築
        X_data = df[list(combo)]
        model_fit = sm.OLS(df['Y'], X_data).fit()
        
        # モデルオブジェクト，BIC，変数セットを保存
        results.append({
            'model': model_fit, 
            'bic': model_fit.bic,
            'variables': combo
        })

# DataFrameに変換して最小BICの行を特定
res_df = pd.DataFrame(results)
best_index = res_df['bic'].idxmin()
best_row = res_df.loc[best_index]

# 3. 結果の表示
print("=== BICが選んだ最善のモデル詳細 ===")
print(f"最小BIC値: {best_row['bic']:.4f}")
print(f"選択された変数: {best_row['variables']}")
print(best_row['model'].summary())

import matplotlib.pyplot as plt
import pandas as pd

def export_minimal_model_to_png(best_row, filename="bic_minimal_result.png"):
    model_result = best_row['model']
    selected_vars = best_row['variables']
    
    # 1. 係数テーブルの取得
    tbl = model_result.summary().tables[1]
    df_res = pd.DataFrame(tbl.data[1:], columns=tbl.data[0])
    df_res.set_index('', inplace=True)
    
    # 2. coef と std err だけに絞り込む
    # 列名にスペースが含まれている場合があるため，ストリップして選択
    df_res.columns = [c.strip() for c in df_res.columns]
    df_minimal = df_res[['coef', 'std err']]

    # 3. 描画準備
    fig, ax = plt.subplots(figsize=(8, 5)) # 列を絞ったので横幅を少しスリムに
    ax.axis('off')

    # 4. テーブル作成
    the_table = ax.table(cellText=df_minimal.values,
                         colLabels=df_minimal.columns,
                         rowLabels=df_minimal.index,
                         loc='center',
                         cellLoc='center')

    # 5. デザイン調整
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    the_table.scale(1.2, 2.5) # 高さを出すと見やすくなります

    # ヘッダーとインデックスの装飾
    for (row, col), cell in the_table.get_celld().items():
        if row == 0 or col == -1:
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#f5f5f5')

    # タイトルに選ばれた変数を表示
    variables_str = ", ".join(selected_vars)
    plt.title(f"BIC Best Model Selection: [{variables_str}]", 
              pad=30, fontsize=13, weight='bold')

    # 6. 保存
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Minimal report saved: {filename}")

# 実行
export_minimal_model_to_png(best_row)