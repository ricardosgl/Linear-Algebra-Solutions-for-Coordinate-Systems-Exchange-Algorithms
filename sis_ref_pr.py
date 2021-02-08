# Ricardo Juan Cárdenes Pérez
# 7/2/2021

import numpy as np
import matplotlib.pyplot as plt

def ref_sis_2d(o,op,e1,e2,p):

    # Operaciones matriciales
    q = np.array([e1,e2]).T

    try:
        c = np.linalg.inv(q)

    except Exception as err:
        print(err.args[0])
        return 'El sistema de referencia 2 no es bidimensional'

    pp = np.matmul(c, p - op)

    # Devolvemos el resultado
    return pp


if __name__ == '__main__':

    # Declaramos sistemas de referencia
    comp = {'O':'', 'O\'': '', 'e1': '', 'e2': '', 'P': ''}
    for i in comp.keys():
        n1 = int(input(f'Introduce la coordenada en X de {i}: '))
        n2 = int(input(f'Introduce la coordenada en Y de {i}: '))
        comp[i] = np.array([[n1],[n2]])

    pp = ref_sis_2d(comp['O'],comp['O\''],comp['e1'],comp['e2'],comp['P'])
    print(pp)
