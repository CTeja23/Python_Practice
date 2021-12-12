
def N(vertex,network):
    c = 0
    l = []
    for i in network[vertex]:
        if i == 1 :
         l.append(c)
        c+=1   
    return l 


max_cliq = list()

def bronk(r,p,x,network):
    
    if len(p) == 0 and len(x) == 0:
        
        max_cliq.append(r)

    for vertex in p[:]:
        r_new = r[::]
        r_new.append(vertex)
        p_new = [val for val in p if val in N(vertex,network)] # p intersects N(vertex)
        x_new = [val for val in x if val in N(vertex,network)] # x intersects N(vertex)
        bronk(r_new,p_new,x_new,network)
        p.remove(vertex)
        x.append(vertex)

 



    

def clickcounter(network):

    x = bronk([],[i for i in range(len(network[0]))],[],network)
    

    cliq = list()
    for lst in max_cliq:
        for num in lst:
            cliq.append(num)

    max_cliq.clear()


    c = list()
    for i in range(len(network[0])):
        c.append(cliq.count(i))


    return c




print(clickcounter([[0,1,1,0,0,0,0],
                [1,0,1,1,0,0,0],
                [1,1,0,0,0,0,0],
                [0,1,0,0,1,1,1],
                [0,0,0,1,0,1,0],
                [0,0,0,1,1,0,1],
                [0,0,0,1,0,1,0]]))

print(clickcounter([[0,1,0,0,0,0,1],
                [1,0,0,0,0,0,1],
                [0,0,0,1,0,0,1],
                [0,0,1,0,0,0,1],
                [0,0,0,0,0,1,1],
                [0,0,0,0,1,0,1],
                [1,1,1,1,1,1,0]]))


