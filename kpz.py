# -*- coding: utf-8 -*-
"""

Created on Sun Feb  7 12:18:20 2021

@author: Caio Encarnação
"""

import random as rdm
import matplotlib.pyplot as plt
import numpy as np

def vizinhanca(matriz,x,y):
    #Periodidicidade
    if x == matriz.shape[1]-1:
        x_1 = 0
    else:
        x_1 = x+1
    if y == matriz.shape[0]-1:
        y_1 = 0
    else: 
        y_1 = y+1
    #Checa todos os vizinhos da posição x,y.  
    fixar = False
    if (matriz[y_1,x_1] == 1 or matriz[y_1,x-1] == 1) or (matriz[y-1,x_1] == 1 or matriz[y-1,x-1] == 1):
        fixar = True
    return fixar

directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
#Nova versão do program de dla mudando condição de fixação de particula para aderir apenas caso haja particulas nos cantos e desconsiderando laterais.
def kpz(N=800,L=100,H=100):
    #Variável pra definir a quantidade de iterações
    Pontos = 0 
    #Criação da matriz.
    matriz = np.zeros((H,L)) 
    #Um valor do espaçamento  para até onde vamos ter o domínio do random walk. Andar por toda a matriz pode levar tempo demais.
    padding = 20 
    #Definimos que nosso domínio começa do centro da matriz.
    x, y = round(L/2), round(H/2)
    #Menores e maiores valores em x e y. Como começamos apenas com uma particula, eles são os mesmos.
    xMin, xMax = x, x
    yMin, yMax = y, y
    #Definimos os dominios do Random Walk. Os limites por onde a particula pode andar
    dominioMinX,dominioMaxX,dominioMinY,dominioMaxY = xMin - padding,xMax + padding,yMin - padding,yMax + padding
    #A partícula é inserida no sistema
    matriz[y,x] = 1
    
    while(Pontos < N):
        #Verificação se existem pontos vizinhos
        vizinho = False 
        start = rdm.choice([0,1,2,3]) 
        #Escolha do ponto inicial do Random Walk
        if start == 0: x, y = dominioMinX,int(rdm.uniform(dominioMinY,dominioMaxY))
        elif start == 1: x, y = dominioMaxX,int(rdm.uniform(dominioMinY,dominioMaxY))
        elif start == 2: x, y = int(rdm.uniform(dominioMinX,xMax)),dominioMinY
        else: x, y = int(rdm.uniform(dominioMinX,dominioMaxX)),dominioMaxY
        #Começa um random walk, checando se o ponto seguinte contem particula ou não.
        while not vizinho:
            #Escolhe o movimento de uma lista com 8 direções possiveis.
            dx,dy = rdm.choice(directions)
            #Determina onde será a nova posição x e y
            newX, newY = x + dx, y + dy
            #Peridiocidade. Se chegar no limite superior, trazemos para baixo e vice-verse.
            if newX>dominioMaxX: newX = dominioMinX
            if newX<dominioMinX: newX = dominioMaxX
            if newY>dominioMaxY: newY = dominioMinY
            if newY<dominioMinY: newY = dominioMaxY
            #Dessa vez a função vizinhança nos diz se há vizinhos relevantes da posição xy
            if vizinhanca(matriz,x,y):
                vizinho = True #Substitui valor de verdade para sair do loop
                matriz[y,x] = 1 #Adiciona particula na posição atual do Random Walk
                #Redefine o menor valor em x e y onde tem particulas
                if x > xMax: xMax = x
                if y > yMax: yMax = y
                if x < xMin: xMin = x
                if y < yMin: yMin = y
                #Com a nova posição das particulas, redefine os dominios do Random Walk se for preciso. Nunca ultrapassando os limites da matriz.
                dominioMinX = max([xMin - padding, 0])
                dominioMaxX = min([xMax + padding, L-1])                
                dominioMinY = max([yMin - padding, 0])                
                dominioMaxY = min([yMax + padding, H-1])
            #Caso não tenha particula, continua o random walk se movendo para a próxima posição.    
            else:
                x,y = newX, newY
        #Conta numero de pontos.
        Pontos+=1
    #Plota a posição de todas as particulas.    
    fig, ax = plt.subplots(figsize = (8,8))
    ax.matshow(matriz,interpolation='nearest')
    ax.axis('off')
    return matriz

