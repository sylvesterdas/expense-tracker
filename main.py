from log import printInfo, printSuccess, printError, printWarn
from time import sleep
from data import data

def add ():
  amount = input("Enter amount: ")

  try:
    amount = float(amount)
  except:
    printError('Invalid amount')
    return add()

  description = input("Enter description: ")

  category = input("Enter category: ")

  new_expense = [ amount, description, category ]
  data.loc[len(data)] = new_expense
  printSuccess("Expense added!")
  print('')

def view ():
  print(data.to_markdown())
  printInfo('Total amount: ' + str(data['Amount'].sum()))
  print('')

def home ():
  print("Expense Tracker Menu:")
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Exit")
  res = input("Enter your choice: ")

  if res == "1":
    print('')
    add()
  elif res == "2":
    sleep(0.1)
    view()
  elif res == "3":
    printWarn('Shutting down...')
    sleep(0.25)
    printSuccess('Exiting Expense Tracker. Goodbye!')
    sleep(0.25)
    return exit(1)
  else:
    printError('invalid option')

  return home()

if __name__ == "__main__":
  home()
