from collections import Iterable

def rounded(func):
		def wrapper(self, n):
			if(isinstance(n, Iterable)):
				ret = [round(i, 2) for i in n]

			else:
				ret = round(n, 2)

			func(self, ret)

		return wrapper