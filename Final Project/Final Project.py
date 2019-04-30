from gamelib import*

game=Game(800,800,"BunnyGame",3)



#Background stuff
titlelogo=Image("Images//ai.png",game)
titlescreen=Image("Images//ts.png",game)
#ts=Image("
bs=Image("Images//blackscreen.jpg",game)
bg=Image("Images//forest1.png",game)
game.setBackground(bg)
titlescreen.resizeTo(game.width,game.height)
bg.resizeTo(805,805)
house=Image("Images//house.png",game)
house.moveTo(150,558)
house.resizeBy(-60)
bs.resizeTo(800,800)
ps=Image("Images//ps.png",game)
hb= Image("Images//rood box.png",game)



#Player stuff
playerL=Animation("Images//bunnyL.png",6,game,396/6,89)
playerR=Animation("Images//bunnyR.png",6,game,395/6,88)

player2r=Animation("Images//bunny2r.png",6,game,396/6,89)
player2r.resizeBy(100)
player2r.moveTo(400,300)

player2l=Animation("Images//bunny2l.png",6,game,395/6,88)
player2r=Animation("Images//bunny2r.png",6,game,396/6,89)

playerL.moveTo(150,550)
playerL.setSpeed(1,0)

playerR.moveTo(150,550)
playerR.setSpeed(1,0)

player2r.visible=True
player2l.visible=False
playerL.visible=False
playerR.visible=True

#Pooncake Stuff
pooncake=Image("Images//mr.pooncake.png",game)
pooncake.moveTo(400,500)
pooncake.resizeBy(-15)


#Goon stuff
goonL=Animation("Images//GoonL.png",9,game,2400/3,1800/3)
goonR=Animation("Images//GoonR.png",9,game,2400/3,1800/3)

goonL.resizeBy(-75)
goonR.resizeBy(-75)

goonL.setSpeed(1,0)

goonL.moveTo(1000,650)

goonL.visible=True
goonR.visible=False


f=Font(white,50,black)

#Jumping stuff/variables
Jumping=False
jumping=False
landed=False
Landed=False
factor=1
Factor=1
scrollx=(0)

hb.moveTo(goonL.x,goonL.y)
hb.resizeTo(goonL.x,goonL.y-30)


while not game.over:
    game.processInput()
    bs.draw()
    titlelogo.draw()

    game.drawText("Loading...",325,500,f)
    if game.time<1:
        game.over=True
    game.update(60)
    game.displayTime()

game.over=False


#TitleScreen
while not game.over:
    game.processInput()
    titlescreen.draw()
    ps.draw()    
    #pooncake.draw()
    if keys.Pressed[K_SPACE]:
        game.over=True
    if keys.Pressed[K_i]:
        titlescreen.visible=False
    if keys.Pressed[K_b]:
        titlescreen.vivible=True
    game.update(20)
                                                                     
game.over=False


#Game
while not game.over:
    game.processInput()
    bg.draw()
    game.scrollBackground("right",0)
    house.draw()
    hb.draw()
    playerR.draw()
    playerL.draw()
    goonL.draw()
    goonR.draw()

    if playerL.collidedWith(hb) or playerR.collidedWith(hb):
        goonL.visible=False
        goonR.visible=False

    if keys.Pressed == False:

        playerL.setSpeed = (0,0)
        playerR.setSpeed = (0,0)

    #PlayerMovement/Jump/Scrollx
    '''if player2r.y<650:
        Landed=False
    else:
        Landed=True
    if keys.Pressed[K_UP] and Landed and not Jumping:
        Jumping=True
    if Jumping:
        player2l.y -=27*Factor
        player2r.y -=27*Factor
        Factor*=.95
        Landed = False
    if Factor < .18:
            Jumping = False
            Factor = 1
    if not Landed:
        player2l.y+=10
        player2r.y+=10'''
    
#Fisrt Player
    if playerR.y<650:
        landed=False
    else:
        landed=True
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping=True
    if jumping:
        playerL.y -=27*factor
        playerR.y -=27*factor
        factor*=.95
        landed = False
    if factor < .18:
            jumping = False
            factor = 1
    if not landed:
        playerL.y+=10
        playerR.y+=10
    
    '''if keys.Pressed[K_LEFT]:
        game.scrollBackground("right",5)
        house.draw()
        house.moveTo(scrollx+150,558)
        player2r.visible=False
        player2l.visible=True
        playerR.visible=False
        playerL.visible=True
        player2l.draw()
        player2l.x-=5
        player2r.x-=5
        scrollx+=5

    if keys.Pressed[K_RIGHT]:
        game.scrollBackground("left",5)
        house.draw()
        house.moveTo(scrollx+150,558)
        player2r.visible=True
        player2l.visible=False
        playerL.visible=False
        playerR.visible=True
        player2r.draw()
        player2r.x+=5
        player2l.x+=5
        scrollx-=5'''



        
    if keys.Pressed[K_a]:
        game.scrollBackground("right",5)
        house.draw()
        playerR.visible=False
        playerL.visible=True
        '''player2r.visible=False
        player2l.visible=True'''
        house.moveTo(scrollx+150,558)
        goonL.moveTo(scrollx+1000,650)
        goonR.moveTo(scrollx+1000,650)
        goonL.draw()
        scrollx+=5
        playerL.draw()
    if keys.Pressed[K_d]:
        game.scrollBackground("left",5)
        house.draw()
        playerL.visible=False
        playerR.visible=True
        '''player2r.visible=True
        player2l.visible=False'''
        house.moveTo(scrollx+150,558)
        goonL.moveTo(scrollx+1000,650)
        goonR.moveTo(scrollx+1000,650)
        goonL.draw()
        scrollx-=5
        playerR.draw()

    #GoonLoganSmartness
    if playerR.x>goonL.x : #player2r.x>goonL.x:
        goonL.visible=False
        goonR.visible=True
    if playerL.x<goonR.x: #player2l.x>goonR.x:
        goonL.visible=True
        goonR.visible=False
        

        
        
    
        
    game.update(20)
game.quit()
    
