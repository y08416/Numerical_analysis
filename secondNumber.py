import ast
import numpy as np

def eigen(A):
    """
    最大固有値と最大固有ベクトルを使ってAの影響を取り除いた行列を計算する関数
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # 固有値と固有ベクトルをソート
    sorted_pairs = sorted(
        zip(eigenvalues, eigenvectors.T), 
        key=lambda x: x[0], 
        reverse=True
    )
    max_eigenvalue, max_eigenvector = sorted_pairs[0]
    
    # 最大固有ベクトルの外積を計算
    max_eigenvector_transposed = np.array([[max_eigenvector[0]], [max_eigenvector[1]]])
    outer_product = np.multiply(max_eigenvalue, np.outer(max_eigenvector, max_eigenvector_transposed))
    
    # Aから最大固有ベクトルの影響を除外
    A_dash = A - outer_product
    return A_dash

def second_largest_eigenvalue(matrix):
    """
    行列の2番目に大きい固有値を計算する関数
    """
    eigenvalues, _ = np.linalg.eig(matrix)
    sorted_eigenvalues = sorted(eigenvalues, reverse=True)
    return sorted_eigenvalues[0]

# 入力と処理
print("対象となる行列を入力（例: [[4, 1], [2, 3]]）:")
matrix_input = input() 
matrix = np.array(ast.literal_eval(matrix_input))

# 最大固有ベクトルの影響を取り除く
result_matrix = eigen(matrix)
print("\nAダッシュ（最大固有ベクトルの影響を取り除いた行列）:\n{}".format(result_matrix))

# 2番目の固有値を計算
second_eigenvalue = second_largest_eigenvalue(result_matrix)
print("\n2番目の固有値: {:.5f}".format(second_eigenvalue))