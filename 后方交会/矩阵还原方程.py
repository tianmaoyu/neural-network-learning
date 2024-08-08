import sympy as sp

# 定义矩阵 A
A = sp.Matrix([
    [1, 2],
    [3, 4]
])

# 定义自变量向量 x
x1, x2 = sp.symbols('x1 x2')
x = sp.Matrix([x1, x2])

# 定义结果向量 b
b = sp.Matrix([5, 11])

# 进行矩阵乘法 Ax
Ax = A * x

# 生成方程组
equations = [sp.Eq(Ax[i], b[i]) for i in range(A.rows)]

# 打印方程组
for eq in equations:
    print(eq)

# 解方程组
solutions = sp.solve(equations, (x1, x2))
print(solutions)