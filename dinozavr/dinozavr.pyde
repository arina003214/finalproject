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
mode=1
q=380
p=0

  
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

def setup():
    
    size(600,600)
    global kak,dino,puc,mode
    puc=loadImage('fon.png')
    kak=loadImage('kaktyc.png')
    dino=loadImage('dinozavr.png')
    
    
def draw():
    global p,kak,dino,puc,y,timer_up,timer_down,w,x,pause_x,pause_y,pause_w,pause_h,mode,q
    
    if mode==1:
        image(puc,0,0,600,600)
        image(kak,w,q,120,130)
        
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
        if p>5:
            w=w-5.5
        if p>10:
            w=w-6
        
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
            p=p +1
        if x==collideRectRect (10, y, 160, 160, w, 360, 150, 150):
            noLoop()
            background(255,0,0)
            textSize(80)
            fill(255)
            text('Game over!!',80,300)
    else:
        fill(90,80,140)
        rect(170,230,250,150)
        textSize(50)
        fill(255)
        textSize(50)
        text('Continue',190,320)
    fill(50,10,210)
    textSize(30)
    text(p,20,40)    
def mouseClicked():
    global pause_x,pause_y,pause_w,pause_h,mode
    if mouseX>490 and mouseX<590 and mouseY>10 and mouseY<70:
        # noLoop()
       
        
    
        mode=0 
    elif mouseX>170 and mouseX<420 and mouseY>230 and mouseY<380:
        mode=1
        
        
            
            



       
                
  
        
def keyPressed():
    global timer_up, timer_down,y
    if key == " " and timer_up == 0 and timer_down == 0:
        timer_up = 40
        
