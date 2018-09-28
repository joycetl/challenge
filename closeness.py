#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
np.set_printoptions(threshold='nan')
#Declare lists 
node1=[]
node2=[]
node=[]
#Open the file edges in variable file_1
with open ("edges","r") as file_1:
    linhas=0
#Read each line called "arc"    
    for arc in file_1:
        linhas+=1
#Separate information in each line arc -- two integer numbers in this case -- and put in a vector arcs [first variable in line] [second variable in line]       
        arcs=arc.split()
#Take variables in vector arcs and put the 1st in list node1 and 2nd in list node2       
        node1.append(int(arcs[0]))
        node2.append(int(arcs[1]))
#Create a matrix of zeros of dimension ix2 
vert=np.zeros((linhas,2))
#Assign values for matrix vert (node1 and node2)
for j in range(0,linhas):
    vert[j][0]=node1[j]
    vert[j][1]=node2[j]
#Take maximum and minimum value of nodes
maxn=int(vert.max())
minn=int(vert.min())
numb=maxn-minn+1
numb=int(numb)
#Create a list called node with all diferent nodes from the file, from minimum to maximum
for j in range(minn,maxn+1):
    node.append(j)
#Create a matrix DIST - in which lines correspond to nodes and the columns correspond to the number of nodes that lie in the specific distance (distances go from 1 to (#nodes -1))  
#Example:
#DIST[0][3] --> # nodes that lie in a distance 4 (3 nodes in between) from the node in position [0] (first node)
#DIST[1][0] --> number of nodes that lie in a distance 1 (directed) from the second node (in position [1])
dist=np.zeros((numb,numb-1))
#Create a matrix CONEX- in which lines correspond to nodes and the columns correspond to the other nodes linked to it with a directed edge 
cont=0
conex=np.full((numb,numb-1),'none')

#########################################################################################################################
# Make matrix CONEX and first column of matrix DIST
#########################################################################################################################

for i in range (0,numb): #go through lines of vector node
    for j in range (0,linhas): # go through lines of file 'edge' (matrix vert)
            if vert[j][0] == node[i]:
                conex[i][cont]=vert[j][1]
                dist[i][0]=dist[i][0]+1
                cont+=1
            elif vert[j][1] == node[i]:
                conex[i][cont]=vert[j][0]
                cont+=1
                dist[i][0]=dist[i][0]+1
    dist[i][0]=int(cont) 
    cont=0
print(conex)

#########################################################################################################################
# SHORTEST PATH
#########################################################################################################################
#Set all distances = infinity
path=[1e9]*numb
for i in range (numb):
    path[i]=[1e9]*numb
    #print(path)
maxit=numb
cont=0


#for i in range (0,numb): #go through all nodes
#    initial = node[i]
#    path[i][i]=0
#    for j in range(0,numb): # go through all the other nodes
#        other = node(j)
#        if other != current:
#            for k in range(0,numb-1): #go through lines of CONEX
#                if conex(i,k) == other:
#                    path[i][conex[i][k]] = 1
#                else:
#                    for l in range(1,numb):
#                        while cont <=maxit and      






#########################################################################################################################
# Finish matrix DIST
#########################################################################################################################

#for i in range(0,numb): #go through lines of vector node
#for j in range (1,numb-1): #go through columns of DIST (starting on second column)
#    for i2 in range(0,numb):
#        for k in range (0,numb-1): # go through columns of CONEX    
#            if conex[i2+j-1][k] != 'none':
#                aux=int(conex[i2+j-1][k]) - 1
#                dist[i2][j]=int(dist[aux][j-1])+int(dist[i2][j])-1
#        print(dist)
#print(dist)




