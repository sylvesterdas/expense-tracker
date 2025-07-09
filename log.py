RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def printError(message):
  print(RED + message + RESET)

def printSuccess(message):
  print(GREEN + message + RESET)

def printWarn(message):
  print(YELLOW + message + RESET)

def printInfo(message):
  print(BLUE + message + RESET)