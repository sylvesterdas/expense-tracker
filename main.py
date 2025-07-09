from log import printInfo, printError, printWarn
import time

def home ():
  print("Expense Tracker Menu:")
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Exit")
  res = input("Enter your choice: ")

  if res == "1":
    printInfo('add')
  elif res == "2":
    printInfo('view')
  elif res == "3":
    printWarn('Shutting down...')
    time.sleep(0.25)
    return exit(1)
  else:
    printError('invalid option')

  return home()

if __name__ == "__main__":
  home()
