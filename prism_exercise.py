# let's calculate the volume of a prism !

length = int(input("input length: "))
widht = int(input("input width: "))
height = int(input("input height: ")) # declare the variables !


def prism_volume(lp=length, wp=width, hp=height):
  return lp * wp * hp # define the function and its parameters
  # here you can see I made the default value of the parameters the variables


calc_volume = prism_volume() # create another variable to assign the function return value to !
print("the volume of the prism is: " + str(calc_volume) + " ml !") # don't forget to turn it into a string to concatenate !
