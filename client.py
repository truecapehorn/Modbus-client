from Modbus_API.modbus_master import TCP_Client,RTU_Client,Master
import json, time




class Client:
    def __init__(self,path,client_type):
        self.path= path
        self.client_type=client_type

    def open_config(self):
        with open(self.path) as json_file:
            return json.load(json_file)

    def get_parm(self):
        _config = self.open_config()
        _dict_parm = _config['client'][self.client_type]
        return _dict_parm


    def make_client(self):
        _parm=self.get_parm().values()
        if self.client_type=='tcp':
            _master = TCP_Client(*_parm)
        if self.client_type=='rtu':
            _master = RTU_Client(*_parm)
        _client = _master.client
        return Master(_client)

class Odczyt:
    def __init__(self, client, unit, reg_start, reg_lenght, data_type, transp=True):
        self.client = client
        self.unit = unit
        self._reg_start = reg_start
        self.reg_lenght = reg_lenght
        self.data_type = data_type
        self.transp = transp

    def _read_reg(self):
        reg = self.client.read_register(self.unit, self._reg_start,
                                   self.reg_lenght, self.reg_type,
                                   self.data_type, self.transp)
        return reg

    def read_holding(self):
        self.reg_type='holding'
        return self._read_reg()

    def reg_adress(self):
        return self._reg_start

    def set_reg_adress(self, adress):
        self._reg_start = adress



if __name__=='__main__':


    modbus = Client('config.json','tcp')
    client=modbus.make_client()
    print(modbus.get_parm())

    # reg_for_check = [30201, 30233, 30531, 30775, 30795, 30803, 30805, 30813, 30837, 30839, 30769, 30771, 30773,
    #                  30957, 30959, 30961, 30537, 30953, 40212, 40915]

    reg_for_check = [i for i in range(1000, 1016)]
    nr = 1
    reg32 = Odczyt(client, unit=3, reg_start=0, reg_lenght=1, data_type='int', transp=True)

    try:
        while True:
            print(nr, end=': ')
            for i in reg_for_check:
                reg32.set_reg_adress(i)
                holding = reg32.read_holding()
                print(holding['Data'], end=',')
            print('\n')
            nr += 1
    except KeyboardInterrupt:
        print('Koniec')
