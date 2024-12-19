#二分法
import numpy as np

# 解きたい関数を書く(ex. np.sin(x))
def target_function(x):
    return x**2-10*np.sin(x)-2

# 二分法による方程式の解探索（元の試行回数を再現）
def bisection_method(f, a, b, limit=2.23, max_iterations=50):
    """
    二分法で方程式f(x)=0の解を探す。
    
    Parameters:
        f: 解を求めたい関数
        a: 区間の左端 (初期値)
        b: 区間の右端 (初期値)
        limit: 停止条件 (区間の幅)
        max_iterations: 最大反復回数
        
    Returns:
        近似解 (解が見つからない場合はNone)
    """
    # 初期チェック: f(a)とf(b)の符号が同じ場合、二分法は適用できない
    if f(a) * f(b) > 0:
        print("f(a)とf(b)の符号が同じため、二分法が適用できません。")
        return None

    num_iterations = 0  # 試行回数
    print(f"0回目: a = {a:.16f}, b = {b:.16f}")

    while True:
        c = (a + b) / 2.0  # 中点

        # f(c)の符号を確認し、次の区間を決定
        if f(c) * f(a) > 0:
            a = c
        elif f(c) * f(b) > 0:
            b = c

        num_iterations += 1
        print(f"{num_iterations}回目: a = {a:.16f}, b = {b:.16f}, c = {c:.16f}")

        # 停止条件: 区間の幅がlimit未満または最大反復回数に達した場合
        if (b - a >= limit) or num_iterations >= max_iterations:
            break

    # 最終的な解（中点）
    solution = (a + b) / 2.0
    print(f"最終解: x ≈ {solution:.16f} (試行回数: {num_iterations})")
    return solution


# メイン実行部
if __name__ == "__main__":
    try:
        a = float(input("区間の左端 a を入力: "))
        b = float(input("区間の右端 b を入力: "))
        
        # 二分法の実行
        solution = bisection_method(target_function, a, b)
        if solution is not None:
            print(f"最終的な解: x ≈ {solution:.16f}")
    except ValueError:
        print("数値を入力してください。")