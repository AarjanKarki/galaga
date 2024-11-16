import pgzrun
WIDTH=500
HEIGHT=500

game_over=False
score=0

galaga=Actor('galaga')
galaga.pos=(WIDTH//2, HEIGHT-60)
bullets=[]
speed=5

def draw():
    screen.clear()
    screen.fill('blue')
    for bullet in bullets:
        bullet.draw()
    galaga.draw()

def update():
    if keyboard.left:
        galaga.x-=2
        if galaga.x<0:
            galaga.x=10
    if keyboard.right:
        galaga.x+=2
        if galaga.x>WIDTH:
            galaga.x=WIDTH-10
    for bullet in bullets:
        bullet.y-=10

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=galaga.x
        bullets[-1].y=galaga.y-20




pgzrun.go()