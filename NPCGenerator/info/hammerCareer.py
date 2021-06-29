import random
from NPCGenerator.info.hammerAleat import aleatory


def career(race, nation, magic, isChaos):
    #magic 0 == random
    #magic 1 == magic
    #magic 2 == nonmagic
    print('********')
    print(race, nation, magic, isChaos)
    print('********')
    race = race.strip('\n')
    nation = nation.strip('\n')
    if isChaos == 0:
        if race=="Dwarf":
            rand=random.randint(1,12)
            if (rand==12 and magic != 2) or magic ==1:
                return ("carDwarfMagic")
            else:
                return("carDwarf")
        elif race=="Elf":
            rand=random.randint(1,7)
            if (rand==7 and magic != 2) or magic ==1:
                return ("carElfMagic")
            else:
                return("carElf")         
        elif race=="Halfling":
            return("carHalfling")        
        elif nation=="Kislev":
            rand=random.randint(1,8)
            if (rand==8 and magic != 2) or magic ==1: 
                return ("carKislevMagic")
            else:
                return("carKislev")
        elif nation=="Bretonnia":
            rand=random.randint(1,8)
            if (rand==8 and magic != 2) or magic ==1:
                return ("carMagic")
            else:
                return("carBretonnia")             
        elif nation=="Estalia" or nation=="Tilea":
            rand=random.randint(1,8)
            if (rand==8 and magic != 2) or magic ==1:
                return ("carMagic")
            else:
                return("carEstalia")
        else:
            rand=random.randint(1,8)
            if (rand==8 and magic != 2) or magic ==1:
                return ("carMagic")
            else:
                return("carEmpire")
    else:
        rand = random.randint(1,6)
        if (rand==8 and magic != 2) or magic ==1:
            return ("carChaosMagic")
        else:
            return("carChaos")
def career2(a,b):
    b = str(b)
    career = aleatory(a+b+".txt")
    career = career[:29]
    d=open("NPCGenerator/info/careerStats.txt","r")
    careerList=(d.readlines())    
    for item in careerList:
        if career in item:
            return item    
    print('ERROR HAMMERCAREER',career,'z')
def career3(a,b):
    b = str(b)
    return(a+b+".txt")
