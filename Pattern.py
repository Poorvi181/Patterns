import pgzrun,random
TITLE="Pattern"
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("black")
    width=WIDTH
    height=HEIGHT-300
    r=255
    g=0
    b=random.randint(100,255)
    '''
    screen.draw.line((50,200),(350,200),(0,0,255))
    screen.draw.circle((200,200),50,(0,0,255))
    screen.draw.filled_circle((200,200),50,(0,0,255))'''
    for i in range(40):
        rect=Rect((0,0),(width,height))
        rect.center=200,200
        screen.draw.rect(rect,(r,g,b))
        width-=10
        height+=10
        r-=10


    

    












pgzrun.go()
