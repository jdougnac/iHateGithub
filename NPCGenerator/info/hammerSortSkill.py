from NPCGenerator.info.hammerOrdSkill import ordSkill
def sortSkill(lista,x):
    lista2=[]
    lista = [z.strip(' ') for z in lista]
    lista = [z.strip("\n") for z in lista]
    h=[]
    if x==0:
        for item in lista:
            if item not in h:
                h.append(item)
        lista=h
    if x==1:
        for item in lista:
            g=lista.count(item)
            if g ==1:
                lista2.append(item)
            elif g==2:                
                item2= ''.join(('',item,' +10'))
                lista2.append(item2)
            elif g>=3:
                item2= ''.join(('',item,' +20'))
                lista2.append(item2)
        lista = list( dict.fromkeys(lista2))

    lista.sort()
    return(lista)
