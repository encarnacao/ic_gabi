#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:37:04 2021

@author: gabriella
"""

import random 
import numpy as np
import matplotlib.pyplot as plt

def KPZ_2D(n,linhas,colunas): #Lembrando que linhas x colunas <= n
    """Essa funcao e uma tentativa de reproduzir o metodo KPZ em 2D dado o numero de particulas e o numero de linhas e colunas
    da matriz que representa a malha 2D"""
    matriz = np.zeros([linhas,colunas]) #Cria uma matriz zerada de linhas e colunas
    X_min, X_max, Y_min, Y_max = 0, linhas-1, 0, colunas-1 #Onde começa e onde termina minhas opcoes de sorteio
    
    #Entrando no loop para colocar os elementos ali:
    matriz[(linhas//2 - 1), (colunas//2 -1)] = 1 #Fixa o 1º elemento na posicao central (ou perto)
    for i in range(1,n):
        if n > linhas*colunas:
            print("Entrada inválida! O numero de elementos é maior do que as dimensões da matriz.")
            break
    
        #Sortear de onde vai sair a segunda particula:
        lado_inicial = random.randint(1,4) #Escolhendo de qual dos 4 lados a particula ira sair
        #legenda: 1-> base, 2-> parte superior, 3-> lateral esquerda, 4-> lateral direita
        if lado_inicial == 1:
            Y_inicial, X_inicial = Y_min, random.randint(X_min,X_max)
        elif lado_inicial ==2:
            Y_inicial, X_inicial = Y_max, random.randint(X_min,X_max)
        elif lado_inicial == 3:
            Y_inicial, X_inicial = random.randint(Y_min, Y_max), X_min
        else:
            Y_inicial, X_inicial = random.randint(Y_min, Y_max), X_max
        X, Y = X_inicial, Y_inicial
        
        if X == matriz.shape[1]-1:
            x_1 = 0
        else:
            x_1 = X+1
        if Y == matriz.shape[0]-1:
            y_1 = 0
        else: 
            y_1 = Y+1
        
        #Fazer a particula andar tal que ela pare apenas quando se encontrarna diagonal de outra particula:
        while (matriz[y_1,x_1] != 1 and matriz[y_1,X-1] != 1) and (matriz[Y-1,x_1] != 1 and matriz[Y-1,X-1] != 1):
            
            X += random.randint(-1,1)
            Y += random.randint(-1,1)
            
            if X < X_min:
                X = X_max
            if X > X_max:
                X = X_min
            if Y > Y_max:
                Y = Y_min
            if Y < Y_min:
                Y = Y_max
                
            if X == matriz.shape[1]-1:
                x_1 = 0
            else:
                x_1 = X+1
            if Y == matriz.shape[0]-1:
                y_1 = 0
            else: 
                y_1 = Y+1
                
        matriz[Y,X] = 1

        #Plotando
    fig, ax = plt.subplots() #define a figura para o plot
    ax.axis('off')
    ax.matshow(matriz) #plota matrix no ax
    return 
        #FALTA:  e subdominio e mudar o while para ele nao colocar nada do lado (talvez nao precise mudar)