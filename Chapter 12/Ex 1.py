
class Employee:

    def __init__(self, name, number):
        self._name = name
        self._number = number
        
    def set_name(self,name):
        self._name = name

    def set_number(self,number):
        self._number = number

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

class ProductionWorker(Employee):

    def __init__(self,name,number,shift_no,pay_rate):

        Employee.__init__(self,name,number)

        self._shift_no = shift_no
        self._pay_rate = pay_rate

    def set_shift_no(self,shift_no):
        self._shift_no = shift_no

    def set_pay_rate(self,pay_rate):
        self._pay_rate = pay_rate

    def get_shift_no(self):
        return self._shift_no

    def get_pay_rate(self):
        return self._pay_rate


def main():

    my_name = raw_input('Enter the name of the employee: ')
    my_number = raw_input('Enter the number of the employee: ')
    my_shift_no = input('Enter the shift number of the employee: ')
    my_pay_rate =  input('Enter the pay rate of the employee: $')

    prodwo = ProductionWorker(my_name,my_number,my_shift_no,my_pay_rate)

    print 'Name of the employee = ', prodwo.get_name()
    print 'Number of the employee = ', prodwo.get_number()
    print 'Shift number of the employee = ', prodwo.get_shift_no()
    print 'Pay rate of the employee = $%.2f' % prodwo.get_pay_rate()


main()
        
