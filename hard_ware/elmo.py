from hard_ware.serialcom import SerialCom
class Elmo(SerialCom):
    def __init__(self,port='com6'):
        super().__init__(port)
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

    def decode_com_rev(self,data):
        print(data)



if __name__ == '__main__':
    se = Elmo(port='com6')
    se.port_open()
    # a=input("输入要发送的数据：")
    a = 'MS;'
    data=se.send(a)
    se.decode_com_rev( data)
    se.port_close()