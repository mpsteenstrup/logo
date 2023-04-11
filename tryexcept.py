
def isInteger():
	a = input('write an integer: ')
	try:
		print(int(a))
	except:
		print('one more time')
		isInteger()

isInteger()
