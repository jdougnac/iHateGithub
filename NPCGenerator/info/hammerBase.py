import random
from NPCGenerator.info.hammerAleat import aleatory

def race():
    raz=aleatory("race.txt")
    return(raz)
def nation(x):
    if x=="Dwarf" or x=="Dwarf\n":
       return(aleatory("origDwarf.txt"))
    elif x=="Human\n" or x == "Human":
        return(aleatory("origHuman.txt"))
    elif x=="Elf\n" or x == "Elf":
        return(aleatory("origElf.txt"))
    elif x=="Halfling\n" or x == "Halfling":
        return(aleatory("origHalfling.txt"))
def faith(y,x):
    if y=="Dwarf" or y=="Dwarf\n":
        fe=aleatory("feDwarf.txt")        
        return(fe)
    elif y=="Elf\n" or y =="Elf":
        fe=aleatory("feElf.txt")        
        return(fe)
    elif y=="Halfling\n" or y == 'Halfling':
        fe=aleatory("feHalfling.txt")        
        return(fe)
    elif x=="Kislev" or x =='Kislev\n':
        fe=aleatory("feKislev.txt")        
        return(fe)
    elif x=="Bretonnia\n" or x =='Bretonnia':
        fe=aleatory("feBretonnia.txt")        
        return(fe)
    elif x=="Albion\n" or x=="Albion":
        fe=aleatory("feAlbion.txt")        
        return(fe)
    elif x=="Estalia\n" or x=="Estalia":
        fe=aleatory("feEstalia.txt")        
        return(fe)
    elif x =="Norsca\n" or x =="Norsca":
        return random.choice(["Khorne", "Nurgle", "Slaanesh", "Tzeentch"])
    else:
        fe=aleatory("feEmpire.txt")        
        return(fe)

