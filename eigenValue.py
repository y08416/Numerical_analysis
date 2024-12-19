#固有値と固有ベクトルの計算

import ast
import numpy as np

def eigen(A):
    """
    与えられた正方行列 A の固有値と固有ベクトルを計算し表示する関数。
    """
    # 固有値と固有ベクトルの計算
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # 固有値から対角行列を生成
    diagonal_matrix = np.diag(eigenvalues)
    
    # 固有値の表示
    print("\n=== 固有値 ===")
    for i, value in enumerate(eigenvalues):
        print(f"λ{i+1}: {value}")
    
    # 固有値からなる対角行列の表示
    print("\n=== 固有値からなる対角行列 ===")
    print(diagonal_matrix)
    
    # 固有ベクトルの表示
    print("\n=== 固有ベクトル ===")
    for i, vector in enumerate(eigenvectors.T):  # 転置して列ごとにアクセス
        print(f"v{i+1} (λ{i+1}={eigenvalues[i]}): {vector}")

# 行列入力のガイド
print("対象となる正方行列を入力してください（例: [[2, 1], [1, 2]]）:")

# 入力を受け取り、行列に変換
try:
    matrix_A_input = input(">> ")
    matrix_A = np.array(ast.literal_eval(matrix_A_input))
    
    # 正方行列か確認
    if matrix_A.shape[0] != matrix_A.shape[1]:
        print("エラー: 入力した行列は正方行列ではありません。")
    else:
        eigen(matrix_A)
except Exception as e:
    print(f"入力エラー: {e}")