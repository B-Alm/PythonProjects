# -*- coding: iso-8859-15 -*-

import platform

print("Distribui��o do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Vers�o do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de M�quina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Vers�o do Python....................: ", platform.python_version())