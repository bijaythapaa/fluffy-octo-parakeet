# def timesTwo(var):
# 	return var*3

# def timesTwo(var): return var*3

# f = lambda var: var*3
# print(f(6))

seq = [1, 2, 3, 4, 5, 6]

# values = list(map(timesTwo, seq))

values = list(map(lambda x: x*3, seq))
print(values)
