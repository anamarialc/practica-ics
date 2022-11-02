#!/usr/bin/env python

import sys
import os

path = "Ficheros_realizar_Ejr2/BU-www-client-traces/condensed/272/Feb95/"


def main():
    separator = '\t'
    for filename in sorted(os.listdir(path)):
        documento = filename.split('.')
        usuario = documento[0][3:]  # Sacamos el numero del usuario de cada uno de los ficheros
        with open(os.path.join(path, filename), 'r') as f:
            for col in f:
                doc = col.split()  # Muestra el contenido de cada fichero a leer print(doc)
                if doc[3][-4:] == '.ps"':
                    print(usuario, separator, 1)  # Imprime el numero del usuario del que lee una URL terminada en .ps
                print(doc[3], '\t', 1)


if __name__ == "__main__":
    main()
