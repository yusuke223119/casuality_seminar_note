# Pearl-style Causal Inference Seminar

パール流因果推論のゼミ発表資料および再現用コードを管理するリポジトリです。

## 発表資料 (Main Materials)

- [スライド (PDF)](./Pearl_Style.pdf) : ゼミで使用したスライド本体
- [LaTeXソース](./Pearl_Style.tex) : スライドのテンプレート一式

## ソースコード (Scripts)

- `SEM_BIC.py`: BICを用いた全モデル探索と変数選択のスクリプト
- `DO.py`: 介入（do-演算）のシミュレーション
- `SEM_MLE.py`: 最尤推定によるパス係数推定用スクリプト

## 参考文献

[1] J. Pearl 著，黒木学訳，『統計的因果推論 ―モデル・推論・推測―』，共立出版，2009.
[2] 宮川雅巳著，『統計的因果推論 ―回帰分析の新しい枠組み―』，朝倉書店，2004.
[3] 宮川雅巳著，『グラフィカルモデル』，朝倉書店，1997.
[4] S. L. Lauritzen, A. P. Dawid, B. N. Larsen, and H. G. Leimer, “Independence properties of directed
Markov fields,” Networks, Vol. 20, No. 5, pp. 491–505, 1990.
