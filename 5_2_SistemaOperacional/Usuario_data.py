# -*- coding: iso-8859-15 -*-

import getpass
from datetime import datetime

print("Usu�rio.......: ", getpass.getuser())
print("Data Completa.: ", datetime.now())
print("Dia...........: ", datetime.now().day)
print("M�s...........: ", datetime.now().month)
print("Ano...........: ", datetime.now().year)
print("Hora..........: ", datetime.now().hour)
print("Minuto........: ", datetime.now().minute)
print("Segundo.......: ", datetime.now().second)