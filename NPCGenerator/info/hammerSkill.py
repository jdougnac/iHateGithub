from NPCGenerator.info.hammerOrdSkill import ordSkill
def skill(career,y):
    firstList=career.split('@') #this divides it into talents and skills    
    skillList=firstList[0].split(',')[1:]
    skillList.remove('') #this leaves us with a clean skill list
    
    
    talentList=firstList[1].split(',')
    talentList.remove('') #this leaves us with a clean talent list   
    
    if y==1:
        skills=ordSkill(skillList)
        return(skills)
    elif y==0:
        talents=ordSkill(talentList) 
        return(talents)


