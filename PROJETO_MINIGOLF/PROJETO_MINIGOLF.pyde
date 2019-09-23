#coordenadas da tela
x = 800
y = 800

la = PVector(200,200)
lb = PVector(200,500)
lc = PVector(300,600)
ld = PVector(600,600)
le = PVector(600,500)
lf = PVector(400,500)
lg = PVector(400,200)

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
    
    text('New Game', width/2, 300)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 300+45 and mouseY >= 300-45:
        rect(width/2, 300,180,90)
        if mousePressed == True:
            estado = Minigolf
    
    text('Credits', width/2, 500)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 500+45 and mouseY >= 500-45:
        rect(width/2, 500,180,90)
        if mousePressed == True:
            estado = Creditos
            
            
            
            
            
            
            
#definicao da bola
v = PVector(0,0)
p = PVector(300,300)
r = 10




#incrementos e verfificadores de movimento    
inc = PVector(0,0)     
ver = False

class Bola:
    def __init__(self,p,v,r):
        self.v = v
        self.p = p
        self.r = r
    def move(self,dt):
        self.p.add(self.v*dt)

    def xlr8(self,dt):
        v = self.v.copy()
        if v.mag() < 0.005:
            self.v.add(v.mult(-1))
        elif v.mag() < 0.1:
            mi = -0.3*v.mag()
            v.mult(mi)
            self.v.add(v)
        else:
            mi = -0.09*v.mag()**2
            v.mult(mi)
            self.v.add(v)

    
        


b = Bola(p,v,r)

def colide(b, s):
    
    vy = s*(b.v.dot(s))
    vx = b.v - vy

    
    vy = vy* (-1)
    
    b.v = vx + vy


t = millis()
xmin = ymin = 200
xmax = ymax = 600

lados = [(la,lb),(lb,lc),(lc,ld),(ld,le),(le,lf),(lf,lg),(lg,la)]
def detecta_colisao():
    global lados, b
    
    for l in lados:
        p1 = l[0].copy()
        p2 = l[1].copy()
        d = dist(p1.x,p1.y,p2.x,p2.y)
        p = (p2-p1).normalize()
        n = PVector(-p.y,p.x)
        ball = b.p.copy()
        v = n*(n.dot(ball-p1))
        
        if v.mag() <= b.r:
            v1 = p*(p.dot(ball-p1))
            v2 = p*(p.dot(ball-p2))
            
            if v1.mag() + v2.mag() <= d:
                colide(b, n)

def Minigolf():
    global estado, Menu, t, xmin, xmax, ymin, ymax, lados
    
    oldt = t
    t = millis()
    dt = t-oldt
    
    background(0)
    rectMode(CORNERS)
    noFill()
    stroke(255)
    #rect(xmin,ymin,xmax,ymax)
    
    b.move(dt)
    b.xlr8(dt)
    
    #if b.p.x <= xmin+b.r:
        #colide(b, PVector(1,0))
    #elif b.p.x >= xmax-b.r:
        #colide(b, PVector(-1,0))
        
    #if b.p.y <= ymin+b.r:
        #colide(b, PVector(0,1))
    #elif b.p.y >= ymax-b.r:
        #colide(b, PVector(0,-1))
    detecta_colisao()
    
    fill(255)
    stroke(255)
    ellipse(b.p.x,b.p.y, 2*b.r, 2*b.r)
    
    for i in lados:
        line(i[0].x,i[0].y,i[1].x,i[1].y)
    
    #noFill()
    #stroke(255)
    #ellipse(b.p.x,b.p.y, 2*b.r+20, 2*b.r+20)
    
    rectMode(CENTER)
    text('Exit', 0.2*width, 50)
    if mouseX <= 0.2*width + 0.1*width and mouseX >= 0.2*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
        rect(0.2*width, 50, 0.2*width, 60)
        if mousePressed == True:
            estado = Menu

    
    

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
    
    if b.v.mag() == 0: #condição para não aceitar tacadas se a bola estiver se movendo
        if sqrt((mouseX - b.p.x)**2 + (mouseY-b.p.y)**2) <= r+10:
            ver = True
    
        if ver:
            inc.x = b.p.x - mouseX
            inc.y = b.p.y - mouseY
            stroke(255,0,0)
            line(b.p.x,b.p.y,mouseX,mouseY)

def mouseReleased():
    global inc, ver
    if ver:
        b.v.add(inc/500)
        inc = PVector(0,0) 
        ver = False
