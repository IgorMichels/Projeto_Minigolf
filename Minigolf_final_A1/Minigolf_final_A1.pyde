#coordenadas da tela
x = 800
y = 600

#lista de lados menu
la = PVector(105,135)
lb = PVector(105,405)
lc = PVector(105,485)
ld = PVector(245,485)
le = PVector(245,565)
lf = PVector(695,565)
lg = PVector(695,485)
lh = PVector(695,135)
li = PVector(295,135)
lj = PVector(295,175)
lk = PVector(295,225)
ll = PVector(605,225)
lm = PVector(605,475)
ln = PVector(335,475)
lo = PVector(295,395)
lp = PVector(195,395)
lq = PVector(195,355)
lr = PVector(195,135)
lados_menu = [(la,lb),(lb,lc),(lc,ld),(ld,le),(le,lf),(lf,lg),(lg,lh),(lh,li),(li,lj),(lj,lk),(lk,ll),(ll,lm),(lm,ln),(ln,lo),(lo,lp),(lp,lq),(lq,lr),(lr,la)]

#lista de lados da fase teste
ta = PVector(250,250)
tb = PVector(250,350)
tc = PVector(550,350)
td = PVector(550,250)

lados1 = [(ta,tb),(tb,tc),(tc,td),(td,ta)]
buraco = [PVector(500,300), 7]

#lista de lados e figuras da fase com rampas
pa = PVector(150,255)
pb = PVector(150,345)
pc = PVector(650,345)
pd = PVector(650,255)

ret_r1 = (PVector(300,255), 50, 90)
ret_r2 = (PVector(450,255), 50, 90)

lados_r = [(pa,pb),(pb,pc),(pc,pd),(pd,pa)]
buraco_r = [PVector(630,300), 7]

# lista de lados fase michels 1
ma = PVector(100,255)
mb = PVector(400,255)
mc = PVector(400,155)
md = PVector(490,155)
me = PVector(490,255)
mf = PVector(590,255)
mg = PVector(617.5,255-55/2*3**(1/2))
mh = PVector(672.5,255-55/2*3**(1/2))
mi = PVector(700,255)
mj = PVector(700,345)
mk = PVector(672.5,345+55/2*3**(1/2))
ml = PVector(617.5,345+55/2*3**(1/2))
mm = PVector(590,345)
mn = PVector(490,345)
mo = PVector(490,445)
mp = PVector(400,445)
mq = PVector(400,345)
mr = PVector(100,345)

    #definicoes dos triangulos centrais
t1a = PVector(410,270)
t1b = PVector(410,310)
t1c = PVector(480,270)
t2a = PVector(410,330)
t2b = PVector(480,330)
t2c = PVector(480,290)
lados_m = [(ma,mb),(mb,mc),(mc,md),(md,me),(me,mf),(mf,mg),(mg,mh),(mh,mi),(mi,mj),(mj,mk),(mk,ml),(ml,mm),(mm,mn),
        (mn,mo),(mo,mp),(mp,mq),(mq,mr),(mr,ma),(t1a,t1b),(t1b,t1c),(t1c,t1a),(t2a,t2b),(t2b,t2c),(t2c,t2a)]
buraco_m = [PVector(680, 300), 7]

# lista de lados fase michels 2
sa = PVector(260,155)
sb = PVector(260,355)
sc = PVector(350,445)
sd = PVector(450,445)
se = PVector(540,355)
sf = PVector(540,155)
sg = PVector(450,155)
sh = PVector(450,355)
si = PVector(350,355)
sj = PVector(350,155)
lados_m2 = [(sa,sb),(sb,sc),(sc,sd),(sd,se),(se,sf),(sf,sg),(sg,sh),(sh,si),(si,sj),(sj,sa)]
buraco_m2 = [PVector(495,175), 7]


#definicoes das classes
class Bola:
    def __init__(self,p,v,r):
        self.v = v.copy()
        self.p = p.copy()
        self.r = r
        self.para = True
    def move(self,dt):
        self.p.add(self.v*dt)
    
    def xlr8(self,dt):    
        v = self.v.copy()
        if self.para:
            if v.mag() < 0.009:
                b.v.sub(b.v)
        if v.mag() < 0.1:
            mi = -0.3*v.mag()
            v.mult(mi)
            self.v.add(v)
        else:
            mi = -0.3*v.mag()**2
            v.mult(mi)
            self.v.add(v)
        self.para = True


