# A^n 行列計算
import ast
import numpy as np

def calculate_matrix_power(matrix, power):
    """
    行列をn乗する関数
    :param matrix: 2次元配列 (行列)
    :param power: 整数 (乗数)
    :return: n乗された行列
    """
    return np.linalg.matrix_power(matrix, power)

def main():
    # ユーザーに行列の入力を促す
    print("行列を入力してください (例: [[1, 2], [3, 4]]): ")
    matrix_input = input()
    
    try:
        # 入力された文字列を2次元リストに変換
        matrix = np.array(ast.literal_eval(matrix_input))
    except (ValueError, SyntaxError):
        print("入力が不正です。正しい形式の行列を入力してください。")
        return
    
    # ユーザーに乗数の入力を促す
    try:
        power = int(input("乗数を入力してください (例: 2): "))
    except ValueError:
        print("乗数は整数で入力してください。")
        return

    # 行列のn乗を計算
    result = calculate_matrix_power(matrix, power)

    # 結果を表示
    print(f"\n行列の {power} 乗の結果:")
    print(result)

if __name__ == "__main__":
    main()