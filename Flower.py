#Corey Schwarz 17 June 2023
#The class "flower" is created, and any flower that exists grows and blooms. "Rose," "Daisy," and "Hydrangea" are all defined as a type of flower. Thus, roses, daisies, and hydrangeas are growing and blooming.
class Flower:
#The class, named Flower, is being defined
    def __init__(self, name): 
        self.name = name
#The Constructor Method is utilized, automatically assigning names to be outputed when the program is run.
    def grow(self):
        print("The " +self.name + " is growing.")
#Creates a function that executes the statement "is growing" when the flower has "grow" after it
    def bloom(self):
        print("The " + self.name + " is blooming.")
#Creates a function that executes the statement "is blooming" when the flower has "bloom" after it
def main():
    flower1 = Flower("Rose")
#Introduces "Rose" as a class of flower; using "Rose" will cause the function to recognize it as the class
    flower1.grow()
#Creates the grow function, adding "is growing" after the name "Rose"
    flower1.bloom()
#Creates the bloom function, adding "is blooming" after the name "Rose"
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Hydrangea")
    flower3.grow()
    flower3.bloom()
#Flowers 2 and 3 follow the same process as 1, but with the names "Daisy" and "Hydrangea" instead
if __name__ == "__main__":
  main()
#Allows the code to run

