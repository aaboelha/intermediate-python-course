#!/usr/bin/python3

def main():
  import random
  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  print(f"the sum of the two rolls is: {dice_sum}")



if __name__== "__main__":
  main()
