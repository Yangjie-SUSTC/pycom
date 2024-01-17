# ！ python
# author：yangjie@2024
# uesd for AF static test
from hard_ware import elmo
from hard_ware import xy_stage
import numpy as np
from hard_ware import serialcom
class AF():
    def __init__(self):
        self.elmo=elmo.Elmo(port='com6')
        self.xy_stage=xy_stage.XyStage()
        pass
    def get_xyz(self):
        self.x,self.y=self.xy_stage.get_xy()
        self.z=self.elmo.get_z()
        pos=[self.x,self.y,self.z]
        return pos

    def static_test(self):
        zr=20
        dz=1
        record_time_ms=1
        x_list=[0,1,2,3,4]
        y_list=[0,1,2,3,4]

        dz_list = range(-zr, zr+dz, dz)
        data_list=[]
        count=0
        total_num=len(x_list)
        for x,y in zip(x_list,y_list):
            count =count+1
            msg='----------- start %d/%d test'%(count,total_num)
            print(msg)

            self.xy_stage.set_xy(x,y)
            x0,y0,z0=self.get_xyz()
            msg='----------- start x %.4f,y %.4f,z %.4f test'%(x0,y0,z0)
            print(msg)
            data={'pos0':[x0,y0,z0]}
            self.elmo.set_z(z0)
            ana_in0 = self.elmo.get_ana_in(record_time_ms)
            af_signal0 = np.mean(ana_in0)
            self.set_af_ref(af_signal0)

            data['ana_in0'] = ana_in0
            data['af_signal0'] = af_signal0
            data['dz_list']=dz_list

            data['ana_in1']=[]
            data['af_signal1'] = []
            data['ana_in2'] = []
            data['af_signal2'] = []


            for dz in dz_list:
                self.elmo.move(dz)
                ana_in1 = self.elmo.get_ana_in(record_time_ms)
                af_signal1 = np.mean(ana_in1)
                data['ana_in1'].append(ana_in1)
                data['af_signal1'].append(af_signal1)
                self.af_on(True)

                ana_in2=self.elmo.get_ana_in(record_time_ms)
                af_signal2=np.mean(ana_in2)
                data['ana_in2'].append(ana_in2)
                data['af_signal2'].append(af_signal2)
                self.af_on(False)
            data_list.append(data)
        return data_list


    def set_af_ref(self,ref):
        self.af_ref=ref
    def af_on(self,status):
        flag = True
        try:
            self.af = status
            msg = 'af : %s' % (status)
            print(msg)
        except:
            flag = False
        return flag


class SinglePointData():
    def __init__(self):
        self.pos=[]
        self.af_signal_off=[]
        self.af_signal_off_mean=[]
        self.af_signal_on = []
        self.af_signal_off_mean = []




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    af = AF()
    data_list = af.static_test()
    print('finish')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
