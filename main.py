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

# Prepare financial statement
def prepFinancialStatement(investment = 50000, marketing_percent = 0.25, operations_percent = 0.25, acquisition_percent = 0.25, cac = 5):
  marketing_cost = investment * marketing_percent
  operations_cost = investment * operations_percent
  acquisition_cost = investment * acquisition_percent
  customers_acquired = int(acquisition_cost / cac)

  financialStatement = {
    "marketing_cost": marketing_cost,
    "operations_cost": operations_cost,
    "acquisition_cost": acquisition_cost,
    "customers_acquired": customers_acquired
  }

  for key, value in financialStatement.items():
    print(f"{key}: {value}")