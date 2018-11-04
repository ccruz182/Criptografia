'''
  File name: decifrado.py
  Author: Cesar Cruz
  Project: Cifrado archivos AES
  Python Version: 2.7
'''

from Crypto.Cipher import AES

from utilidadesCripto \
import lectura_archivo, fragmentador, decifrar, escritura_archivo


ARCHIVO_CIFRADO = "resultados/cifrado.jpg"
ARCHIVO_ORIGINAL = "resultados/original.jpg"

LLAVE = "This is a key123"
VECTOR_INICIAL = "This is an IV456"

archivo_en_bytes = lectura_archivo(ARCHIVO_CIFRADO)

fragmentos = fragmentador(archivo_en_bytes, 16)

archivo_decifrado = decifrar(fragmentos, LLAVE, VECTOR_INICIAL)

escritura_archivo(ARCHIVO_ORIGINAL, archivo_decifrado)