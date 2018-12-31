##Create three dictionaries
##All three will have the same corresponding keys, but different values

def main():

        course1 = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'} 

        course2 = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'} 
        
        course3 = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'} 

        key_in = raw_input('Enter a course number:')

        if key_in in course1 and key_in in course2 and key_in in course3:
                print 'Room number:', course1[key_in]
                print 'Instructor:', course2[key_in]
                print 'Lecture timing:', course3[key_in]


main()

        
        

        
