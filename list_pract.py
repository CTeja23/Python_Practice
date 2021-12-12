graph = [[0,1,1,0,0,0,0],[1,0,1,1,0,0,0],[1,1,0,0,0,0,0],[0,1,0,0,1,1,1],[0,0,0,1,0,1,0],[0,0,0,1,1,0,1],[0,0,0,1,0,1,0]]


#function determines the neighbors of a given vertex
def N(vertex):
    c = 0
    l = []
    for i in graph[vertex]:
        if i == 1 :
         l.append(c)
        c+=1   
    return l 

#the Bron-Kerbosch recursive algorithm

# global max_cliq


max_cliq = list()

def bronk(r,p,x):
    if len(p) == 0 and len(x) == 0:
        max_cliq.append(r)
    for vertex in p[:]:
        r_new = r[::]
        r_new.append(vertex)
        p_new = [val for val in p if val in N(vertex)] # p intersects N(vertex)
        x_new = [val for val in x if val in N(vertex)] # x intersects N(vertex)
        bronk(r_new,p_new,x_new)
        p.remove(vertex)
        x.append(vertex)


bronk([], [0,1,2,3,4,5,6], [])


print(max_cliq)