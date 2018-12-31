##In a particular factory, a shift supervisor is a salaried employee who
##supervises a shift. In addition to a salary, the shift supervisor earns a
#yearly bonus when his or her shift meets production goals.
##Write a ShiftSupervisor class that is a subclass of the Employee class
##you created in Programming Exercise 1.
##The ShiftSupervisor class should keep a data attribute for the annual
##salary and a data attribute for the annual production bonus that a shift
##supervisor has earned.
##Demonstrate the class by writing a program that uses a ShiftSupervisor object.

class Employee:

    def __init__(self, salary):
        self._salary = salary

    def set_salary(self,salary):
        self._salary = salary

    def get_salary(self):
        return self._salary



class ShiftSupervisor(Employee):

    def __init__(self,salary,bonus):

        Employee.__init__(self,salary)

        self._bonus = bonus

    def set_bonus(self,bonus):
        self._bonus = bonus

    def get_bonus(self):
        return self._bonus


def main():

    shift_guy = ShiftSupervisor(4500, 275)

    print 'Salary = $', shift_guy.get_salary()
    print 'Bonus = $', shift_guy.get_bonus()

main()
        
