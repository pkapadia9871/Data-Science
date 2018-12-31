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


class Information:

        def __init__(self,name,address,age,phone):
            self.__name = name
            self.__address = address
            self.__age = age
            self.__phone = phone
            
        def set_name(self,name):
            self.__name = name

        def set_address(self,address):
            self.__address = address

        def set_age(self,age):
            self.__age = age

        def set_phone(self,phone):
            self.__phone = phone
            
        def get_name(self):
            
            return self.__name
        
        def get_address(self):
            
            return self.__address
        
        def get_age(self):
            
            return self.__age
        
        def get_phone(self):
            
            return self.__phone

        def get_info():
            self._name = raw_input('Enter your name: ')
            self._address = raw_input('Enter your address: ')
            self._age = raw_input('Enter your age: ')
            self._phone = raw_input('Enter your phone number: ')



def main():

##Make three instances of the Information class:
##One for you, one for a family member, one for a friend
        

        print 'Type in your info: '
        my_info = Information()
        print 'Type in your family members info: '
        family_info = Information()
        print 'Type in your friends info: '
        friend_info = Information()



        

main()
