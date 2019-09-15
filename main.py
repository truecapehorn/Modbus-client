from client import Klient, Rejestry, Cewki
import time

modbus = Klient('config.json', 'tcp')
client = modbus.make_client()
print(modbus.get_parm())

# reg_for_check = [30201, 30233, 30531, 30775, 30795, 30803, 30805, 30813, 30837, 30839, 30769, 30771, 30773,
#                  30957, 30959, 30961, 30537, 30953, 40212, 40915]

reg = Rejestry(client, unit=1, reg_start=1000, reg_lenght=16, data_type='int')
bol = Cewki(client, unit=1, reg_start=0, reg_lenght=250)

reg_for_check = [i for i in range(1000, 1016)]
nr = 1


def print_data(time, data):
    return print("{} : {}".format(time, data), end=';\n')


try:
    while True:
        # reg.set_reg_adress(0)
        # reg.set_lenght_data(nr)
        # bol.set_lenght_data(nr)
        holding = reg.read_holding()
        col = bol.read_coil()
        print_data(holding['Time'][1], holding['Data'])
        print_data(col['Time'][1], col['Data'])
        nr += 1
        time.sleep(1)
except KeyboardInterrupt:
    print('\nKoniec')
