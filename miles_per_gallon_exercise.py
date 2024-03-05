# let's create a program that approximater the number or miles per gallon that a car gets !
# first, we'll import randint function by "function import"

from random import randint
# now let's create our MPG function using floor division to avoid float results and we will also need the return function !

def mimi_mpg(m, g):
  return(m//g)

# declaring our variables
miles = randint(200, 400)
gas = randint(10, 25)

print("mimi, the car can travel " + str(mpg(miles, gas)) + " miles!\nthat's because the car's fuel tank can hold " + str(gas) + 
      " gallons of gas,\nwhich means it can cover " + str(miles) + " miles on a full tank!)  