def colide(b, s):
    s.normalize()
    vy = s*(b.v.dot(s))
    vx = b.v - vy

    
    vy = vy* (-1)
    b.p.add(2*vy)
    b.v = vx + vy

#definicao da bola
v = PVector(0,0)     # vel = 1cm/ms
p = PVector(300,300) # proporcao e de 1px = 1cm
r = 2                # diametro da bolinha oficial vale 40mm
b = Bola(p.copy(),v.copy(),r)

t = millis()
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

#incrementos e verfificadores de movimento    
inc = PVector(0,0)     
ver = False


#condicoes iniciais
fase = 1
tempo = 0
animacao = 0
tempo_animacao = 0
click = PVector(150,155)
p = PVector(150,155)
v = PVector(0,0)
b = Bola(p,v,2)

def Menu():
    global estado, click, animacao, t, inc, b, lados_menu, tempo_animacao
    
    lados = lados_menu

    oldt = t
    t = millis()
    dt = t-oldt
    background(34,115,55)

    #pista colorida    
    rectMode(CORNER)
    fill(122,166,56)
    stroke(122,166,56)
    rect(105,135,90,350)
    rect(195,395,100,90)
    triangle(295,395,335,475,295,485)
    rect(245,565,450,-90)
    rect(605,135,90,430)
    rect(295,135,310,90)

    #borda da pista
    stroke(0)
    for i in lados_menu:
        line(i[0].x,i[0].y,i[1].x,i[1].y)

    #animacao
    if tempo_animacao < 50:
        tempo_animacao += 1
    
    elif tempo_animacao == 50:    
        if animacao == 0:
            animacao += 1
            click = PVector(150,155)
            p = PVector(150,155)
            v = PVector(0,0)
            b = Bola(p,v,2)
    
        elif animacao < 60:
            animacao += 1
            click.y -= 1
            stroke(255,0,0)
            line(b.p.x,b.p.y,click.x,click.y)
            
        elif animacao == 60:
            inc.x = b.p.x - click.x
            inc.y = b.p.y - click.y
            b.v.add(inc/300)
            animacao += 1
        
        elif animacao == 61:
            b.move(dt)
            b.xlr8(dt)
            if b.p.y >= 485:
                b.v.y = -b.v.y
            if b.v.mag() == 0:
                animacao += 1
                click.x = b.p.x
                click.y = b.p.y
    
        elif animacao < 120:
            animacao += 1
            click.y -= 1
            click.x -= 2
            stroke(255,0,0)
            line(b.p.x,b.p.y,click.x,click.y)
    
        elif animacao == 120:
            inc.x = b.p.x - click.x
            inc.y = b.p.y - click.y
            b.v.add(inc/300)
            animacao += 1
        
        elif animacao == 121:
            b.move(dt)
            b.xlr8(dt)
            if b.p.y >= 565:
                b.v.y = -b.v.y
            if b.v.mag() == 0:
                animacao += 1
                click.x = b.p.x
                click.y = b.p.y
    
        elif animacao < 180:
            animacao += 1
            click.y += 1.2
            click.x += 0.3
            stroke(255,0,0)
            line(b.p.x,b.p.y,click.x,click.y)
    
        elif animacao == 180:
            inc.x = b.p.x - click.x
            inc.y = b.p.y - click.y
            b.v.add(inc/300)
            animacao += 1
        
        elif animacao == 181:
            b.move(dt)
            b.xlr8(dt)
            if b.p.x <= 605:
                b.v.x = -b.v.x
            if b.p.y <= 135:
                b.v.y = -b.v.y
            if b.v.mag() == 0:
                animacao += 1
                click.x = b.p.x
                click.y = b.p.y
    
        elif animacao < 240:
            animacao += 1
            click.y += 1.2
            click.x += 0.5
            stroke(255,0,0)
            line(b.p.x,b.p.y,click.x,click.y)
    
        elif animacao == 240:
            inc.x = b.p.x - click.x
            inc.y = b.p.y - click.y
            b.v.add(inc/300)
            animacao += 1
        
        elif animacao == 241:
            b.move(dt)
            b.xlr8(dt)
            if b.p.x <= 605 and b.p.y >= 225:
                b.v.y = -b.v.y
            if b.p.y <= 135:
                b.v.y = -b.v.y
            if b.v.mag() == 0:
                animacao += 1
                click.x = b.p.x
                click.y = b.p.y
    
        elif animacao < 270:
            animacao += 1
            click.y -= 0.05
            click.x += 2.9
            stroke(255,0,0)
            line(b.p.x,b.p.y,click.x,click.y)
    
        elif animacao == 270:
            inc.x = b.p.x - click.x
            inc.y = b.p.y - click.y
            b.v.add(inc/300)
            animacao += 1
        
        elif animacao == 271:
            b.move(dt)
            b.xlr8(dt)
            if b.p.x <= 605 and b.p.y >= 225:
                b.v.y = -b.v.y
            if b.p.y <= 135:
                b.v.y = -b.v.y
            if b.p.x <= 295:
                b.v.x = -b.v.x
            if (b.p.x - 325)**2 + (b.p.y - 180)**2 <= 49:
                b.p.x = 325
                b.p.y = 180
                b.v.x = 0
                b.v.y = 0
                tempo_animacao += 1
        else:
            tempo_animacao += 1
    elif tempo_animacao < 100:
        tempo_animacao += 1
    else:
        tempo_animacao = 0
        animacao = 0
        
    #buraco
    fill(0)
    stroke(0,0,0)
    ellipse(325, 180, 7, 7)

    fill(255)
    stroke(255)
    ellipse(b.p.x,b.p.y, 2*b.r, 2*b.r)
    
    rectMode(CENTER)
    textAlign(CENTER)
    textSize(50)
    text('MINIGOLF',width/2,100)
    
    textSize(20)
    fill(0,0,0)
    stroke(0)
    
    text('New Game', width/2, 280)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 280+45 and mouseY >= 280-45:
        noFill()
        rect(width/2, 280,180,90)
    
    fill(0,0,0)
    text('Credits', width/2, 370)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 370+45 and mouseY >= 370-45:
        noFill()
        rect(width/2, 370,180,90)

