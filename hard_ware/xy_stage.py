class XyStage():
    def __init__(self):
        self.x=0
        self.y=0

    def set_xy(self, x,y):
        flag = True
        try:
            self.x = x
            self.y = y
            msg = 'move to x: %.4f,y: %.4f' % (self.x ,self.y )
            print(msg)
        except:
            flag = False
        return flag
    def get_xy(self):
        pos=[self.x,self.y]
        msg='x: %.4f,y: %.4f'%(self.x,self.y)
        print(msg)
        return pos
    def move(self,dx,dy):
        self.x = self.x+dx
        self.y = self.y+dy
        msg='move  dx: %.4f,dy: %.4f' % (self.dx, self.dy)
        print(msg)
