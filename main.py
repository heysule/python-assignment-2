# With a for & while loop, print even numbers from 1 - 30.
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

# With a for & while loop, print odd numbers from 1 - 30.
def printOldNumbersForLoop():
  for number in range(1,31):
    if(number % 2 != 0):
      print(number)

def printOldNumbersWhileLoop():
  i = 1
  while(i < 31):
    if (i % 2 != 0):
      print(i)
    i += 1