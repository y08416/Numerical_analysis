#ニュートン法

import numpy as np

# 関数の定義
def function(x):
    """解きたい関数を書く"""
    return x**2-10*np.sin(x)-2

def derivative_function(x):
    """解きたい関数の導関数"""
    return 2*x-10*np.cos(x)

# 初期値と精度の設定
x_current = 3 # 初期値
tolerance = 0.001  # 小数点以下の桁数
iteration = 3  # 繰り返し回数

# ニュートン法のループ
while True:
    # ニュートン法の更新式: x_next = x_current - f(x)/f'(x)
    x_next = x_current - function(x_current) / derivative_function(x_current)
    
    # 結果の表示
    print(f"{iteration}回目: x = {x_next:.6f}, f(x) = {function(x_next):.6f}")
    
    # 収束判定: f(x)の絶対値が許容誤差以下か確認
    if abs(function(x_next)) < tolerance:
        break
    
    # 次のイテレーションに進む
    x_current = x_next
    iteration += 1

# 最終結果の表示
print(f"\n収束しました: 解 x ≈ {x_next:.6f}")