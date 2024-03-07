# our range is from 1 to 50, so we should put 51 as the limit
for num in range(1, 51):
  # first condition: if the number is divisible by both 3 and 5, "FizzBuzz" will be printed
    if num % 3 == 0 and num % 5 == 0:
      print("FizzBuzz")
  # second condition: if the number is divisible by 3, print "Fizz"
    elif num % 3 == 0:
      print("Fizz")
  # third condition: if the number is divisible by 5, print "Buzz"
    elif num % 5 == 0:
      print("Buzz")
  # fourth condition: if the number is not divisible by either of them, print the number
    else:
      print(num)
