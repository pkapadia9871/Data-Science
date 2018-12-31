##Class: Pet
## Attributes: name, animal type, age
##Needs init_ method that creates these attributes
##Methods: set_(name, age, animal_type), get(name, type, age)

##Once you have written the class, write a program that creates an
##object of the class and prompts the user to enter the name, type,
##and age of his or her pet. This data should be
##stored as the object’s attributes.
##Use the object’s accessor methods to retrieve the pet’s name,
##type, and age and display this data on the screen.


class Pet:

        def __init__(self,name,animal,age):
            self.__name = name
            self.__animal = animal
            self.__age = age

        def set_name(self,name):
            self.__name = name

        def set_animal(self,animal):
            self.__animal = animal

        def set_age(self,age):
            self.__age = age
            
        def get_name(self):
            return self.__name
        def get_animal(self):
            return self.__animal
        def get_age(self):
            return self.__age


def main():

        
        pet_name = raw_input('What is the name of the pet? ' )
        pet_animal = raw_input('What is the animal of the pet? ')
        pet_age = raw_input('What is the age of the pet? ')

        my_pet = Pet(pet_name,pet_animal,pet_age)

        print 'The name of your pet is: ', my_pet.get_name()
        print 'The animal of your pet is: ', my_pet.get_animal()
        print 'The age of your pet is: ', my_pet.get_age()


main()
