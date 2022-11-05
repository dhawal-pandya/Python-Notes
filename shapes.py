from turtle import *
import math

angle = 0
radius = (180 / math.pi)
granularity = 5
speed(0)

def move_with_angle(degree):
    counter = degree
    while(counter > 0):
        right(granularity)
        forward(granularity)
        counter -= granularity

def make_dot():
    spikes = 8
    while(spikes > 0):
        forward(5 + 5 * (1 - spikes % 2))
        backward(5 + 5 * (1 - spikes % 2))
        right(45)
        spikes -= 1

def make_quarter():
    left(135)
    penup()
    forward(radius)
    right(90)
    pendown()
    move_with_angle(90)
    right(90)
    penup()
    forward(radius)
    right(225)
    pendown()

def make_semi():
    make_dot()
    left(90)
    penup()
    forward(radius)
    right(90)
    pendown()
    move_with_angle(180)
    right(90)
    penup()
    forward(radius)
    left(90)
    pendown()

def make_paune():
    make_dot()
    left(135)
    penup()
    forward(radius)
    right(90)
    pendown()
    move_with_angle(270)
    right(90)
    penup()
    forward(radius)
    left(135)
    pendown()

def make_side():
    make_dot()
    make_quarter()
    right(180)
    make_quarter()
    right(180)

def cross_jump():
    penup()
    forward(radius * math.sqrt(2))
    pendown()

def jump():
    penup()
    forward(radius)
    pendown()

def make_cross():
    spikes = 4
    right(45)
    while(spikes > 0):
        forward(radius)
        penup()
        backward(radius)
        right(90)
        pendown()
        spikes -= 1
    left(45)

def make_worm(n):
    if n > 3:
        n = 3
    else:
        n = 2

    result = ""
    start = "82826"
    r = n - 2
    repeat_one = ("8784" * r)
    mid = "8786"
    repeat_two = ("88" * r )
    end = "8828181"
    result = start + repeat_one + mid + repeat_two + end
    return result

def make_border(n):
    # n = 3

    result = ""
    r = n - 2
    start = ("88" * ((n - 1)//2))
    mid_one = "2"
    repeat_one = ("4878" * ((n - 1)//2))
    mid_two = "a5a"
    repeat_two = ("8784" * ((n - 3)//2))
    mid_three = "8782"
    repeat_three = ("88" * ((n - 1)//2))
    end = "22"
    result = start + mid_one + repeat_one + mid_two + repeat_two + mid_three + repeat_three + end
    return result



# kolamcode = "68781878688187868818786"
# kolamcode_four_times = "4878b5b878"
# kolamcode = "82855282822"
# kolamcode = "8226878618168786188181"
# kolamcode = "9292687848784878688888829191"
# kolamcode = "8824878a5a87828822"
# kolamcode = "8888248784878a5a87848782888822"
kolamcode = make_border(5)+ "1" + make_worm(3) 

for _ in range(4):
    make_dot()
    for c in kolamcode:
        match c:
            case "a":
                right(45)
            case "b":
                left(45)
            case "1":
                right(90)
            case "2":
                left(90)
            case "3":
                make_quarter()
            case "4":
                make_side()
            case "5":
                make_semi()
            case "6":
                make_paune()
            case "7":
                make_cross()
            case "8":
                cross_jump()
            case "9":
                jump()
            case _:
                print("Error, instructions unclear. Hacked NASA instead.")


penup()
while(True):
    forward(100)