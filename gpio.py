from gpiozero import Button
from time import sleep

button4 = Button(4)
button17 = Button(17)
button18 = Button(18)
button27 = Button(27)
button22 = Button(22)
button23 = Button(23)
button24 = Button(24)
button25 = Button(25)
while True:
    
    if button4.is_pressed:
        print("4 Pressed pin7")
    elseif button17.is_pressed:
        print("17 Pressed pin 11")
    elseif button18.is_pressed:
        print("18 Pressed pin 12")
    elseif button27.is_pressed:
        print("27 Pressed pin 13")
    elseif button22.is_pressed:
        print("22 Pressed pin 15")
    elseif button23.is_pressed:
        print("23 Pressed pin 16")
    elseif button24.is_pressed:
        print("24 Pressed pin 18")
    elseif button25.is_pressed:
        print("25 Pressed pin 22")
    else:
        print("Released")
    sleep(1)
