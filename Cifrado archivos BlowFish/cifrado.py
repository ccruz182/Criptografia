'''
  File name: cifrado.py
  Author: Cesar Cruz
  Project: Cifrado archivos Blowfish
  Python Version: 2.7
'''

from utilidadesCripto \
import lectura_archivo, fragmentador, cifrar, escritura_archivo

ARCHIVO_A_CIFRAR = "cobit.pdf"
ARCHIVO_CIFRADO = "resultados/cifrado.pdf"

LLAVE = "MI_LLAVE"
VECTOR_INICIAL = "IV123456"

#Lectura del archivo. Se almacena en una lista
archivo_en_bytes = lectura_archivo(ARCHIVO_A_CIFRAR)

fragmentos = fragmentador(archivo_en_bytes, 8)

archivo_cifrado = cifrar(fragmentos, LLAVE, VECTOR_INICIAL)

escritura_archivo(ARCHIVO_CIFRADO, archivo_cifrado)