# let's create some objects which will inherit methods and states from a parent class
# for this example, we will make a set of coins that can rust, be cleaned, be flipped and spent
# we'll use the british coins as examples: 1p (one pence), 2p, 5p, 10p, 20p, 50p, £1 (one pound) and £2

import random  # for the flip method


class Coin:  # this will be our parent class
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):  # **kwargs = Key Word ARGuments !!
        # by using this inside the innit function of our parent class, we are now able to take those key word arguments
        # we created on out objects and pack them down into a dictionary called "kwargs" to be used

        for key, value in kwargs.items():  # key-value pairs !!
            setattr(self, key, value)  # setattr =  set attribute !!

        self.is_rare = rare  # a few states for our objects to inherit
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25  # if a coin is rare (like a rare edition), its value goes up
        else:
            self.value = self.original_value

        if self.is_clean:  # a clean coin will have its original colour
            self.colour = self.clean_colour
        else:  # a rusted coin will change colour depending on which data you put in that coin's object dictionary !!
            self.colour = self.rusty_colour

    # make sure the method isn't inside another method !!
    def rust(self):  # for rusting our coins
        self.colour = self.rusty_colour

    def clean(self):  # cleaning the coins
        self.colour = self.clean_colour

    def __del__(self):  # spending the coins
        print("Coin spent!")

    def flip(self):  # flipping the coins
        # which can be heads if heads_options == True or tails if heads_options == False
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):  # this defines what comes out when you print the object, so it'll look organized in the output
        if self.original_value >= 1.00:
            return "£{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))  # let's multiply the value so in the example it
            # looks like 1p (instead of 0.01p), 2p, 5p, etc.


# our first object that will inherit from the parent class is a one pound coin (£1)
class One_Pound(Coin):  # class names should start with capital letters !!
    def __init__(self):  # first we need a constructor method to define some things
        data = {  # now we need a dictionary of data for the Pound class
            "original_value": 1.00,  # £
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,  # because it's a circle
            "diameter": 22.5,  # mm
            "thickness": 3.15,  # mm
            "mass": 9.5  # g
        }
        super().__init__(**data)  # unpack to use in the parent class !!


# now let's set up the other coins !!

class One_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,  # £
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,  # mm
            "thickness": 1.52,  # mm
            "mass": 3.56  # g
        }
        super().__init__(**data)


class Two_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.02,  # £
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,  # mm
            "thickness": 1.85,  # mm
            "mass": 7.12  # g
        }
        super().__init__(**data)


class Five_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,  # £
            "clean_colour": "silver",
            "rusty_colour": None,  # silver coins don't rust, we will need to override the stardard behaviour
            # that we get from the parent class
            "num_edges": 1,
            "diameter": 18.0,  # mm
            "thickness": 1.77,  # mm
            "mass": 3.25  # g
        }
        super().__init__(**data)

        def rust(self):  # polymorphism = when the same function name has different forms, shapes and versions !!
            self.colour = self.clean_colour  # now we made it so the rust method inherited from the parent class behaves
            # differently for this specific object


class Ten_Pence(Coin):  # another silver coin
    def __init__(self):
        data = {
            "original_value": 0.10,  # £
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,  # mm
            "thickness": 1.85,  # mm
            "mass": 6.50  # g
        }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour


class Twenty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,  # £
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,  # this coin is a heptagon !!
            "diameter": 21.4,  # mm
            "thickness": 1.7,  # mm
            "mass": 5.00  # g
        }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour


class Fifty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,  # £
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,  # another heptagon
            "diameter": 27.3,  # mm
            "thickness": 1.78,  # mm
            "mass": 8.00  # g
        }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour


class Two_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,  # £
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,  # mm
            "thickness": 2.50,  # mm
            "mass": 12.00  # g
        }
        super().__init__(**data)


# let's make a list of coins
coins = [One_Pence(), Two_Pence(), Five_Pence(),
         Ten_Pence(), Twenty_Pence(), Fifty_Pence(),
         One_Pound(), Two_Pound()]
# now we will loop through each of them
for coin in coins:
    arguments = [coin, coin.colour, coin.value,
                 coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]
    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(
        *arguments)  # here we are unpacking the arguments we created

    print(string)

# the "coin spent!" x8 output happens because the destructor method of our parent class prints it when it is deleted;
# since Python manages memory for us, the object is automatically deleted when it's no longer needed, AKA when the
# script ends, even though you did not explicitly use del on it.
