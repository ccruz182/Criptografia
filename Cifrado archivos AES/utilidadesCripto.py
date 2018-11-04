'''
  File name: utilidadesCripto.py
  Author: Cesar Cruz
  Project: Cifrado archivos AES
  Python Version: 2.7
'''
from Crypto.Cipher import AES

# Funcion para la lectura de un archivo en bytes.
# Retorna una lista con los bytes.
def lectura_archivo(nombre_archivo):
  archivo_en_bytes = []

  f = open(nombre_archivo, "rb")
  try:
    byte = f.read(1)

    while byte != "":        
      archivo_en_bytes.append(byte)
      byte = f.read(1)
    
  finally:
    f.close()
    return archivo_en_bytes

# Funcion para fragmentar el archivo, dada una longitud.
def fragmentador(archivo_en_bytes, tam_fragmento):
  fragmentos = []

  # Calculo del numero de fragmentos a realizar y si habra extras.
  numFrag = len(archivo_en_bytes) / tam_fragmento
  extras = len(archivo_en_bytes) % tam_fragmento

  i = 0

  # Se corta el arreglo
  for k in range(numFrag):
    pedazo = archivo_en_bytes[i:(i + tam_fragmento)]  
    nuevoPedazo = ''.join(pedazo)
    fragmentos.append(nuevoPedazo)
    i += 16

  # Hay bytes restantes.
  if extras != 0:
    ultimo_pedazo = archivo_en_bytes[i:(i + extras)]
    ultimo_pedazo = ''.join(ultimo_pedazo)
    tam_ultimo = len(ultimo_pedazo)

    for j in range(tam_fragmento - tam_ultimo):
      ultimo_pedazo += '\0'

    fragmentos.append(ultimo_pedazo)  

  return fragmentos

# Funcion para el cifrado de una lista de fragmentos.
def cifrar(fragmentos, llave, vector_inicial):
  archivo_cifrado = []

  for fragmento in fragmentos:
    cifrador = AES.new(llave, AES.MODE_CBC, vector_inicial)
    ciphertext = cifrador.encrypt(fragmento)  
    archivo_cifrado.append(ciphertext)

  return archivo_cifrado

def decifrar(fragmentos, llave, vector_inicial):
  archivo_decifrado = []

  for fragmento in fragmentos:
    decifrador = AES.new(llave, AES.MODE_CBC, vector_inicial)
    ciphertext = decifrador.decrypt(fragmento)  
    archivo_decifrado.append(ciphertext)

  return archivo_decifrado


# Funcion para la escritura de un archivo, con el contenido.
def escritura_archivo(nombre_archivo, contenido):
  f = open(nombre_archivo, 'wb')
  
  for parte in contenido:
    f.write(parte)
  
  f.close()