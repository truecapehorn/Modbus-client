from Modbus_API.modbus_master import *
import json, time

with open('config.json') as json_file:
    config = json.load(json_file)

host = config['client']['tcp']['host']
port = config['client']['tcp']['port']





class Odczyt:
    def __init__(self, client, unit, reg_start, reg_lenght, data_type,transp=True):
        self.client = client
        self.unit = unit
        self.reg_start = reg_start
        self.reg_lenght = reg_lenght
        self.data_type = data_type
        self.transp = transp

    def _read_reg(self):
        reg = client.read_register(self.unit, self.reg_start,
                                   self.reg_lenght, self.reg_type,
                                   self.data_type ,self.transp)
        return reg

    def read_holding(self):
        self.reg_type = 'holding'
        reg = self._read_reg()
        return reg


modbus = TCP_Client(host, port)
client = Master(modbus.client)

print(modbus.host,modbus.port)

# reg_for_check = [30201, 30233, 30531, 30775, 30795, 30803, 30805, 30813, 30837, 30839, 30769, 30771, 30773,
#                  30957, 30959, 30961, 30537, 30953, 40212, 40915]

reg_for_check = [i for i in range(1000, 1016)]
nr = 1
reg32 = Odczyt(client, unit=3, reg_start=0, reg_lenght=1, data_type='int',transp=True)

try:
    while True:
        print(nr, end=': ')
        for i in reg_for_check:
            reg32.reg_start = i
            holding = reg32.read_holding()
            print(holding['Data'], end=',')
        print('\n')
        nr += 1
except KeyboardInterrupt:
    print('Koniec')
