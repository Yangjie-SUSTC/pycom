class Elmo():
    def __init__(self):
        self.z=0

    def move(self, dz):
        flag = True
        try:
            self.z = self.z+dz
            msg = 'move dz: %.4f' % (dz)
            print(msg)
        except:
            flag = False
        return flag
    def set_z(self,z):
        flag = True
        try:
            self.z=z
            msg = 'move to z: %.4f' % (self.z)
            print(msg)
        except:
            flag=False
        return flag
    def get_z(self):
        msg = 'z: %.4f' % (self.z)
        print(msg)
        return self.z

    def get_ana_in(self,record_time_ms):
        signal=[0,0,0]

        return signal