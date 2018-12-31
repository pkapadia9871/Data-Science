def main():

        m = input('Enter the mass in kg: ')
        v = input('Enter the velocity in m/s: ')

        e = kinetic_energy(m,v)
        print 'The kinetic energy in joules = ', e , ' J' 
        

def kinetic_energy(m,v):
    return (m * v * v / 2)

main()
