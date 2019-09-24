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

v0 = PVector(0,0)
p0 = PVector(300,300)
r0 = 10


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

    def xlr8(self,dt,at=False):
        v = self.v.copy()
        if at == False:
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
        else:
            if v.mag() < 0.01:
                self.v.add(v.mult(-1))
            elif v.mag() < 0.2:
                mi = -0.5*v.mag()
                v.mult(mi)
                self.v.add(v)
            else:
                mi = -0.5*v.mag()**2
                v.mult(mi)
                self.v.add(v)
        
at = False
b = Bola(p,v,r)
b0 = Bola(p0,v0,r0)


class Obstaculo:
    def __init__(self):
        pass

    def obstaculo1(self, px, py, x, y):
        #definir cores ainda
        #ver equações das elipses para ver a tangente
        self.px = px
        self.py = py
        
        fill(242, 141, 53)    
        rect(px, py, x, y)
    
        fill(0)
        ellipse(px + 0.5*x, py + 0.5*y, 1.5*x, 0.5*y)
        #ellipse 1

        fill(242, 141, 53)
        ellipse(px + 0.5*x, py + 0.5*y, x, 0.25*y)
        #ellipse 2
        
        self.a21 = (1.5*x)**2 + (0.5*y)**2
        self.b21 = (0.5*y)**2
        #dados da ellipse 1
        
        self.a22 = (x)**2 + (0.25*y)**2
        self.b22 = (0.25*y)**2
        #dados da ellipse 2
        
    def obstaculo2(self, px, py, x, y):
        #definir cores ainda
        #equações
        self.px = px
        self.py = py
                
        fill(0, 0, 0)
        translate(px, py)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg1x = x/cos(PI/7.0)
        tg1y = y/sin(PI/7.0)
        self.tg1 = PVector(tg1x, tg1y)
        
        fill(127, 0, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg2x = x/cos(2*PI/7.0)
        tg2y = y/sin(2*PI/7.0)
        self.tg2 = PVector(tg2x, tg2y)
        
        fill(255, 0, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg3x = x/cos(3*PI/7.0)
        tg3y = y/sin(3*PI/7.0)
        self.tg3 = PVector(tg3x, tg3y)
        
        fill(0, 127, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg4x = x/cos(4*PI/7.0)
        tg4y = y/sin(4*PI/7.0)
        self.tg4 = PVector(tg4x, tg4y)
        
        fill(0, 255, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg5x = x/cos(5*PI/7.0)
        tg5y = y/sin(5*PI/7.0)
        self.tg5 = PVector(tg5x, tg5y)
        
        fill(0, 0, 127)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg6x = x/cos(6*PI/7.0)
        tg6y = y/sin(6*PI/7.0)
        self.tg6 = PVector(tg6x, tg6y)
        
        fill(0, 0, 255)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg7x = x/cos(PI)
        tg7y = y/sin(PI)
        self.tg7 = PVector(tg7x, tg7y)
        
    def obstaculo3(self, pxi, pyi, pxo, pyo, x, y):
        #buraco negro
        #entra num ponto e sai em outro com mesma velocidade, aceleração e direção
        self.pxi = pxi
        self.pyi = pyi
        self.pxo = pxo
        self.pyo = pyo
        
        stroke(0, 0, 255)
        fill(0)
        ellipse(pxi, pyi, x, y)
        
        stroke(255, 0, 0)
        fill(0)
        ellipse(pxo, pyo, x, y)

    def obstaculo4(self, px, py, x, y):
        #lago
        #caso a bolinha entre aqui, ela volta para o ponto em que saiu
        self.px = px
        self.py = py
        
        ellipse(px, py, x, y)
        ellipse(px, py, x/2, y/2)
        
    def obstaculo5(self, px, py, x, y):
        #areia
        #aumenta a força necessária para a bolinha se mover
        self.px = px
        self.py = py
        
        fill(242, 188, 121)
        noStroke()
        ellipse(px, py, 3*x/2, y)
        self.a2 = (1.5*x)**2 + (0.5*y)**2
        self.b2 = (0.5*y)**2
        #dados da ellipse
        
o = Obstaculo()

def colide(b, s):
    s.normalize()
    vy = s*(b.v.dot(s))
    vx = b.v - vy

    
    vy = vy* (-1)
    b.p.add(2*vy)
    b.v = vx + vy


t = millis()


lados = [(la,lb),(lb,lc),(lc,ld),(ld,le),(le,lf),(lf,lg),(lg,la)]
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
    global estado, Menu, t, lados, b, b0, p0, v0, r0, o, at
        
    oldt = t
    t = millis()
    dt = t-oldt
    dt = 38
    background(122, 166, 56)
    o.obstaculo5(300,500,70,120)
    
    rectMode(CORNERS)
    
    fill(255,255,255)
    stroke(255)
    rectMode(CENTER)
    text('Exit', 0.11*width, 50)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
        noFill()
        rect(0.11*width, 50, 0.2*width, 60)
        if mousePressed == True:
            estado = Menu
            b = b0
            b0 = Bola(p0,v0,r0)
                
    print(o.px)
    if (p.x-o.px)**2/o.a2 + (p.y-o.py)**2/o.b2 <=1:
        at = True
    else:
        at = False
    
    b.move(dt)
    b.xlr8(dt, at)
    
    
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
    
    stroke(0)
    for i in lados:
        line(i[0].x,i[0].y,i[1].x,i[1].y)
    
    #ellipse(b.p.x,b.p.y, 2*b.r+20, 2*b.r+20)


    
    

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
    global inc, ver
    if ver:
        b.v.add(inc/500)
        inc = PVector(0,0) 
        ver = False
        
