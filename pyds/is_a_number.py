def isANumber(x):
  if type(x) is bool:
    return False

  try:
    float(x)
    return True
  except:
    return False
