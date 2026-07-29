# Pearl-style Causal Inference Seminar

パール流因果推論のゼミ発表資料および再現用コードを管理するリポジトリです.

## 発表資料 (Main Materials)

- [スライド (PDF)](./Pearl_Style.pdf) : ゼミで使用したスライド本体
- [LaTeXソース](./Pearl_Style.tex) : スライドのテンプレート一式

## ソースコード (Scripts)

- `SEM_BIC.py`: BICを用いた全モデル探索と変数選択のスクリプト
- `DO.py`: 介入（do-演算）のシミュレーション
- `SEM_MLE.py`: 最尤推定によるパス係数推定用スクリプト
- `backdoor.py`: バックドア基準のシミュレーションコード

## 参考文献

- J. Pearl 著，黒木学訳，『統計的因果推論 ―モデル・推論・推測―』，共立出版，2009.
- 宮川雅巳著，『統計的因果推論 ―回帰分析の新しい枠組み―』，朝倉書店，2004.

- 宮川雅巳著，『グラフィカルモデル』，朝倉書店，1997.

- 清水昌平著，『因果探索入門』，講談社，2023.

- J. Pearl, D. Mackenzie著，夏目大訳，『因果推論の科学 「なぜ？」の問いにどう答えるか』，文藝春秋，2022.

- S. L. Lauritzen, A. P. Dawid, B. N. Larsen, and H. G. Leimer, “Independence properties of directed
  Markov fields,” Networks, Vol. 20, No. 5, pp. 491–505, 1990.

- I. Shpitser and J. Pearl, ``Identification of Joint Causal Effects in the Graphs with Confounded Joint Effects,'' in \textit{Proceedings of the 21st National Conference on Artificial Intelligence (AAAI-06)}, 2006, pp. 1219--1226.

- J. Tian and J. Pearl, ``Probabilities of Causation: Bounds and Identification,'' Proceedings of the Sixteenth Conference on Uncertainty in Artificial Intelligence, pp.~589--598, 2000.

- P. D. Stolley, ``When genius errs: R.A. Fisher and the lung cancer controversy,'' \textit{American Journal of Epidemiology}, vol. 133, no. 5, pp. 416--425, 1991.

- T. Verma and J. Pearl,
  ``Equivalence and Synthesis of Causal Models,''
  in Proceedings of the Sixth Conference on Uncertainty in Artificial Intelligence (UAI), 1990, pp. 255--270.

- P. Spirtes, C. Glymour, and R. Scheines,
  Causation, Prediction, and Search,
  2nd ed.,
  MIT Press, 2000.

- C. Meek,
  ``Causal Inference and Causal Explanation with Background Knowledge,''
  in Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence (UAI), 1995, pp. 403--410.

-  D. M. Chickering,
  ``Optimal Structure Identification with Greedy Search,''
  Journal of Machine Learning Research,
  vol. 3, pp. 507--554, 2002.

-  X. Zheng, B. Aragam, P. Ravikumar, and E. P. Xing,
  ``DAGs with NO TEARS: Continuous Optimization for Structure Learning,''
  in Advances in Neural Information Processing Systems (NeurIPS), vol. 31, 2018.



