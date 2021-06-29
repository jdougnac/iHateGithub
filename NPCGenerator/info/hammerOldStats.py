def oldStats(currentCar,oldCars):
    compList=[]
    firstComp=[]
    for item in currentCar[32:44]:
        firstComp.append(int(item))
    d=open("NPCGenerator/info/careerStats.txt","r")
    f=(d.readlines())
    s=0
    for career in oldCars:
        s=0
        del compList[:]
        for line in f:
            if career in line:
                for ittem in line[32:43]:
                    compList.append(int(ittem))
        for value in compList:
            try:
                if s<len(firstComp):
                    if value>firstComp[s]:
                        firstComp[s]=value
            except IndexError:
                print("error, firstComp is",firstComp)
                print("s es",s)
            s+=1
    return(firstComp)
