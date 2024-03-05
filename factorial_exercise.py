# create a function which takes one positive integer and its input and returns its factorial
# the factorial of a number is the product of all the integers from 1 to that number, ex.: 3 factorial (3*2*1) = 6 !!
def mimi_factorial(mimi_num):
  mimi_result = 1 # since it will be multiplied, it was given the initial value of 1 instead of the usual 0 !

  for counter in range(mimi_num, 1, -1): # execute this loop x times from given number to 1, decrease 1 each time 
    mimi_result *= counter # mimi_result = mimi_result * counter

  return mimi_result # save the value of mimi_result variable on memory

print(mimi_factorial(3)) # 6
print(mimi_factorial(4)) # 24
print(mimi_factorial(5)) # 120
