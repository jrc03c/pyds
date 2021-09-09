oldFilter = filter

def filter(fn, arr):
  return list(oldFilter(fn, arr))
