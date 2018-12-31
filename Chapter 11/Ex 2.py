class Car:

        def __init__(self,year_model, make, speed):
            self.__year_model = year_model
            self.__make = make
            self.__speed = speed

        def set_year_model(self, year_model):
            self.__year_model = year_model

        def set_make(self,make):
            self.__make = make

        def set_speed(self,speed):
            self.__speed = speed

        def get_year_model(self):
            return self.__year_model
        
        def get_make(self):
            return self.__make

        def get_speed(self):
            return self.__speed
    
        def accelerate(self):
            self.__speed += 5
            
        def brake(self):
            self.__speed -= 5
            
        def get_speed(self):
            return self.__speed


def main():
        
        car_model = raw_input('What is the year model of the car? ' )
        car_make = raw_input('What is the make of the car? ')
        car_speed = 0
        print('At the start, the speed of the car is 0.')

        my_car = Car(car_model,car_make,car_speed)

        print 'The year model of your car is: ',my_car.get_year_model()
        print 'The make of your car is: ', my_car.get_make()
        

        for i in range(5):
            my_car.accelerate()
            print 'The current speed of your car is: ', my_car.get_speed()
            
        for i in range(5):
            my_car.brake()
            print 'The current speed of your car is: ', my_car.get_speed()

main()
