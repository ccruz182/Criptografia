'''
  File name: cifrado.py
  Author: Cesar Cruz
  Project: Cifrado archivos AES
  Python Version: 2.7
'''

from utilidadesCripto \
import lectura_archivo, fragmentador, cifrar, escritura_archivo

ARCHIVO_A_CIFRAR = "yo.jpg"
ARCHIVO_CIFRADO = "resultados/cifrado.jpg"

LLAVE = "This is a key123"
VECTOR_INICIAL = "This is an IV456"

#Lectura del archivo. Se almacena en una lista
archivo_en_bytes = lectura_archivo(ARCHIVO_A_CIFRAR)

fragmentos = fragmentador(archivo_en_bytes, 16)

archivo_cifrado = cifrar(fragmentos, LLAVE, VECTOR_INICIAL)

escritura_archivo(ARCHIVO_CIFRADO, archivo_cifrado)