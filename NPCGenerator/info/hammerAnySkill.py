import random
def anySkill(file,numer):
    d=open('NPCGenerator/info/'+file,"r")
    f=(d.readlines())
    finalList=[]
    anyList=random.sample(f,numer)
    
    for item in anyList:
        itemNoLine = item.strip('\n')
        finalList.append(itemNoLine)
    d.close
    return finalList





