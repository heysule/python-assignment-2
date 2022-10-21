def printEvenNumbersForLoop():
  for number in range(1,31):
    if(number % 2 == 0):
      print(number)

def printEvenNumbersWhileLoop():
  i = 1
  while(i < 31):
    if (i % 2 == 0):
      print(i)
    i += 1