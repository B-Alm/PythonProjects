# -*- coding: iso-8859-15 -*-
import  hashlib

string = (input("Digite o texto a ser gerado  a hash: "))

menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ### 
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    dIGITE O N�MERO DO HASH A SER GERADO: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))

    print('O hash MD5 da string: ', string, '�: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))

    print('O hash sha1 da string: ', string, '�: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))

    print('O hash sha256 da string: ', string, '�: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))

    print('O hash sha512 da string: ', string, '�: ', resultado.hexdigest())
else:
    print('Algo d errado n�o deu certo, tente novamente')