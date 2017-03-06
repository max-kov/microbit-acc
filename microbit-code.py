from microbit import *
import random

name = 'test'+str(random.randint(1,100))+'.txt'

with open(name, 'w') as myFile:
    myFile.write('timestamp X Y Z \n')
    display.scroll('R')
    while not button_b.is_pressed():
        myFile.write(str(running_time())+' '+str(accelerometer.get_x())+' '+str(accelerometer.get_y())+' '+str(accelerometer.get_z())+'\n')
    display.scroll('D')