from NPCGenerator.info.hammerSkill import skill
def oldSkill(oldCar,x,variable):
    d=open("NPCGenerator/info/careerStats.txt","r")
    tempSkill=[]
    olSkills=[]
    f=(d.readlines())
    for carrera in oldCar:
        for line in f:
            if carrera in line[0:28]:
                tempSkill=skill(line,x)
                for item in tempSkill:
                    olSkills.append(item)
    for item in olSkills:
        variable.append(item)