def detecta_buraco():
    global tempo, fase, estado, Menu, t, lados, b, lados_r, ret_r1, ret_r2, buraco, Creditos
    bru = buraco[0]
    if (bru.x-b.p.x)**2 + (bru.y - b.p.y)**2 <= (buraco[1]/2)**2:
        b.p.x = bru.x
        b.p.y = bru.y
        b.v.x = 0
        b.v.y = 0
        tempo+=1
        if tempo >100:
            tempo = 0
            if fase == 1:
                b.p.x = 170
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                lados = lados_r
                buraco = buraco_r
            elif fase == 2:
                b.p.x = 170
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                lados = lados_m
                buraco = buraco_m
            elif fase == 3:
                b.p.x = 305
                b.p.y = 175
                b.v.x = 0
                b.v.y = 0
                lados = lados_m2
                buraco = buraco_m2
            elif fase == 4:
                estado = Creditos
                fase = 0
                b = Bola(p.copy(),v.copy(),r)
                lados = lados1
                buraco = [PVector(500,300), 7]
                
                
            fase += 1
        
    
lados = lados1    

def Minigolf():
    global estado, Menu, t, lados, b, lados_r, ret_r1, ret_r2, buraco
    oldt = t
    t = millis()
    dt = t-oldt
    
    def fase1():
        rectMode(CORNER)
        stroke(122,166,56,127)
        fill(122,166,56,127)
        rect(250,250,300,100)
        
        stroke(0)
        for i in lados:
            line(i[0].x,i[0].y,i[1].x,i[1].y)
        fill(0)    
        ellipse(buraco[0].x, buraco[0].y, buraco[1], buraco[1])
    
    def fase2():
        rectMode(CORNER)
        stroke(122,166,56,127)
        fill(122,166,56,127)
        rect(150,255,500,90)
        
        noStroke()
        fill(149,191,59,100)
        rect(ret_r1[0].x, ret_r1[0].y,ret_r1[1], ret_r1[2])
        fill(149,191,59,255)
        rect(ret_r2[0].x, ret_r2[0].y,ret_r2[1], ret_r2[2])
        
        stroke(0)
        for i in lados:
            line(i[0].x,i[0].y,i[1].x,i[1].y)
        fill(0)    
        ellipse(buraco[0].x, buraco[0].y, buraco[1], buraco[1])
        
        if b.p.x > 300 and b.p.x < 350 :
            b.para = False
            b.v.x -= 0.0001*dt
            b.v.y -= 0.0001*dt
            
        if b.p.x > 450 and b.p.x < 500 :
            b.para = False
            b.v.x += 0.0001*dt
            b.v.y += 0.0001*dt
            
    def fase3():
        rectMode(CORNER)
        stroke(122,166,56)
        fill(122,166,56)
        rect(100,255,600,90)
        rect(400,155,90,290)
        triangle(590,255,617.5,255-55/2*3**(1/2),700,255)
        triangle(617.5,255-55/2*3**(1/2),672.5,255-55/2*3**(1/2),700,255)
        triangle(700,345,672.5,345+55/2*3**(1/2),617.5,345+55/2*3**(1/2))
        triangle(617.5,345+55/2*3**(1/2),590,345,700,345)
                
        stroke(0)
        for i in lados:
            line(i[0].x,i[0].y,i[1].x,i[1].y)
            
        fill(0)    
        ellipse(buraco[0].x, buraco[0].y, buraco[1], buraco[1])
        fill(252,237,20)
        triangle(410,270,410,310,480,270)
        triangle(410,330,480,330,480,290)
    
    def fase4():
        rectMode(CORNER)
        stroke(122,166,56,127)
        fill(122,166,56,127)
        rect(260,155,90,200)
        rect(450,155,90,200)
        
        stroke(242,188,121)
        fill(242,188,121)
        triangle(261,355,350,445,450,445)
        triangle(450,445,540,355,261,355)

        stroke(0)
        for i in lados:
            line(i[0].x,i[0].y,i[1].x,i[1].y)
        
        fill(0)    
        ellipse(buraco[0].x, buraco[0].y, buraco[1], buraco[1])
        
        #freiando caso esteja na areia
        if b.p.y > 355:
            b.xlr8(dt)
            
    background(34,115,55)
    
    if fase == 1:
        fase1()
    elif fase == 2:
        fase2()
    elif fase == 3:
        fase3()
    elif fase == 4:
        fase4()
    
    rectMode(CENTER)
    stroke(0)
    fill(0)
    text('Exit', 0.11*width, 50)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
        noFill()
        rect(0.11*width, 50, 0.2*width, 60)
        
    text('Restart', 0.11*width, 120)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 120+30 and mouseY >= 120-30:
        noFill()
        rect(0.11*width, 120, 0.2*width, 60)
                                                    
            
    b.move(dt)
    b.xlr8(dt)
    
    detecta_colisao()
    detecta_buraco()
    
    fill(255)
    stroke(255)
    ellipse(b.p.x,b.p.y, 2*b.r, 2*b.r)
    

