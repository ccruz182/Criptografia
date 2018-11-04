from Crypto.Cipher import AES

ARCHIVO_A_CIFRAR = "Practica2.rar"
ARCHIVO_CIFRADO = "cifrado.rar"


archivoEnBytes = []

f = open(ARCHIVO_A_CIFRAR, "rb")
try:
  byte = f.read(1)
  while byte != "":        
    archivoEnBytes.append(byte)
    byte = f.read(1)
    
finally:
    f.close()

fragmentos = []
numFrag = len(archivoEnBytes) / 16
extras = len(archivoEnBytes) % 16

i = 0

for k in range(numFrag):
  pedazo = archivoEnBytes[i:(i + 16)]  
  nuevoPedazo = ''.join(pedazo)
  fragmentos.append(nuevoPedazo)
  i += 16

if extras != 0:
  ultimo_pedazo = archivoEnBytes[i:(i+extras)]
  ultimo_pedazo = ''.join(ultimo_pedazo)
  tam_ultimo = len(ultimo_pedazo)
  for j in range(16 - tam_ultimo):
    ultimo_pedazo += '\24'
  
  fragmentos.append(ultimo_pedazo)  

archivoCifrado = []
for fragmento in fragmentos:
  cifrador = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  ciphertext = cifrador.encrypt(fragmento)  
  archivoCifrado.append(ciphertext)

f = open(ARCHIVO_CIFRADO, 'wb')
for parte in archivoCifrado:
  f.write(parte)
f.close()