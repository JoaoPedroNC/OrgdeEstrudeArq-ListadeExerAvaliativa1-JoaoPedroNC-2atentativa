import struct
arquivo= open(“sinasc-sp-2018.dat”, “r”)

registro_struct = struct.Struct(“6s7s6s8s2s1s4s8s”)

cod_munici = 0

cod_estabe= 1

cod_sexo = 5

cod_peso = 6

#1) Qual é o tamanho do arquivo em bytes?
print(f”1) Tamanho do arquivo em bytes: {arquivo.seek(0, 2)}bytes”)
  
#2) Qual é o tamanho de cada registro?
print(“2) Tamanho de cada registro:”, registro_struct.size)

#3) Quantos registros tem o arquivo?    
num_registros = int(arquivo.seek(0,2)// registro_struct.size)
print(“3)Quantos registros tem o arquivo:”,num_registros)
  
#4) Copie em um novo arquivo chamado “sinasc-sp-capital-2018.dat” os registros dos nascimentos (CODMUNNASC) que ocorreram na capital, cujo código é “355030”. 
#Quantos registros tem esse novo arquivo?  
  
  quantidade_em_sp = 0
  with open(“sinasc-sp-capital-2018.dat”, “w”)as novo_arquivo:

arquivo.seek(0)

for _ in range(num_registros):

registro_lido = bytes(arquivo.read(registro_struct.size), “utf-8”)

registro_tuple = registro_struct.unpack(registro_lido)

if registro_tuple[cod_munici] = b ’355030’:

novo_arquivo.write(registro_lido.decode(‘utf-8’))

quantidade_em_sp += 1

print(“4)Quantidade de registros com município de São Paulo:”, quantidade_em_sp)
  
 #5) Quantas meninas nasceram em Santos (354850) no ano de 2018?

quantidade_meninas = 0

for _ in range(num_registros):

registro_lido = bytes(arquivo.read(registro_struct.size), “utf-8”)

registro_tuple = registro_struct.unpack(registro_lido)

if registro_tuple[cod-munici] = b ’354850’ and registro_tuple[cod_sexo] = b’2’:

quantidade_meninas += 1

print(“5)Quantas meninas nasceram em Santos(354850) no ano de 2018:”, quantidade_meninas)
  
  #6) Quantos bebês nasceram com baixo peso (< 2500) em campinas (350950) no ano de 2018?
  
quantidade_bebes = 0

arquivo.seek(0)

for _ in range(num_registros):

registro-lido = bytes(arquivo.read(registro_struct.size),”utf-8”)

registro_tuple = registro_struct.unpack(registro_lido)

if registro_tuple [cod_mucici] = b ’350950’ and int(registro_tuple[cod_peso])<2500:


quantidade_bebes += 1

print(“6) Quantos bebês que nasceram com baixo peso (<2500)em Campinas(350950) no ano de 2018:”,quantidade_bebes)
  #7) Ordene o arquivo pelo código do estabelecimento, gere o arquivo “sinasc-sp-2018-ordenado.dat”. 
  #Não é para fazer ordenação externa. Pode trazer todos os registros para memória principal.
  registros = []

arquivo.seek(0)

for _ in range(num-registros):

registro_lido = bytes(arquivo.read(registro_struct.size),”utf-8”)

registro_tuple = registro_struct.unpack(registro_lido)

registros.append(registro_tuple)

registros.sort(key=lambda x: x[cod_estabel])

with open(“sinasc-sp-2018-ordenado.dat”,”w”)as novo_arquivo:

for registro in registros:

bytes_registro = registro_struct.pack(*registro)

novo_arquivo.write(bytes_registro.decode(‘utf-8’))

print(f ”7) {num_registros} registros ordenados pelo nome da escola e gravados em um novo arquivo sinasc-sp-2018-ordenado.dat.”

#8) Com o arquivo ordenado, conte o número de nascimentos por estabelecimento.
#Leia o primeiro registro e atribua ao contador 1. 
#Enquanto não for final do arquivo, leia os registros subsequentes sempre guardando o código do estabelecimento do registro anterior. 
#Quando o estabelecimento mudar ou quando o final do arquivo for alcançado, imprima o contador. 
#Se o registro lido tiver o mesmo código do estabelecimento do anterior, apenas acrescente 1 unidade ao contador, sem imprimir.
with open(“sinasc-sp-2018-ordenado.dat”, “r”) as arquivo_ordenado:

quant_estabelecimentos=0

contador = 0

estabelecimento_anterior= “”

arquivo_ordenado.seek(0)

for _ in range(num_registros):

registro_lido = bytes(arquivo_ordenado.read(registro_struct.size), “utf-8”)

registro_tuple = registro_struct.unpack(registro_lido)

if registro_tuple[cod_estabe] == estabelecimento_anterior:

contador += 1

else :

if contador>=1:

print(f”{estabelecimento_anterior} : {contador}”)

quant_estabelecimentos += 1

contador = 1

estabelecimento_anterior = registro_tuple[cod_estabe]

print(f”8)Quantidade de estabelecimentos diferentes: {quant_estabelecimentos}”)
  
  
