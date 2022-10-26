import random



class Settings():
    def __init__(self):
        self.bgcolor=(100,200,100)
        self.width=800
        self.height=750
        
        self.lift=80
        self.gravity=float(0.7)
        self.pipe_speed=1
        self.delay=float(2000)
        self.center_pos=random.randint(110,600)
        