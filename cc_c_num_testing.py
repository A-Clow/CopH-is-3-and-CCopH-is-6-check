# -*- coding: utf-8 -*-
"""
This code is to test if an input graph $H = (V,E)$ has cop number $k$ for graphs we know have attacking cop number at least $2k$. 
At least for now the goal will be to check in the case that $k = 3$ where our graphs H are G^2 - E for a $(3,9)$-cage $G$. 
Our results are the following.

c(H_1)=3

c(H_2)=3

c(H_3)=3

c(H_4)=3

c(H_5)=3

c(H_6)=3

c(H_7)=3

c(H_8)=3

c(H_9)=3

c(H_10)=3

c(H_11)=3

c(H_12)=3

c(H_13)=3

c(H_14)=3

c(H_15)=3

c(H_16)=3

c(H_17)=3

c(H_18)>3

A.Clow
"""

!pip install cop-number
import networkx as nx
import matplotlib.pyplot as plt
from cop_number.cop import copk,cop_num

"""We are specfically interested in checking the cop number of graphs constructed from $(3,9)$-cages. As such I will include the full list of $(3,9)$-cages stroed as graphs in networkx below.

This is not original work in the sense that the list of $(3,9)$-cages can be found at http://users.cecs.anu.edu.au/~bdm/papers/ninecage.pdf

What is original work is generating these graphs as networkx objects and considering the graphs $G^2-E$.
To this end we write the next bit of code to create all 18 $(3,9)$-cages as networkx objects, along with $G^2-E$ for each $(3,9)$-cage, as as networkx objects.
"""

# This cell generates all 18 (3,9)-cages and all graph H = G^2 - E where G is a (3,9)-cage as objects in networkx
# The list of graphs H is stored as a list, named HList

# This function takes an integer n
# and will return a list containing all tuples (i,i+1) mod n
def cycle_generator(n):
  i =1
  L=[]
  while i <= n-1:
   L.append((i,i+1))
   i += 1
  L.append((n,1))

  return L

# This function will take a graph G = (V,E) of girth at least 5 stored as an object in networkx
# and will return H = G^2 - E stored as an object in networkx

def square_deleteOG(G):

  Vertices = list(G)
  H_Edges = []
  H = nx.Graph()

  sp = dict(nx.all_pairs_shortest_path_length(G))

  for u in Vertices:
    for v in Vertices:
      if sp[u][v] == 2:
        H_Edges.append((u,v))

  H.add_edges_from(H_Edges)
  return H

Cycle_List = cycle_generator(58)


EList_1 = [(1,9), (2,27), (3,42), (4,13), (5,47), (6,55), (7,34), (8,20), (10,39), (11,52), (12,31), (14,22),
(15,36), (16,54), (17,41), (18,48), (19,29), (21,44), (23,57), (24,40), (25,33), (26,53), (28,37), (30,56), (32,45),
(35,50), (38,46), (43,51), (49,58)]

G_1 = nx.Graph()
G_1.add_edges_from(Cycle_List)
G_1.add_edges_from(EList_1)
H_1 = square_deleteOG(G_1)



EList_2 = [(1,9), (2,25), (3,42), (4,39), (5,48), (6,34), (7,15), (8,44), (10,27), (11,49), (12,32), (13,38),
(14,56), (16,51), (17,26), (18,42), (19,58), (20,36), (21,29), (22,50), (23,40), (24,33), (25,46), (28,55), (31,43),
(35,53), (37,45), (41,54), (47,57)]

G_2 = nx.Graph()
G_2.add_edges_from(Cycle_List)
G_2.add_edges_from(EList_2)
H_2 = square_deleteOG(G_2)


EList_3 = [(1,9), (2,16), (3,43), (4,50), (5,38), (6,55), (7,46), (8,27), (10,22), (11,32), (12,48), (13,37),
(14,28), (15,54), (17,33), (18,39), (19,47), (20,29), (21,52), (23,44), (24,56), (25,49), (26,40), (30,57), (31,42),
(34,51), (35,45), (36,58), (41,53)]

G_3 = nx.Graph()
G_3.add_edges_from(Cycle_List)
G_3.add_edges_from(EList_3)
H_3 = square_deleteOG(G_3)



EList_4 = [(1, 9), (2, 44), (3, 20), (4, 37), (5, 13), (6, 47), (7, 53), (8, 23), (10, 30), (11, 50), (12, 41),
(14, 26), (15, 58), (16, 32), (17, 52), (18, 40), (19, 28), (21, 49), (22, 33), (24, 39), (25, 45), (27, 35), (29, 55),
(31, 46), (34, 42), (36, 51), (38, 56), (43, 54), (48, 57)]

G_4 = nx.Graph()
G_4.add_edges_from(Cycle_List)
G_4.add_edges_from(EList_4)
H_4 = square_deleteOG(G_4)


