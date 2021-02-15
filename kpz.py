# -*- coding: utf-8 -*-
"""
Tentando criar a parada que é 2D mas tem 3 dimensões. Deus tenha piedade de nós.

Created on Thu Feb 11 20:31:53 2021

@author: Caio
"""
import numpy as np
import matplotlib.pyplot as plt
import random as rdm

def kpz(N=500,l=10,c=10):
    """
    Dado numero de elementos, linhas e colunas de uma matriz, aloca particulas aleatóriamente
    seguindo as regras definidas na função altura.
    
    Uma particula não pode estar alocada do lado da outra, ela sempre está em cima de outra
    Ou estão se ligando pelas arestas.
    """
    # Temos uma matriz booleana, onde 0 indica um espaço SEM particula. 1 indica a presença de uma partícula.
    matriz = np.zeros((l,c,N))
    # Criamos uma figura e adicionamos eixos 3D nele para scatter. A visualização não está das melhores.
    fig = plt.figure(figsize = (6,6))
    ax = fig.add_subplot(111, projection='3d')
    x,y,z = [],[],[]
    
    for i in range(N):
        # Geramos o indice de linha e coluna que nos dirá o ponto do plano que iremos analisar
        # Checar explicação na função altura para melhor explicação do que está sendo feito.
        new_c,new_l = rdm.randint(0,c-1), rdm.randint(0,l-1)
        # Alterar o valor de verdade sobre a presença da particula na posição sorteada com a altura.
        # Definida pela função e suas regras.
        matriz[new_l,new_c,altura(matriz,new_l,new_c)] = 1
        
    #Pega a interface, isto é, a última particula da cada espaço da matriz[linha,coluna] para o plot
    # Checa cada linha e cada coluna nesses 2 loops
    for i in range(l):
        for n in range(c):
            # Transforma a coluna de particulas em uma lista
            column = list(matriz[i,n,:])
            # Checa se naquele espaço da matriz[i,n] tem alguma partícula
            if 1 in column:
                # Caso tenha, armazena o valor da coluna e da linha como x e y
                x.append(n)
                y.append(i)
                # Inverte a lista pra adicionar o indice da última particula como z
                list.reverse(column)
                z.append(len(column) - list.index(column,1)-1)
                
    ax.plot_trisurf(x,y,z)
    ax.set_xlabel('Linha') 
    ax.set_ylabel('Coluna') 
    ax.set_zlabel('Altura')
    # A figura é mostrada
    # A gente vê a figura, não consegue saber se deu certo ou errado e fica triste.
    plt.show()
    
    return 
    
def altura(matriz,l,c):
    
    """
    Parameters
    ----------
    matriz : np.array
        Matriz das particulas.
    l : int
        Índice da linha da matriz.
    c : int
        Índice da coluna da matriz.

    Returns
    -------
    h : int
        Altura da matriz.
    """
    # Imaginando a matriz como um plano, separado em varios pontos. Particulas vão se acumulando e criando colunas
    # que crescem desse plano sendo assim a terceira cordenada da matriz(esta que é tridimensional) apenas a altura
    # da coluna de particulas. Sendo assim matriz[l,c,h] se refere a altura h da coluna de particulas no ponto (l,c).
    # Espero que tenha ficado claro.
    
    listas = []
    indices = [0]*9
    
    # Dado um determinado ponto neste plano (l,c), varremos todas as colunas dos 8 pontos em volta
    # e do próprio ponto. Adiciona as coluna na variável "listas", convertendo-as a fim de usar
    # reverse mais adiante caso tenha 1 na coluna.
    
    # Varremos da linha anterior até a seguinte (l+(-1), l+0 e l+1)
    for m in range(-1,2):
        # Varremos da coluna anterior até a seguinte (c+(-1), c+0 e c+1)
        for n in range(-1,2):
            # Condições para garantir peridiocidade. Caso l+m seja maior que 
            # o maior indice de linha matriz(matriz.shape[0] - 1), o indice se torna 0 (análogo para coluna)
            if l+m > matriz.shape[0]-1: linha = 0
            else: linha = l+m
            if c+n > matriz.shape[1]-1: coluna = 0
            else: coluna = c+n
            # Converte a coluna de particulas(não confundir com indice de coluna da matriz) para uma lista 
            # E adicionamos esta lista a uma lista. Fazemos isso a fim de usar uma propriedade de listas.
            listas.append(list(matriz[linha,coluna,:]))
    
    # Como temos 9 pontos para checar as colunas de particulas, vamos ter 9 indices de altura.
    # Usamos reverse na lista para que list.index(1) nos dê o índice da ÚLTIMA ocorrência do
    # número 1 na lista. 
    for i in range(9):
        if 1 in listas[i]:
            list.reverse(listas[i])
            indices[i] = len(listas[i]) - list.index(listas[i],1)
        # Caso não tenha particula naquela coluna, não há nada a ser feito.
        # Como a indices é uma list de zeros, nada precisa ser feito
        else:
            continue
    # A altura é dada pelo maior dos indices de altura nesse espaço 3x3 do plano. Alocando a nova particula
    # sempre acima das demais neste espaço.
    return max(indices)