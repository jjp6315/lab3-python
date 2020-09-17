# Author: Ji Woong Park jjp6315@psu.edu
# Collaborator: Joshua Watt jhw5304@psu.edu
# Collaborator: Claudio Tapia-Manon cbt311@psu.edu
# Collaborator: Dongsheng Zang dkz5086@psu.edu
# Section: 005R
# Breakout: 9

def sum_n(n):
  if n == 0:
    return n
  else: 
    return n + sum_n(n-1)
    

def print_n (s, n):
  if n == 0: 
    return
  else:
    print (f"{s}")
    print_n(s, n-1)

def run():
  n = input("Enter an int: ")
  n = int(n)
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")

  print_n(s, n)

if __name__ == "__main__":
  run()