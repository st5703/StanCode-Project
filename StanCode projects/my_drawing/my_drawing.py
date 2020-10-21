"""
File: my-drawing
Name: Che-Hsien, Chiu
----------------------
TODO: drawing by campy graphics
"""

from campy.graphics.gobjects import GOval, GRect, GLine
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage

window = GWindow(width=1250,height=600)

def main():
    """
    TODO: drawing by campy graphics
    """
    sky()
    cloud()
    graze()
    ground1()
    rock()
    wood()
    ground2()
    moai()
    me()

    # reference picture
    real = GImage('real_image.png')
    window.add(real,x=800,y=0)



def sky():
    """
    sky drawing
    """
    sky = GRect(800,285,x=0,y=0)
    window.add(sky)
    sky.color = 'skyblue'
    sky.filled = True
    sky.fill_color = 'skyblue'


def wood():
    """
    wood drawing
    """
    dx = 0
    dy = 400

    while dx < 200:
        wood = GRect(30, 20, x=dx, y=dy)
        wood.color = 'brown'
        wood.filled = True
        wood.fill_color = 'brown'
        window.add(wood)
        dx += 20
        dy += 5

    dx = 200
    dy = 444

    while dx < 800:
        wood = GRect(100, 20, x=dx, y=dy)
        wood.color = 'brown'
        wood.filled = True
        wood.fill_color = 'brown'
        window.add(wood)
        dx += 100
        dy -= 3


def graze():
    """
    graze drawing
    """
    graze = GRect(800,315,x=0,y=285)
    graze.color = 'sage'
    graze.filled = True
    graze.fill_color = 'sage'
    window.add(graze)


def ground1():
    """
    ground 1 drawing
    """
    ground = GRect(800,20,x=0,y=285)
    ground.color = 'peru'
    ground.filled = True
    ground.fill_color = 'peru'
    window.add(ground)


def ground2():
    """
    ground 2 drawing
    """
    dx = 0
    dy = 445
    while dx < 200:
        ground = GRect(20,200,x = dx, y = dy)
        ground.color = 'peru'
        ground.filled = True
        ground.fill_color = 'peru'
        window.add(ground)
        dx += 20
        dy += 5

    dx = 200
    dy = 490
    while dx < 800:
        ground = GRect(20,200,x = dx, y = dy)
        ground.color = 'peru'
        ground.filled = True
        ground.fill_color = 'peru'
        window.add(ground)
        dx += 20
        dy -= 0.5



def me():
    """
    me drawing
    """

    face = GOval(40,50,x=250, y = 210)
    face.color = 'burlywood'
    face.filled = True
    face.fill_color = 'burlywood'
    window.add(face)

    L_eye = GLine(258,225,267,225)
    window.add(L_eye)

    R_eye = GLine(275, 225, 284, 225)
    window.add(R_eye)

    nose = GLine(271, 232, 268, 240)
    window.add(nose)

    nose = GLine(268, 240, 273,240)
    window.add(nose)

    mouse = GOval(10,10,x = 265, y =250)
    mouse.color = 'black'
    window.add(mouse)

    neck = GRect(15,13,x=264, y = 255)
    neck.color = 'burlywood'
    neck.filled = True
    neck.fill_color = 'burlywood'
    window.add(neck)

    body = GRect(70,120,x = 237, y = 285)
    body.color = 'navy'
    body.filled = True
    body.fill_color = 'navy'
    window.add(body)

    body = GOval(70,40,x = 237, y = 265)
    body.color = 'navy'
    body.filled = True
    body.fill_color = 'navy'
    window.add(body)

    body = GOval(30,100,x = 225, y = 276)
    body.color = 'navy'
    body.filled = True
    body.fill_color = 'navy'
    window.add(body)

    body = GOval(30,100,x = 288, y = 276)
    body.color = 'navy'
    body.filled = True
    body.fill_color = 'navy'
    window.add(body)


    dx = 237
    dy = 406
    for i in range(13):
        L_foot = GRect(30,10,x=dx, y = dy)
        L_foot.color = 'gray'
        L_foot.filled = True
        L_foot.fill_color = 'gray'
        window.add(L_foot)
        dx -=1
        dy+=10


    dx = 277
    dy = 406
    for i in range(13):
        L_foot = GRect(30,10,x=dx, y = dy)
        L_foot.color = 'gray'
        L_foot.filled = True
        L_foot.fill_color = 'gray'
        window.add(L_foot)
        dx +=1
        dy+=10

    shoe = GRect(30,30,x=224, y = 536)
    shoe.color = 'white'
    shoe.filled = True
    shoe.fill_color = 'white'
    window.add(shoe)

    shoe = GRect(30,30,x=290, y = 536)
    shoe.color = 'white'
    shoe.filled = True
    shoe.fill_color = 'white'
    window.add(shoe)

    tie = GLine(230,546, 250,546)
    window.add(tie)

    tie = GLine(230, 551, 250, 551)
    window.add(tie)

    tie = GLine(240, 540, 240, 560)
    window.add(tie)
