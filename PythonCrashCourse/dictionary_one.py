d1 = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': [1, 2, 3,],
}
print(d1['key1'])
print(d1['key2'])

print(d1['key3'][2])
my_list = d1['key3']
print(my_list[0])

d2 = {
	'key1': 'value1',
	'key2': {
		'innerkey': [4, 5, 6,]
		}
}
print(d2['key2'])
print(d2['key2']['innerkey'])
print(d2['key2']['innerkey'][1])
