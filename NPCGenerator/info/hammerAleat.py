import random
def aleatory(file):
    d=open('NPCGenerator/info/'+file,"r")
    f=(d.readlines())
    z=random.choice(f)
    d.close
    return(z)
