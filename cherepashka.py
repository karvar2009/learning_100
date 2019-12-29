from turtle import *

c = Turtle()
c.shape('turtle')
c.color('BLUE')
c.pensize(2)


def d(picsel):
 c.fd(picsel)


def r(gradusr):
 c.rt(gradusr)


def l(gradusl):
 c.lt(gradusl)


def up():
 c.penup()


def down():
 c.pendown()


def a_letter():
     down()
     l(90)
     r(45)
     d(50)
     r(90)
     d(50)
     r(180)
     d(30)
     r(320)
     d(25)
     up()
     d(-25)
     r(-320)
     d(-30)
     r(-180)
     r(-45)
     d(40)


def b_letter ():
    down()
    r(-90)
    d(40)
    for k in range (1,71):
        d(1)
        r(4)
    r(180)
    for p in range (1,71):
        d(1)
        r(4)
    r(85)
    up()
    d(80)


def c_letter():
    down()
    r(180)
    for g in range (1,60):
        d(1)
        r(3)
    up()
    r(90)
    d(20)
    l(90)
    d(50)



def d_letter ():
    l(90)
    down()
    d(40)
    r(90)
    for gg in range (1,61):
        d(1)
        r(3)
    up()
    l(180)
    d(70)
    l(90)
    d(10)
    r(90)


def e_letter ():
    down()
    r(180)
    for g in range (1,81):
        d(1)
        r(3)
    r(105)
    d(40)
    up()
    l(90)
    d(10)
    l(90)
    d(80)
    r(7)
def f_letter ():
    down()
    l(90)
    d(20)
    r(90)
    d(20)
    d(-20)
    l(90)
    d(20)
    r(90)
    d(18)
    up()
    r(90)
    d(30)
    l(90)
    d(40)



def g_letter ():
    l(90)
    d(40)
    l(90)
    down()
    for g in range (1,91):
        d(1)
        l(3)
    l(90)
    d(20)
    up()
    r(180)
    d(60)



def h_letter ():
    down()
    l(90)
    d(20)
    r(90)
    d(15)
    r(180)
    d(15)
    r(90)
    d(20)
    r(90)
    up()
    d(15)
    r(90)
    down()
    d(40)
    l(90)
    up()
    d(40)
    l(90)
    d(10)
    r(90)




def i_letter ():
    down()
    l(90)
    d(25)
    up()
    d(14)
    down()
    d(1)
    up()
    r(180)
    d(30)
    l(90)
    d(40)



def j_letter ():
    up()
    d(20)
    l(90)
    d(40)
    down()
    r(180)
    d(25)
    for ggg in range (1,31):
        d(1)
        r(5)
    r(110)
    up()
    d(45)
    l(90)
    d(5)
    r(93)





up()
d(-300)
down()
a_letter()
b_letter()
c_letter()
d_letter()
e_letter()
f_letter()
g_letter()
h_letter()
i_letter()
j_letter()
done()