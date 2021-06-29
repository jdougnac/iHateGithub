import random
def stats(race,prevAdvances,talents):
    ws=0
    bs=0
    strength=0
    toughness=0
    agility=0
    intelligence=0
    willpower=0
    fellowship=0
    wounds=0
    attacks=1
    movement=0
    fatePoints=0
    magic=0
    wound=random.randint(1,10)
    fate=random.randint(1,10)        
    if race=="Dwarf" or race=="Dwarf\n":
        ws=random.randint(1,10)+random.randint(1,10)+30
        bs=random.randint(1,10)+random.randint(1,10)+20
        strength=random.randint(1,10)+random.randint(1,10)+20
        toughness=random.randint(1,10)+random.randint(1,10)+30
        agility=random.randint(1,10)+random.randint(1,10)+10
        intelligence=random.randint(1,10)+random.randint(1,10)+20
        willpower=random.randint(1,10)+random.randint(1,10)+20
        fellowship=random.randint(1,10)+random.randint(1,10)+10
        if wound==1 or wound ==2 or wound==3:
            wounds=11
        elif wound==4 or wound==5 or wound==6:
            wounds=12
        elif wound==7 or wound ==8 or wound==9:
            wounds=13
        elif wound==10:
            wounds=14
        movement=3
        if fate==1 or fate==2 or fate==3 or fate==4:
            fatePoints=1
        elif fate==5 or fate==6 or fate==7:
            fatePoints=2
        elif fate==8 or fate==9 or fate==10:
            fatePoints=3  
    elif race=="Elf\n" or race == "Elf":
        ws=random.randint(1,10)+random.randint(1,10)+20
        bs=random.randint(1,10)+random.randint(1,10)+30
        strength=random.randint(1,10)+random.randint(1,10)+20
        toughness=random.randint(1,10)+random.randint(1,10)+20
        agility=random.randint(1,10)+random.randint(1,10)+30
        intelligence=random.randint(1,10)+random.randint(1,10)+20
        willpower=random.randint(1,10)+random.randint(1,10)+20
        fellowship=random.randint(1,10)+random.randint(1,10)+20
        if wound==1 or wound ==2 or wound==3:
            wounds=9
        elif wound==4 or wound==5 or wound==6:
            wounds=10
        elif wound==7 or wound ==8 or wound==9:
            wounds=11
        elif wound==10:
            wounds=12  
        movement=5
        if fate==1 or fate==2 or fate==3 or fate==4:
            fatePoints=1
        elif fate==5 or fate==6 or fate==7:
            fatePoints=2
        elif fate==8 or fate==9 or fate==10:
            fatePoints=2        
    elif race=="Halfling\n" or race == "Halfling":
        ws=random.randint(1,10)+random.randint(1,10)+10
        bs=random.randint(1,10)+random.randint(1,10)+30
        strength=random.randint(1,10)+random.randint(1,10)+10
        toughness=random.randint(1,10)+random.randint(1,10)+10
        agility=random.randint(1,10)+random.randint(1,10)+30
        intelligence=random.randint(1,10)+random.randint(1,10)+20
        willpower=random.randint(1,10)+random.randint(1,10)+20
        fellowship=random.randint(1,10)+random.randint(1,10)+30
        if wound==1 or wound ==2 or wound==3:
            wounds=8
        elif wound==4 or wound==5 or wound==6:
            wounds=9
        elif wound==7 or wound ==8 or wound==9:
            wounds=10
        elif wound==10:
            wounds=11 
        movement=4
        if fate==1 or fate==2 or fate==3 or fate==4:
            fatePoints=2
        elif fate==5 or fate==6 or fate==7:
            fatePoints=2
        elif fate==8 or fate==9 or fate==10:
            fatePoints=3          
    elif race=="Human\n" or race =="Human":
        ws=random.randint(1,10)+random.randint(1,10)+20
        bs=random.randint(1,10)+random.randint(1,10)+20
        strength=random.randint(1,10)+random.randint(1,10)+20
        toughness=random.randint(1,10)+random.randint(1,10)+20
        agility=random.randint(1,10)+random.randint(1,10)+20
        intelligence=random.randint(1,10)+random.randint(1,10)+20
        willpower=random.randint(1,10)+random.randint(1,10)+20
        fellowship=random.randint(1,10)+random.randint(1,10)+20
        if wound==1 or wound ==2 or wound==3:
            wounds=10
        elif wound==4 or wound==5 or wound==6:
            wounds=11
        elif wound==7 or wound ==8 or wound==9:
            wounds=12
        elif wound==10:
            wounds=13
        movement=4
        if fate==1 or fate==2 or fate==3 or fate==4:
            fatePoints=2
        elif fate==5 or fate==6 or fate==7:
            fatePoints=3
        elif fate==8 or fate==9 or fate==10:
            fatePoints=3
          
    ws+=prevAdvances[0]*5
    bs+=prevAdvances[1]*5
    strength+=prevAdvances[2]*5
    toughness+=prevAdvances[3]*5
    agility+=prevAdvances[4]*5
    intelligence+=prevAdvances[5]*5
    willpower+=prevAdvances[6]*5
    fellowship+=prevAdvances[7]*5
    attacks+=prevAdvances[8]
    wounds+=prevAdvances[9]
    movement+=prevAdvances[10]
    magic+=prevAdvances[11]
    for i in range(len(talents)):
        if "Warrior Born" in talents[i]:
            ws+=5
        elif "Fleet Footed" in talents[i]:
            movement+=1
        elif "Hardy" in talents[i]:
            wounds+=1
        elif "Lightning Reflexes" in talents[i]:
            agility+=5
        elif "Marksman" in talents[i]:
            bs+=5
        elif "Savvy" in talents[i]:
            intelligence+=5
        elif "Suave" in talents[i]:
            fellowship+=5
        elif "Very Resilient" in talents[i]:
            toughness+=5
        elif "Very Strong" in talents[i]:
            strength+=5
    stats = [ws, bs, strength, toughness, agility, intelligence, willpower, fellowship, attacks, wounds, movement, magic, fatePoints]
    return stats
