import numpy as np
import sympy as sym


def fkine(th, d, alp, a):
 
    #Pasamos de grados a radianes
    th = th*np.pi/180.0
    alp = alp*np.pi/180.0
    
    dh_matrix = np.array(
        [ [(sym.cos(th)), (-np.cos(alp)*sym.sin(th)), (np.sin(alp)*sym.sin(th)),  (-a*sym.cos(th))],
          [(sym.sin(th)), (np.cos(alp)*sym.cos(th)),  (-np.sin(alp)*sym.cos(th)), (a*sym.sin(th)) ],
          [     (0)     , (sym.sin(alp)),             (sym.cos(alp)),             (d)             ],
          [     (0),      (0),                        (0),                        (1)             ]
        ]
    )

    return dh_matrix

#Ingreso de valores para cada una de las matrices
T_01 = fkine(sym.Symbol('th1'), 13, -90, 0)
T_12 = fkine(sym.Symbol('th2'), 0, 0, 8)
T_23 = fkine(sym.Symbol('th3'), sym.Symbol('-l'), 90, 0)
T_34 = fkine(sym.Symbol('th4'), 8, -90, 0)
T_45 = fkine(sym.Symbol('th5'), 0, 90, 0)
T_56 = fkine(sym.Symbol('th6'), sym.Symbol('t'), 0, 0)

#Imprime las matrices por cada link
print('Matriz T 01 = \n' , T_01 ,
     '\nMatriz T 12 = \n', T_12,
     '\nMatriz T 23 = \n', T_23,
     '\nMatriz T 34 = \n', T_34,
     '\nMatriz T 45 = \n', T_45,
     '\nMatriz T 56 = \n', T_56)

#Operaciones para encontrar la matriz de 0 a 6
T_02 = np.multiply(T_01,T_12)
T_03 = np.multiply(T_02,T_23)
T_04 = np.multiply(T_03,T_34)
T_05 = np.multiply(T_04,T_45)
T_06 = np.multiply(T_05,T_56)

print('Matriz T 06 = \n', T_06)

a = 1