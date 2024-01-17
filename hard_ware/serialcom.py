import serial#导入串口通信库
class SerialCom(serial.Serial):
    def __init__(self,port='com6',baudrate= 115200,timeout=0.1,bytesize= 8,stopbits= 1,parity= "N" ):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.parity = parity # 奇偶校验位
        self.timeout=timeout

    def port_open(self):#对串口的参数进行配置
        self.open()
        if(self.isOpen()):
            print("open %s！"%self.port)
        else:
            print("open %s fail"%self.port)

    def port_close(self):
        self.close()
        if(self.isOpen()):
            print("close %s fail！"%self.port)
        else:
            print("close %s"%self.port)

    def send(self,send_data):
        data='Null'
        if(self.isOpen()):
            self.write(send_data.encode('utf-8'))#编码
            print("send->", send_data)
            data=self.recieve()

        else:
            print("send fail！")
        return data
    def recieve(self):
        data=self.readall()
        msg=data.decode('utf-8')
        print("recieve<- %s"%msg)
        return data

if __name__ == '__main__':
    se=SerialCom(port='com6')
    se.port_open()
        #a=input("输入要发送的数据：")
    a='MS;'
    se.send(a)
    se.port_close()

