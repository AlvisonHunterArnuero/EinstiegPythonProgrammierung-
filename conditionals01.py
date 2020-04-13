# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we
# are in trouble. Coded with love by Alvison Hunter Arnuero - April 2020

def parrot_trouble(talking, hour):
  if talking and (hour >= 7 and hour <= 20):
    return print ('Parrot can talk freely, we are in trouble is set to  ',False)
  elif talking and hour > 20:
    return print ('Parrot can NOT talk freely, we are in trouble is set to  ',True)
  elif talking == False:
    return print ('Parrot is not talking right now, we are in trouble is set to  ',False)
  else:
    return print  ('Parrot can NOT talk at all, we are in trouble set to  ',True)


parrot_trouble(True, 6)
parrot_trouble(True, 4)
parrot_trouble(True, 7)
parrot_trouble(False, 6)
