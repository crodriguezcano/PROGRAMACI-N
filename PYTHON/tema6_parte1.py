
def codigo_1( number ): 
    a = 0 
    for j in range(1, number+1): 
        a += a + j 
    for k in range(number, 0, -1): 
        a -= 1 
        a *= 2 
    return a 

def codigo_2(): 
    a = 0 
    a -= 1 
    a *= 2 

def codigo_3( number ): 
    a = 0; 

    for j in range(1, number+1): 
        for k in range(1, number+1): 
            a += a + ( k*j ) 
    return a

def codigo_4(array): 
    for k in range(len(array)): 
        if( array[k] % 2 == 0 ): 
            return k 
    return null 

import numpy as np 
x = list(np.random.randint(low=1,high=500000, size=99999999)) 

def constante(x:list) -> list: 
    return x 
constante(x) 