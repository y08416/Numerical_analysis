#レイリー商

import numpy as np

def rayleigh_quotient(A, x, tol=1e-6, max_iter=3):
    """
    レイリー商を用いて行列Aの最大固有値を求める関数

    Parameters:
        A (numpy.ndarray): 正方行列
        x (numpy.ndarray): 初期ベクトル
        tol (float): 収束判定の許容誤差
        max_iter (int): 最大反復回数
    """
    x = x / np.linalg.norm(x)  # 初期ベクトルを正規化
    prev_r = 0  # 前回のレイリー商
    iteration = 0  # 反復回数

    while iteration < max_iter:
        # x_d = A * x
        x_d = A @ x  
        # レイリー商を計算
        r = (x @ x_d) / (x @ x)

        # 収束判定（前回との差が許容誤差以下なら終了）
        if abs(r - prev_r) < tol:
            break

        # x_d を正規化して次のxとする
        x = x_d / np.linalg.norm(x_d)
        prev_r = r  # レイリー商を更新
        iteration += 1

        print(f"Iteration {iteration}: レイリー商 = {r:.6f}, x = {x}")

    print("\n結果:")
    print(f"最大固有値（近似）: {r:.6f}")
    print(f"対応する固有ベクトル: {x}")

# 行列Aと初期ベクトルx
A = np.array([[7, -4], [2, 1]])
x = np.array([0, 1])

rayleigh_quotient(A, x)