EList_5 = [(1, 9), (2, 27), (3, 17), (4, 46), (5, 38), (6, 52), (7, 33), (8, 42), (10, 22), (11, 37), (12, 54),
(13, 45), (14, 32), (15, 50), (16, 41), (18, 55), (19, 34), (20, 44), (21, 51), (23, 31), (24, 47), (25, 40), (26, 53),
(28, 36), (29, 43), (30, 56), (35, 48), (39, 57), (49, 58)]

G_5 = nx.Graph()
G_5.add_edges_from(Cycle_List)
G_5.add_edges_from(EList_5)
H_5 = square_deleteOG(G_5)



EList_6 = [(1, 9), (2, 37), (3, 48), (4, 13), (5, 28), (6, 34), (7, 19), (8, 51), (10, 30), (11, 40), (12, 22),
(14, 52), (15, 43), (16, 31), (17, 25), (18, 39), (20, 46), (21, 55), (23, 35), (24, 50), (26, 58), (27, 45), (29, 54),
(32, 47), (33, 57), (36, 44), (38, 53), (41, 49), (42, 56)]
G_6 = nx.Graph()
G_6.add_edges_from(Cycle_List)
G_6.add_edges_from(EList_6)
H_6 = square_deleteOG(G_6)



EList_7 = [(1, 9), (2, 45), (3, 38), (4, 54), (5, 13), (6, 48), (7, 25), (8, 31), (10, 19), (11, 40), (12, 34),
(14, 28), (15, 51), (16, 37), (17, 43), (18, 55), (20, 47), (21, 29), (22, 36), (23, 53), (24, 44), (26, 39), (27, 56),
(30, 42), (32, 52), (33, 46), (35, 57), (41, 49), (50, 58)]

G_7 = nx.Graph()
G_7.add_edges_from(Cycle_List)
G_7.add_edges_from(EList_7)
H_7 = square_deleteOG(G_7)



EList_8 = [(1, 9), (2, 33), (3, 39), (4, 25), (5, 53), (6, 47), (7, 19), (8, 42), (10, 51), (11, 37), (12, 46),
(13, 21), (14, 41), (15, 26), (16, 32), (17, 56), (18, 38), (20, 29), (22, 34), (23, 50), (24, 44), (27, 36), (28, 58),
(30, 52), (31, 45), (35, 54), (40, 49), (43, 55), (48, 57)]

G_8 = nx.Graph()
G_8.add_edges_from(Cycle_List)
G_8.add_edges_from(EList_8)
H_8 = square_deleteOG(G_8)



EList_9 = [(1, 9), (2, 52), (3, 23), (4, 13), (5, 34), (6, 18), (7, 46), (8, 38), (10, 29), (11, 20), (12, 55),
(14, 43), (15, 37), (16, 31), (17, 25), (19, 51), (21, 36), (22, 47), (24, 40), (26, 56), (27, 35), (28, 44), (30, 49),
(32, 54), (33, 41), (39, 50), (42, 58), (45, 53), (48, 57)]

G_9 = nx.Graph()
G_9.add_edges_from(Cycle_List)
G_9.add_edges_from(EList_9)
H_9 = square_deleteOG(G_9)



EList_10 = [(1, 9), (2, 41), (3, 34), (4, 28), (5, 17), (6, 38), (7, 45), (8, 22), (10, 53), (11, 27), (12, 37),
(13, 48), (14, 42), (15, 31), (16, 24), (18, 54), (19, 47), (20, 40), (21, 29), (23, 35), (25, 50), (26, 44), (30, 57),
(32, 52), (33, 46), (36, 56), (39, 51), (43, 55), (49, 58)]

G_10 = nx.Graph()
G_10.add_edges_from(Cycle_List)
G_10.add_edges_from(EList_10)
H_10 = square_deleteOG(G_10)



EList_11 = [(1, 9), (2, 15), (3, 38), (4, 49), (5, 20), (6, 55), (7, 34), (8, 41), (10, 22), (11, 48), (12, 54),
(13, 28), (14, 43), (16, 33), (17, 47), (18, 40), (19, 29), (21, 44), (23, 32), (24, 39), (25, 56), (26, 50), (27, 35),
(30, 58), (31, 52), (36, 45), (37, 53), (42, 51), (46, 57)]

G_11 = nx.Graph()
G_11.add_edges_from(Cycle_List)
G_11.add_edges_from(EList_11)
H_11 = square_deleteOG(G_11)




EList_12 = [(1, 9), (2, 41), (3, 14), (4, 46), (5, 33), (6, 18), (7, 38), (8, 23), (10, 28), (11, 52), (12, 20),
(13, 37), (15, 24), (16, 50), (17, 57), (19, 42), (21, 47), (22, 31), (25, 54), (26, 34), (27, 48), (29, 43), (30, 56),
(32, 51), (35, 58), (36, 44), (39, 55), (40, 49), (45, 53)]

G_12 = nx.Graph()
G_12.add_edges_from(Cycle_List)
G_12.add_edges_from(EList_12)
H_12 = square_deleteOG(G_12)



