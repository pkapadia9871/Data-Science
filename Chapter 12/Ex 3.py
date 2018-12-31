##Write a class named Person with data attributes for a
##person’s name, address, and telephone number.
##Next, write a class named Customer that is a subclass of the Person class.
##The Customer class should have a data attribute for a customer number and a
##Boolean data attribute indicating whether the customer wishes to be on a
##mailing list. Demonstrate an instance of the Customer class in a simple
##program.



class Person:

    def __init__(self, name, address, tel_no):
        self._name = name
        self._address = address
        self._tel_no = tel_no
        
    def set_name(self,name):
        self._name = name

    def set_address(self,address):
        self._address = address

    def set_tel_no(self,tel_no):
        self._tel_no = tel_no

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_tel_no(self):
        return self._tel_no


class Customer(Person):

    def __init__(self,name,address,tel_no,cust_no,wish):

        Person.__init__(self,name,address,tel_no)

        self._cust_no = cust_no
        self._wish = wish

    def set_cust_no(self,cust_no):
        self._cust_no = cust_no 

    def set_wish(self,wish):
        self._wish = wish 

    def get_cust_no(self):
        return self._cust_no

    def get_wish(self):
        return self._wish

def main():

    his_name = raw_input ('Enter the name : ')
    his_address = raw_input ('Enter the address : ')
    his_tel_no = raw_input ('Enter the telephone number : ')
    his_cust_no = raw_input ('Enter the customer number : ')
    his_wish = raw_input ('Enter the wish (yes) or (no) : ')        
    
    customer_guy = Customer(his_name,his_address,his_tel_no,his_cust_no,his_wish)

    print 'Name : ', customer_guy.get_name()
    print 'Address : ', customer_guy.get_address()
    print 'Telephone number : ', customer_guy.get_tel_no()
    print 'Customer number : ', customer_guy.get_cust_no()
    print 'Wish : ', customer_guy.get_wish()

main()
        