posy = y-50

def Creditos():
    global posy, Menu, estado, y
    background(0)
    posx = width/2
    v = -3
    posy += v
    fill(255)
    text("Minigolf: \n Isaque Vieira Machado Pim \n Igor Patricio Michels  \n \n Agradecimentos: \n Paulo Cesar \n Asla de Sa \n Coffee Machine do 14", posx, posy)
    if posy < -400:
        estado = Menu
        posy = y-50
        animacao = 0
        tempo_animacao = 0
    

estado = Menu

def setup():
    size(x, y)
    
def draw():
    global estado
    estado()
    
def mouseDragged():
    global inc, ver
    
    if b.v.mag() == 0: #condicao para nao aceitar tacadas se a bola estiver se movendo
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
    global estado, Minigolf, Creditos, b, p, v, r, lados, buraco, fase, tempo, animacao, tempo_animacao
    if estado == Menu:
        if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 250+45 and mouseY >= 250-45:
                estado = Minigolf  
                b.p.x = 300
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                animacao = 0
                tempo_animacao = 0
        if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 400+45 and mouseY >= 400-45:
                estado = Creditos
                animacao = 0
                tempo_animacao = 0
    if estado == Minigolf:
        if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
            estado = Menu
            b = Bola(p.copy(),v.copy(),r)
            lados = lados1
            buraco = [PVector(500,300), 7]
            fase = 1
            animacao = 0
            tempo_animacao = 0
        if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 120+30 and mouseY >= 120-30:
            if fase == 1:
                b.p.x = 300
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                tempo = 0
            elif fase == 2:
                b.p.x = 170
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                tempo = 0
            elif fase == 3:
                b.p.x = 170
                b.p.y = 300
                b.v.x = 0
                b.v.y = 0
                tempo = 00
            elif fase == 4:
                b.p.x = 305
                b.p.y = 175
                b.v.x = 0
                b.v.y = 0
                tempo = 0
