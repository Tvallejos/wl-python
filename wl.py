from igraph import *

def init_partition(g,init):
    return [ [init for i in range(len (g.vs))]]

def copy_partition(partition):
    partition_copy = [i for i in partition]
    return partition_copy

def list_eq(l1, l2):
    if(len(l1) == 0 & len(l2) == 0):
        return True
    else:
        return l1[0] == l2[0] and list_eq(l1[1:],l2[1:])

def wl_color(g,init):
    P = init_partition(g,init)
    i = 0
    while( True ):
        Pi = copy_partition(P[i])
        i+=1
        for v in g.vs:
            neighbors = list(map((lambda v: v.index), v.neighbors()))
            for idx in range(len(neighbors)):
                neighbors[idx] = P[i-1][neighbors[idx]]
            Pi[v.index] += hash(tuple(neighbors))
        if list_eq(partition_wc(P[i-1]),partition_wc(Pi)) or (i-10 > len(g.vs)):
            print('Number of iterations before returning: '+str(i))
            return [Pi[i] for i in range(len(Pi))]
        else:
            P.append(Pi)

def indexes(v,l):
    idxs = []
    for idx,val in enumerate(l):
        if val == v:
            idxs.append(idx)
    return tuple(idxs)


def partition(p):
    P = []
    for idx, color in enumerate(p):
        P.append((indexes(color,p),color))
    return list(set(P))

def partition_wc(p):
    P = partition(p)
    return list(map(lambda p: p[0],P))

def wl_partition(g):
    return partition(wl_color(g,0))

# G and G2 are not isomorphic and produce the same partition
# As they are fractionally isomorphic
G = Graph()
G.add_vertices(6)
G.add_edges([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)])

G2 = Graph()
G2.add_vertices(6)
G2.add_edges([(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)])

print(wl_partition(G))
print(wl_partition(G2))


# Frucht graph produce a non fine partition as is 3-regular
# Therefore it has a fractionally automorphism
Frucht = Graph.Famous('Frucht')
print(wl_partition(Frucht))


# Now we test a asymmetric and non regular graph
#         2
#         |
# 0 - 1 - 3 - 4 - 5 - 6

A = Graph()
A.add_vertices(7)
A.add_edges([(0,1),(3,2),(1,3),(3,4),(4,5),(5,6)])
print(wl_partition(A))

