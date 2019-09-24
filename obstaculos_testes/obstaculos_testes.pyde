class Obstaculo:
    def __init__(self):
        pass

    def obstaculo1(self, px, py, x, y):
        #definir cores ainda
        #ver equações das elipses para ver a tangente
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
        stroke(0, 0, 255)
        fill(0)
        ellipse(pxi, pyi, x, y)
        
        stroke(255, 0, 0)
        fill(0)
        ellipse(pxo, pyo, x, y)

    def obstaculo4(self, px, py, x, y):
        #lago
        #caso a bolinha entre aqui, ela volta para o ponto em que saiu
        ellipse(px, py, x, y)
        ellipse(px, py, x/2, y/2)
        
    def obstaculo5(self, px, py, x, y):
        #areia
        #aumenta a força necessária para a bolinha se mover
        ellipse(px, py, 3*x/2, y)

o = Obstaculo()

def setup():
    size(1200, 800)
    noStroke()
    
    
def draw():
    background(255)
    o.obstaculo1(300, 300, 200, 200)
    print(o.a21)
    print(o.b21)
    print(o.a22)
    print(o.b22)
#    print(o.tg5)
#    print(o.tg6)
#    print(o.tg7)

    o.obstaculo2(700, 300, 100, 100)
