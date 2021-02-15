#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:33:20 2021

@author: gabriella
"""

import random 
import numpy as np
import matplotlib.pyplot as plt

def tamanho_matrizes(matriz,indice_linha,indice_coluna,colunas,linhas):
    lista_tamanho = []
    altura = 0
    
    if indice_linha > linhas - 1:
        indice_linha = 0
    if indice_coluna > colunas - 1:
        indice_coluna = 0
    for numero in matriz[indice_linha,indice_coluna,:]: #le os numeros daquela linha e coluna 
        list.append(lista_tamanho,numero) #cria uma lista com esses numeros
    if 1 in lista_tamanho:
        list.reverse(lista_tamanho)
        altura = len(lista_tamanho) - list.index(lista_tamanho,1) #pega a altura se existir um numero 1 ali
    return altura
    
        
    


def KPZ_superficie(n,linhas,colunas): #Lembrando que linhas x colunas <= n
    """Essa funcao e uma tentativa de reproduzir o metodo KPZ em 2D dado o numero de particulas e o numero de linhas e colunas
    da matriz que representa a malha 2D"""
    matriz = np.zeros([linhas,colunas,n]) #Cria uma matriz zerada de linhas, colunas e "aluras"
    x,y,z = [], [], []
    for t in range (n+1):
        indice_linha, indice_coluna = random.randint(0,linhas-1), random.randint(0,colunas-1)
        posicao_nova_em_z = max(tamanho_matrizes(matriz, indice_linha, indice_coluna,colunas,linhas), tamanho_matrizes(matriz, indice_linha + 1, indice_coluna,colunas,linhas), tamanho_matrizes(matriz, indice_linha + 1, indice_coluna - 1,colunas,linhas), tamanho_matrizes(matriz, indice_linha, indice_coluna - 1,colunas,linhas),
                                tamanho_matrizes(matriz, indice_linha - 1, indice_coluna + 1,colunas,linhas), tamanho_matrizes(matriz, indice_linha - 1, indice_coluna,colunas,linhas),
                                tamanho_matrizes(matriz, indice_linha - 1, indice_coluna + 1,colunas,linhas), tamanho_matrizes(matriz, indice_linha, indice_coluna + 1,colunas,linhas), tamanho_matrizes(matriz, indice_linha +1, indice_coluna + 1,colunas,linhas))
        matriz[indice_linha, indice_coluna, posicao_nova_em_z] = 1
    
    # Checa cada linha e cada coluna nesses 2 loops
    for i in range(linhas):
        for n in range(colunas):
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
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x,y,z)
    return matriz
    
    
    