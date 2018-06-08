from random import randint
from gpiozero import LED, Button
from time import sleep

#pinout for LEDs in order red, blue, green, yellow
rbgy = [LED(22), LED(23), LED(17), LED(18)]

#pinout for buttons corresponding to LEDs in same order
button = [Button(13), Button(6), Button(12), Button(5)]

rbgy[3].on()              #the yellow LED is made to blink only to alert the user
sleep(0.2)                #that the game is now ready to be played
rbgy[3].off()

#This infinite while loop allows the game to be played an infinite amount of times without the need to
#restart the machine
while True:
        series_length = 1 #starting length for the game

        paused = True     #the game is considered 'paused' until it has been started

        while paused:
                if button[0].is_pressed and button[1].is_pressed and button[2].is_pressed and button[3].is_pressed:
                        paused = False
        for i in range(0,16):
                rbgy[i%4].on()    #the modular arithmetic in conjunction with the
                sleep(0.1)        #range from 0-16 allows the LED sequence to
                rbgy[i%4].off()   #repeat four times
        sleep(1)

        counter = 0       #counts successes; used in determining when to increase
                          #series_length
        playing = True    #while this variable is True, the player may continue
                          #to 'level-up'

        #the entire game takes place within this while loop
        while playing:
                sequence = []
                repeat = []

                for i in range(series_length):
                        r = randint(0,3)
                        sequence.append(r)
                        rbgy[r].on()
                        for j in range(0,4):
                                if j != r:
                                        rbgy[j].off()
                        sleep(1)
                        rbgy[r].off()
                        sleep(0.1)

                while len(repeat) < series_length:
                        for j in range(0,4):
                                if button[j].is_pressed:
                                        repeat.append(j)
                                        button[j].when_pressed = rbgy[j].on()
                                        sleep(0.5)
                                        button[j].when_released = rbgy[j].off()
                sleep(0.5)
                if sequence == repeat:
                        for i in range(0,5):
                                rbgy[2].on()
                                sleep(0.2)
                                rbgy[2].off()
                                sleep(0.2)
                        counter += 1
                else:
                        for i in range(0,5):
                                rbgy[0].on()
                                sleep(0.2)
                                rbgy[0].off()
                                sleep(0.2)
                        playing = False

                if counter == 2:
                        for i in range(0,8):
                                rbgy[i%4].on()   #the modular arithmetic in conjunction
                                sleep(0.1)       #with the range from 0-8 allows the LED
                                rbgy[i%4].off()  #sequence to repeat twice
                        series_length += 1
                        counter = 0
                sleep(1)