#
    tie = GLine(300, 546, 320, 546)
    window.add(tie)

    tie = GLine(300, 551, 320, 551)
    window.add(tie)

    tie = GLine(310, 540, 310, 560)
    window.add(tie)

    hand = GLine(240,310,245,380)
    window.add(hand)

    hand = GLine(305,310,300,380)
    window.add(hand)

def cloud():
    """
    cloud drawing
    """
    cloud = GOval(100, 30, x=70, y=150)
    cloud.filled = True
    cloud.color = 'white'
    cloud.fill_color = 'white'
    window.add(cloud)

    cloud = GOval(100, 30, x=170, y=100)
    cloud.filled = True
    cloud.color = 'white'
    cloud.fill_color = 'white'
    window.add(cloud)

    cloud = GOval(100, 30, x=270, y=10)
    cloud.filled = True
    cloud.color = 'white'
    cloud.fill_color = 'white'
    window.add(cloud)

    cloud = GOval(100, 30, x=700, y=160)
    cloud.filled = True
    cloud.color = 'white'
    cloud.fill_color = 'white'
    window.add(cloud)

    cloud = GOval(100, 30, x=500, y=70)
    cloud.filled = True
    cloud.color = 'white'
    cloud.fill_color = 'white'
    window.add(cloud)


def moai():
    """
    moai drawing
    """
    moai = GOval(85,40,x = 470, y = 106)
    moai.color = 'darkgrey'
    moai.filled = True
    moai.fill_color = 'darkgrey'
    window.add(moai)

    moai = GRect(85,90,x = 470, y = 130)
    moai.color = 'darkgrey'
    moai.filled = True
    moai.fill_color = 'darkgrey'
    window.add(moai)

    moai_eye = GOval(35,25,x = 475, y = 125)
    moai_eye.color = 'black'
    moai_eye.filled = True
    moai_eye.fill_color = 'dimgray'
    window.add(moai_eye)

    moai_eye = GOval(35, 25, x=515, y=125)
    moai_eye.color = 'black'
    moai_eye.filled = True
    moai_eye.fill_color = 'dimgray'
    window.add(moai_eye)

    moai_nose = GLine (510,150,505,185)
    window.add(moai_nose)
    moai_nose = GLine (516,150,521,185)
    window.add(moai_nose)
    moai_nose = GLine(505, 185, 521, 185)
    window.add(moai_nose)

    moai_mouse = GOval(70, 40, x=477, y=195)
    moai_mouse.color = 'black'
    window.add(moai_mouse)

    moai = GRect(70,15,x=477,y = 205)
    moai.color = 'darkgrey'
    moai.filled = True
    moai.fill_color = 'darkgrey'
    window.add(moai)


    moai = GOval(135,100,x = 445, y = 210)
    moai.color = 'darkgrey'
    moai.filled = True
    moai.fill_color = 'darkgrey'
    window.add(moai)

    moai = GRect(132,160,x = 447, y = 250)
    moai.color = 'darkgrey'
    moai.filled = True
    moai.fill_color = 'darkgrey'
    window.add(moai)

    moai_L = GLine(460,280,463,410)
    window.add(moai_L)

    moai_R = GLine(567,280,564,410)
    window.add(moai_R)


def rock():
    """
    rock drawing
    """
    rock = GRect(800,15,x=0, y= 370)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)
    rock = GRect(50,40,x = 750, y = 360)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)
    rock = GRect(50,40,x = 700, y = 355)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)
    rock = GRect(50, 40, x=650, y=350)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)

    rock = GRect(40, 20, x=20, y=400)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)

    rock = GRect(40, 40, x=40, y=380)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)

    rock = GRect(40, 60, x=60, y=360)
    rock.color = 'dimgray'
    rock.filled = True
    rock.fill_color = 'dimgray'
    window.add(rock)

if __name__ == '__main__':
    main()
