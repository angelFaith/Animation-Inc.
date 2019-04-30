from gamelib import*#import game library
#objects/initial settings
game = Game (800,600,"Jumping Smurf")
bk = Image("bk.jpg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping


smurf = Animation("smurf_sprite.png",16,game,512/4,512/4)
smurf.moveTo(100,400)
smurf.stop()


while not game.over:
    game.processInput()
    
    bk.draw()
    smurf.draw()
    if smurf.y< 400:
        landed = False
    else:
        landed = True
   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True

    if jumping:
        smurf.y -=27*factor
        factor*=.95
        landed = False
        
        if factor < .18:
            jumping = False
            factor = 1
            
    if not landed: 
        smurf.y +=6
      




    if keys.Pressed[K_RIGHT]:
        smurf.nextFrame()
        smurf.x+=2
    if keys.Pressed[K_LEFT]:
        smurf.nextFrame()
       
        smurf.x-=2
        
   
    game.update(60)
game.quit()
