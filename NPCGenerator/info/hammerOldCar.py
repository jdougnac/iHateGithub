import random
def carOld(career,powerLevel):    
    currCareer=career
    u=0
    indPower=int(powerLevel)-1
    prevCareer=[]  
    commas=[]
    entTemp=[]
    d=open("NPCGenerator/info/careerList.txt","r")
    f=(d.readlines())
    while indPower!=0:
        indPower=indPower-1        
        for line in f:
            if currCareer in line[0:29]:
                entTemp=line.split(",")
                del entTemp[0]
                del entTemp[-1]
                currCareer=random.choice(entTemp)
                prevCareer.append(currCareer)              
    d.close    
    return(prevCareer)


