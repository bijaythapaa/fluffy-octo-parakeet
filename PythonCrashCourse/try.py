d = {
	'k1': [
		1,
		2,
		3,
		{
		'tricky': [
			'oh',
			'man',
			'inception',
			{
			'target': [
				1,
				2,
				3,
				'hello',
			]
			}
		]
		}
	]
}

d1 = {
	'name': ['ram', 'shyam', 1, 2,],
	'last': 'shya',
	'age': 222,
}

l1 = [ 1, 2, 4, 5]

print(d1['name'][1])

print(d['k1'][3]['tricky'][3]['target'][3])

def findDog(text):
	temp = 'dog'
	count = 0
	input = text.split()

	for value in input:
		if value == temp:
			count += 1
		# if temp in input:
		# 	return True

	return count
	# return False


get_text = input("Ask For Dog: ")
print(findDog(get_text))
