# Write a Python program that declares a class describing
# your favorite animal. Have the data members of the class
# represent the following physical parameters of the animal:
# length of the arms (float), length of the legs (float),
# number of eyes (int), does it have a tail? (bool),
# is it furry? (bool). Write an initialization function that
# sets the values of the data members when an instance of the
# class is created. Write a member function of the class to print out
# and describe the data members representing the physical characteristics
# of the animal.

class Fav_Animal:

    def __init__(self, arms = 2, legs = 2, eyes = 2, tail =  True, furry = True):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def __str__(self):
        s = ""
        p = ""

        if self.furry:
            s = "They are very furry"
        else:
            s = "they dont have any fur"

        if self.tail:
            p = "They have a really cool tail"
        else:
            p = "They dont have a tail and that's ok"

        return f'''My favorite animal has {self.arms} arms and {self.legs} legs.
{s}.
{p}.
I was surprised to see they had {self.eyes} eyes.\n
'''

if __name__ == "__main__":
    Alexis = Fav_Animal(3, 6, 3,True, True)
    print(f"Alexis has something to say about his animal\n{Alexis}")
    Jack = Fav_Animal()
    print(f"Jack has something to say about his animal\n{Jack}")