#冪乗法による固有値計算

import ast
import numpy as np

def power_method(matrix, initial_vector, tolerance=0.001, max_iterations=5):
    """
    冪乗法を用いて最大固有値と対応する固有ベクトルを計算する関数

    Parameters:
        matrix (numpy.ndarray): 対象の行列
        initial_vector (numpy.ndarray): 初期ベクトル
        tolerance (float): 収束判定の許容誤差
        max_iterations (int): 最大反復回数

    Returns:
        eigenvalue (float): 近似した最大固有値
        eigenvector (numpy.ndarray): 近似した固有ベクトル
    """
    eigenvector = initial_vector.copy()
    print("\n=== 冪乗法による固有値計算 ===\n")
    for iteration in range(1, max_iterations + 1):
        # 次の反復ベクトルを計算
        next_vector = matrix @ eigenvector
        # 固有値の近似値 (r) を計算
        eigenvalue = next_vector[0, 0]
        # ベクトルを正規化
        eigenvector = next_vector / eigenvalue

        print(f"反復 {iteration}: 近似固有値 = {eigenvalue}")
        print(f"  次のベクトル:\n{eigenvector}")

        # 収束判定
        if np.linalg.norm(matrix @ eigenvector - eigenvalue * eigenvector) < tolerance:
            print("\n収束しました！\n")
            return eigenvalue, eigenvector

    print("\n最大反復回数に達しましたが収束しませんでした。\n")
    return None, None

if __name__ == "__main__":
    # 行列の入力
    print("対象の行列を入力 (例: [[2, 1], [1, 3]]):")
    matrix_input = input()
    matrix = np.array(ast.literal_eval(matrix_input), dtype=float)

    # 初期ベクトルの入力
    print("\n初期ベクトルを入力 (例: [[1], [1]]):")
    initial_vector_input = input()
    initial_vector = np.array(ast.literal_eval(initial_vector_input), dtype=float)

    # 冪乗法を実行
    eigenvalue, eigenvector = power_method(matrix, initial_vector)

    # 結果を表示
    if eigenvalue is not None:
        print("\n=== 結果 ===")
        print(f"最大固有値の近似値: {eigenvalue}")
        print("対応する固有ベクトル:")
        print(eigenvector)