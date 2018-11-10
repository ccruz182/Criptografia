'''
  File name: decifrado.py
  Author: Cesar Cruz
  Project: Cifrado archivos AES
  Python Version: 2.7
'''

from utilidadesCripto \
import lectura_archivo, fragmentador, decifrar, escritura_archivo


ARCHIVO_CIFRADO = "resultados/cifrado.pdf"
ARCHIVO_ORIGINAL = "resultados/original.pdf"

LLAVE = "MI_LLAVE"
VECTOR_INICIAL = "IV123456"

archivo_en_bytes = lectura_archivo(ARCHIVO_CIFRADO)

fragmentos = fragmentador(archivo_en_bytes, 8)

archivo_decifrado = decifrar(fragmentos, LLAVE, VECTOR_INICIAL)

escritura_archivo(ARCHIVO_ORIGINAL, archivo_decifrado)