def quotient(a,b):
  # a -> int
  # b -> int
  if not isinstance(a, int) or not isinstance(b, int):
    raise TypeError('Input should be an integer')
  try:
    return a/b
  except ZeroDivisionError:
	  return 'Invalid! cannot divide by 0'
