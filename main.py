from client import Klient, Rejestry, Cewki
import time

modbus_rtu = Klient('config.json', 'rtu')
client_rtu = modbus_rtu.make_client()
print(modbus_rtu.get_parm())


reg_1 = Rejestry(client_rtu, unit=64, reg_start=0, reg_lenght=10, data_type='int')
reg_2 = Rejestry(client_rtu, unit=25, reg_start=70, reg_lenght=10, data_type='int')


def print_data(device ,time, data):
    return print("Urzadzenie:{} - {} : {}".format(device, time, data), end=';\n')


try:
    while True:

        holding_1 = reg_1.read_holding()
        print_data(holding_1['Device'],holding_1['Time'][1], holding_1['Data'])


        time.sleep(1)
except KeyboardInterrupt:
    print('\nKoniec')
