import time

class Manager():
    num_of_circles = 1000
    
    def __init__(self):
        self.points = []
        self.delta_radius = 1
        self.delta_angle = 0.01*TWO_PI
        self.increment = 0.0001
    
    def create_points(self):
        distance = self.delta_radius
        angle =self.delta_angle
        for i in range(self.num_of_circles):
            circle = Circle(angle, distance, i)
            distance += self.delta_radius
            angle +=self.delta_angle
            self.points.append(circle)
        
        
        
    def update(self):
        self.delta_angle += self.increment*TWO_PI
        distance = self.delta_radius
        angle =self.delta_angle
        for circle in self.points:
            circle.changhe_pos(angle, distance)
            circle.change_color()
            distance += self.delta_radius
            angle +=self.delta_angle
        
    def show(self):
        for circle in self.points:
            circle.show()

class Circle():
    num_of_circle = 1000
    radius = 65
    def __init__(self, angle, distance, number):
        self.x = distance*cos(angle)
        self.y = distance*sin(angle)
        self.hue_value = number
    
    def show(self):
        fill(self.hue_value, self.num_of_circle,self.num_of_circle)
        ellipse(self.x, self.y, self.radius, self.radius)
     
    def changhe_pos(self, angle, distance):
         self.x = distance*cos(angle)
         self.y = distance*sin(angle)
    
    def change_color(self):
        self.hue_value += 1
        if self.hue_value == self.num_of_circle:
            self.hue_value = 0
            
        
man = Manager()

def setup():
    size(1500,1500)
    frameRate(30)
    translate(width/2, height/2)
    fill(0,0,255)
    ellipse(0,0, 25, 25)
    global man
    man.create_points()
    fill(255)
    textSize(32)
    colorMode(HSB, 1000)
    
    
i = 0

def draw():
    background(51)
    translate(width/2, height/2)
    global i
    global man
    man.update()

    man.show()
    textAlign(TOP, CENTER)
    fill(200, 1000, 1000)
    text(ceil(frameRate), -width/2 +20,-height/2 + 20)
    text(man.delta_angle, -width/2+20,height/2-40)
    #approximation of th golden ratio, for some reason doesnt stop
    if man.delta_angle == 0.618:
        time.sleep(5)
    
    
    
