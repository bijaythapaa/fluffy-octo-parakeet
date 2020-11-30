def timesTwo(var):
	return var*2

seq = [1,2,3,4,5,6]

value1 = map(timesTwo, seq)
print(value1)

value2 = list(map(timesTwo, seq))
print(value2)
