def isIterable(x):
  try:
    iter(x)
    return True
  except:
    return False
