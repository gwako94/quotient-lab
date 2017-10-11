def Divide(a,b):
  try:
    return a/b
  except TypeError:
	return 'Invalid! cannot divide by string'
  except ZeroDivisionError:
	return 'Invalid! cannot divide by 0'
  
