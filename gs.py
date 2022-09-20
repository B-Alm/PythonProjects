import random, string

tamanho = int(input('Digite o tamanho de senha que voce deseja: '))
#tamanho = 16
chars = string.ascii_letters + string.digits + '!@#$%&*()_-+='
#digitis de 0 a 9 #letters usa letras mauisculas e minusculas juntas

rnd = random.SystemRandom() #os.uramdom gera numeros aleatorios
print(''.join(rnd.choice(chars) for i in range(tamanho)))
#choice reotrna uma lista de caracteres ramdomicos

