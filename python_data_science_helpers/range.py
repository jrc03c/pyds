oldRange = range

def range(a, b, step=1):
	return list(oldRange(a, b, step))
