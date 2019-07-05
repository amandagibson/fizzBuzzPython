print("Enter a number: ")
number = int(input())

if number % 15 is 0:
  print("Fizz Buzz!")
elif number % 5 is 0:
  print("Buzz!")
elif number % 3 is 0:
  print("Fizz!")
else:
  print(f"{number} is not divisible by 15, 5 or 3!")