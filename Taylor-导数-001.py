from sympy import symbols, expand, Function

x,y=symbols("x y")
function = Function('f')
f=x**2+x*y+y**2
# 查看 f 的类型
print(type(f))
# 查看 f 可用的属性和方法
print(dir(f))
help(f.diff)

dif_x=f.diff(x)
dif_y=f.diff(y)
# function.subs()
dif_x_value=dif_x.subs({x:1,y:2})
dif_y_value=dif_x.subs({x:1,y:2})
taylor_series=f.subs({x: 1, y: 2}) +dif_x_value*(x-1)+ dif_y_value*(y-2)
# 展开表达式
taylor_series = expand(taylor_series)
print(taylor_series)