EList_13 = [(1, 9), (2, 33), (3, 41), (4, 24), (5, 17), (6, 45), (7, 30), (8, 38), (10, 19), (11, 53), (12, 27),
(13, 47), (14, 22), (15, 58), (16, 36), (18, 49), (20, 43), (21, 32), (23, 51), (25, 56), (26, 37), (28, 42), (29, 50),
(31, 55), (34, 46), (35, 52), (39, 48), (40, 54), (44, 57)]

G_13 = nx.Graph()
G_13.add_edges_from(Cycle_List)
G_13.add_edges_from(EList_13)
H_13 = square_deleteOG(G_13)



EList_14 = [(1, 9), (2, 27), (3, 41), (4, 50), (5, 36), (6, 55), (7, 20), (8, 47), (10, 52), (11, 35), (12, 42),
(13, 29), (14, 49), (15, 58), (16, 24), (17, 40), (18, 34), (19, 28), (21, 43), (22, 51), (23, 31), (25, 46), (26, 54),
(30, 38), (32, 56), (33, 48), (37, 45), (39, 53), (44, 57)]

G_14 = nx.Graph()
G_14.add_edges_from(Cycle_List)
G_14.add_edges_from(EList_14)
H_14 = square_deleteOG(G_14)



EList_15 = [(1, 9), (2, 22), (3, 51), (4, 45), (5, 17), (6, 28), (7, 54), (8, 48), (10, 42), (11, 19), (12, 27),
(13, 46), (14, 53), (15, 23), (16, 39), (18, 34), (20, 55), (21, 30), (24, 43), (25, 49), (26, 57), (29, 37), (31, 47),
(32, 41), (33, 52), (35, 58), (36, 44), (38, 50), (40, 56)]

G_15 = nx.Graph()
G_15.add_edges_from(Cycle_List)
G_15.add_edges_from(EList_15)
H_15 = square_deleteOG(G_15)



EList_16 = [(1, 9), (2, 50), (3, 38), (4, 31), (5, 23), (6, 15), (7, 45), (8, 28), (10, 33), (11, 21), (12, 39),
(13, 55), (14, 49), (16, 35), (17, 41), (18, 58), (19, 30), (20, 47), (22, 52), (24, 57), (25, 34), (26, 48), (27, 40),
(29, 54), (32, 43), (36, 53), (37, 46), (42, 51), (44, 56)]

G_16 = nx.Graph()
G_16.add_edges_from(Cycle_List)
G_16.add_edges_from(EList_16)
H_16 = square_deleteOG(G_16)



EList_17 = [(1, 9), (2, 26), (3, 35), (4, 21), (5, 41), (6, 16), (7, 31), (8, 52), (10, 43), (11, 19), (12, 34),
(13, 50), (14, 27), (15, 45), (17, 57), (18, 38), (20, 29), (22, 51), (23, 44), (24, 32), (25, 39), (28, 54), (30, 47),
(33, 56), (36, 46), (37, 53), (40, 49), (42, 55), (48, 58)]

G_17 = nx.Graph()
G_17.add_edges_from(Cycle_List)
G_17.add_edges_from(EList_17)
H_17 = square_deleteOG(G_17)



EList_18 = [(1, 9), (2, 35), (3, 49), (4, 23), (5, 13), (6, 28), (7, 42), (8, 19), (10, 46), (11, 39), (12, 33),
(14, 52), (15, 58), (16, 25), (17, 48), (18, 37), (20, 53), (21, 32), (22, 45), (24, 40), (26, 34), (27, 54), (29, 38),
(30, 50), (31, 57), (36, 44), (41, 56), (43, 51), (47, 55)]

G_18 = nx.Graph()
G_18.add_edges_from(Cycle_List)
G_18.add_edges_from(EList_18)
H_18 = square_deleteOG(G_18)


HList = [H_1,H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9,H_10,H_11,H_12,H_13,H_14,H_15,H_16,H_17,H_18]

"""This next code is to verify that for all $i \neq j$, $H_i \not\cong H_j$."""

i=0
while i <= 17:
  H = HList[i]
  NewList = list(range(18))
  NewList.remove(i)
  for j in NewList:
    G = HList[j]
    A = nx.is_isomorphic(G,H)
    if A == True:
      print(i, " is ismorphic to ", j)
  i += 1
  print(i)

"""In order to check the if cop nuber of each $H_i$ is equal to $3$ we use code from https://github.com/Jabbath/Cop-Number

The function copk(H,k) returns true if $c(H) > k$ and false otherwise.

We note that the following function is included so that a reader can easily run the check themselves. We note however that it may be better to run the code in parallel for each $H_i$, rather than as a loop as we have written it here, as each check is computationally hard.
"""

i=0
while i <= 17:
  i += 1
  k = copk(HList[i-1],3)
  print("H_",i, " has cop number > 3;", k)
