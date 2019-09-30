#coordenadas da tela
x = 800
y = 600

la = PVector(250,250)
lb = PVector(250,350)
lc = PVector(550,350)
ld = PVector(550,250)

def Menu():
    global estado
    
    background(0)
    rectMode(CENTER)
    
    textAlign(CENTER)
    textSize(30)
    text('MINIGOLF',width/2,100)
    
    textSize(20)
    noFill()
    stroke(255)
    
    text('New Game', width/2, 250)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 250+45 and mouseY >= 250-45:
        rect(width/2, 250,180,90)
    
    text('Credits', width/2, 400)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 400+45 and mouseY >= 400-45:
        rect(width/2, 400,180,90)
            
            
#definicao da bola
v = PVector(0,0) # vel = 1cm/ms
p = PVector(300,300) # proporção é de 1px = 1cm
r = 2 # diametro da bolinha oficial vale 40mm



#incrementos e verfificadores de movimento    
inc = PVector(0,0)     
ver = False


class Bola:
    def __init__(self,p,v,r):
        self.v = v.copy()
        self.p = p.copy()
        self.r = r
    def move(self,dt):
            self.p.add(self.v*dt)
    
    def xlr8(self,dt):
        v = self.v.copy()
        if v.mag() < 0.009:
            self.v.add(v.mult(-1))
        elif v.mag() < 0.1:
            mi = -0.3*v.mag()
            v.mult(mi)
            self.v.add(v)
        else:
            mi = -0.3*v.mag()**2
            v.mult(mi)
            self.v.add(v)
    
b = Bola(p.copy(),v.copy(),r)


def colide(b, s):
    s.normalize()
    vy = s*(b.v.dot(s))
    vx = b.v - vy

    
    vy = vy* (-1)
    b.p.add(2*vy)
    b.v = vx + vy


t = millis()


lados = [(la,lb),(lb,lc),(lc,ld),(ld,la)]
r2 = b.r**2

def detecta_colisao():
    global lados, b, r2
    
    for l in lados:
        p1 = l[0].copy()
        p2 = l[1].copy()
        p = p2-p1
        ball = b.p.copy()
        v1 = p.dot(ball-p1)
        v2 = p.dot(ball-p2)
        
        if v1 > 0 and v2 < 0:
            a_ = (ball-p1) - (v1/(v1-v2))*p
            if a_.x**2 + a_.y**2 <= r2:
                colide(b,a_)


def Minigolf():
    global estado, Menu, t, lados, b
        
    oldt = t
    t = millis()
    dt = t-oldt
    dt = 38
    background(122, 166, 56)
        
    rectMode(CORNERS)
    
    fill(255,255,255)
    stroke(255)
    rectMode(CENTER)
    text('Exit', 0.11*width, 50)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
        noFill()
        rect(0.11*width, 50, 0.2*width, 60)
                                                    
            
    b.move(dt)
    b.xlr8(dt)
    
    detecta_colisao()
    
    fill(255)
    stroke(255)
    ellipse(b.p.x,b.p.y, 2*b.r, 2*b.r)
    
    stroke(0)
    for i in lados:
        line(i[0].x,i[0].y,i[1].x,i[1].y)

posy = y-50

def Creditos():
    global posy, Menu, estado
    background(0)
    posx = width/2
    v = -3
    posy += v
    text("Minigolf: \n Isaque Vieira Machado Pim \n Igor Patricio Michels  \n \n Agradecimentos: \n Paulo Cesar \n Asla de Sa \n Coffee Machine do 14", posx, posy)
    if posy < -400:
        estado = Menu
        posy = y-50

    
    
    
estado = Menu

def setup():
    size(x, y)
    
def draw():
    global estado
    estado()
    
def mouseDragged():
    global inc, ver
    
    #if b.v.mag() == 0: #condição para não aceitar tacadas se a bola estiver se movendo
    if sqrt((mouseX - b.p.x)**2 + (mouseY-b.p.y)**2) <= r+10:
        ver = True
    
    if ver:
        inc.x = b.p.x - mouseX
        inc.y = b.p.y - mouseY
        stroke(255,0,0)
        line(b.p.x,b.p.y,mouseX,mouseY)

def mouseReleased():
    global inc, ver, estado, Minigolf
    if estado == Minigolf:
        if ver:
            b.v.add(inc/300)
            inc = PVector(0,0) 
            ver = False
            
def mouseClicked():
    global estado, Minigolf, Creditos, b, p, v, r
    if estado == Menu:
        if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 250+45 and mouseY >= 250-45:
                estado = Minigolf    
        if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 400+45 and mouseY >= 400-45:
                estado = Creditos
    if estado == Minigolf:
        if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
            estado = Menu
            b = Bola(p.copy(),v.copy(),r)
        
