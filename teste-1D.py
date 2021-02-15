#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:46:16 2021

@author: gabriella
Modificado por: Caio
"""
import random 
import numpy as np
import matplotlib.pyplot as plt 
import time

def simulacao(n,L):
    """Dado um numero de elemntos de tamanho l e comprimento 1, essa funcao 
    deposita os elementos aleatoriamente nas colunas obedecendo certas
    condicoes"""
    start_time = time.time()
    matriz = np.zeros([n,L]) #Comecamos com todas as linhas e colunas zeradas (criamos uma matriz com o numero de colunas L e linas n)

    for t in range(n):
        i = random.randint(0,L-1) #Para cada instante de tempo t, ela gera o valor i de uma coluna
        # O que o programa fazia antes está condensado na função nova_posicao pra ficar mais conciso.
        posicao_nova = nova_posicao(matriz,i)
        matriz[posicao_nova,i] = 1 #Novo elemento adicionado
        
    
    print("--- %s Segundos ---" % (time.time() - start_time))
    matriz = matriz[~(matriz == 0).all(1)] #Retira todas as linhas da matriz que tem apenas 0(e são excedentes)
    fig, ax = plt.subplots() #define a figura para o plot
    ax.matshow(matriz) #plota matrix no ax
    ax.invert_yaxis() #inverte o eixo y no plot
    ax.xaxis.tick_bottom() #trazendo os ticks do eixo x pra baixo.
    return

# Defini uma nova função apenas pegando o código abaixo e colocando dentro dela pra ficar mais limpo o código do plot.
def nova_posicao(matriz,i):
    l_atual,l_seguinte,l_anterior = (0,0,0)
    L=matriz.shape[1]
    # h(i-1,t-1): pegando a altura anteior (posicao)
    coluna_anterior = list(matriz[:,i-1])
    if 1 in coluna_anterior:
        list.reverse(coluna_anterior) # Ele só vai mudar o tamnaho "l" se encontrar algum valor diferente de 0 na lista, caso contrário, a altura é 0
        l_anterior = len(coluna_anterior) - list.index(coluna_anterior,1)

            
    # h(i+1,t-1):
    if i != L-1:
        coluna_seguinte = list(matriz[:,i+1])
        if 1 in coluna_seguinte:
            list.reverse(coluna_seguinte)
            l_seguinte = len(coluna_seguinte) - list.index(coluna_seguinte,1)
    else:
        coluna_seguinte = list(matriz[:,0])
        if 1 in coluna_seguinte:
            list.reverse(coluna_seguinte)
            l_seguinte = len(coluna_seguinte) - list.index(coluna_seguinte,1)
            
    # h(i,t-1):
    coluna_atual = list(matriz[:,i])
    if 1 in coluna_atual:
        list.reverse(coluna_atual)
        l_atual = len(coluna_atual) - list.index(coluna_atual,1)
    
    posicao_nova = max(l_atual,l_seguinte,l_anterior)
    return posicao_nova