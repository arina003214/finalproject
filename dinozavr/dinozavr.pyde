kak=0
dino=0
puc=0
timer_up=0
timer_down=0
y=300
w=450
x=True
pause_x=490
pause_y=10
pause_w=100
pause_h=60
  
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

def setup():
    size(600,600)
    global kak,dino,puc
    puc=loadImage('fon.png')
    kak=loadImage('kaktyc.png')
    dino=loadImage('dinozavr.png')
    
def draw():
    global kak,dino,puc,y,timer_up,timer_down,w,x,pause_x,pause_y,pause_w,pause_h
    image(puc,0,0,600,600)
    image(kak,w,380,120,130)
    w = w - 5
    image(dino,10,y,160,200)
    noStroke()
    fill(250,190,50) 
    rect(0,500,600,100)
    fill(60,40,220)
   # кнопка пауза 
    rect(pause_x,pause_y,pause_w,pause_h)
    fill(255)
    textSize(30)
    text('pause',495,45)
    
    if timer_down > 0:
        timer_down = timer_down - 1
        y = y + 6
    if timer_up > 0:
        timer_up = timer_up - 1
        y = y - 6
        if timer_up == 0:
            timer_down = 40
    
    if w< 0:
        w=random(600,1000)
    if x==collideRectRect (10, y, 160, 160, w, 360, 150, 150):
        noLoop()
        background(255,0,0)
        textSize(80)
        fill(255)
        text('Game over!!',80,300)

def mouseClicked():
    global pause_x,pause_y,pause_w,pause_h
    if mouseX>490 and mouseX<590 and mouseY>10 and mouseY<70:
        noLoop()
        background(205,200,220)
        fill(90,80,140)
        rectMode(CENTER)
        rect(300,300,250,150)
        textSize(50)
        fill(255)
        text('farther',220,310)
    elif mouseX>300 and mouseX<550 and mouseY>300 and mouseY<450:
                
def keyPressed():
    global timer_up, timer_down,y
    if key == " " and timer_up == 0 and timer_down == 0:
        timer_up = 40
        
