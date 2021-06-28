import random
from NPCGenerator.info.hammerExp import experience
from NPCGenerator.info.hammerBase import *
from NPCGenerator.info.hammerCareer import career
from NPCGenerator.info.hammerCareer import career2
from NPCGenerator.info.hammerCareer import career3
from NPCGenerator.info.hammerStats import stats
from NPCGenerator.info.hammerSkill import skill
from NPCGenerator.info.hammerName import name
from NPCGenerator.info.hammerOldCar import carOld
from NPCGenerator.info.hammerOldSkill import oldSkill
from NPCGenerator.info.hammerSortSkill import sortSkill
from NPCGenerator.info.hammerOldStats import oldStats
from NPCGenerator.info.hammerRaceSkills import raceSkills




#for isMagic, as well as isChaos, 0 means it could go either way
#1 means that it will be a magic/ chaos career, and 2 means
#there won't be any chaos or magic careers

#cambiar a clase
class GenerateNPC:
    def __init__(self, raceDef, gender, level, isMagic,isChaos, careerDef):
        self.npc = []
        self.raceDef = raceDef
        self.gender = gender
        self.level = level
        self.isMagic = isMagic
        self.careerDef = careerDef
        self.isChaos = isChaos
        #self.createNPC(self, raceDef, gender, level, isMagic, careerDef, isChaos)
        self.createNPC(raceDef, gender, level, isMagic, isChaos, careerDef)
    def createNPC(self, raceDef, gender, level, isMagic, isChaos, careerDef):
        finalCareer=''
        if raceDef == '0':
            raceDef = int(raceDef)
        if careerDef == '0':
            print('bagong')
            careerDef = int(careerDef)
        if gender == '0':
            gender = int(gender)
        level = int(level)
        isMagic = int(isMagic)
        isChaos = int(isChaos)
        chaosChance = 0
        isNPCChaotic = 0
        chaosRoll = random.randint(1,100)
        if isChaos == 0:
            chaosChance = 10
        elif isChaos == 1:
            chaosChance = 100
        elif isChaos == 2:
            chaosChance = 0

        if chaosRoll <= chaosChance:
            isNPCChaotic = 1
        #if the selected career is one of the chaotic ones
        #(like cult acolyte or magus), isNPCChaotic turns to 1
        if careerDef != 0:
            if '240' in careerDef or '241' in careerDef or '242' in careerDef or '243' in careerDef or '244' in careerDef or '245' in careerDef or '246' in careerDef or '247' in careerDef or '248' in careerDef or '249' in careerDef or '250' in careerDef or '251' in careerDef or '252' in careerDef or '253' in careerDef or '254' in careerDef or '255' in careerDef or '256' in careerDef:
                isNPCChaotic = 1
        print('zz',raceDef, type(raceDef))
        if raceDef == 0:
            print('OIBNGKDJFGKJFG')
            NPCRace=race()
            NPCNation = nation(NPCRace)
            print(NPCRace, NPCNation)
            print('OIBNGKDJFGKJFG')
        elif "Empire" in raceDef:
            NPCRace="Human"
            NPCNation = random.choice(['Averland','Hochland','Middenland','Nordland','Ostermark','Ostland','Reikland','Stirland','Talabecland'])
        elif "Bretonnia" in raceDef:
            NPCRace = "Human"
            NPCNation = "Bretonnia"
        elif "Estalia" in raceDef:
            NPCRace = "Human"
            NPCNation = "Estalia"            
        elif "Kislev" in raceDef:
            NPCRace = "Human"
            NPCNation = "Kislev"
        elif "Norsca" in raceDef:
            NPCRace = "Human"
            NPCNation = "Norsca"
        else:
            NPCRace= raceDef
            NPCNation = nation(NPCRace)
            
        if gender == 0:
            NPCGender=random.choice(["male", "female"])
        else:
            NPCGender=gender
        if level == 0:
            NPCexperience=experience()
        else:
            NPCexperience=level    
        NPCMagic = isMagic
        print(NPCRace,NPCNation, NPCMagic, isNPCChaotic)
        NPCCareer=career(NPCRace,NPCNation, NPCMagic, isNPCChaotic)
        if careerDef == 0:
            finalCareer=career2(NPCCareer,NPCexperience)
        else:
 
            NPCexperience = careerDef[-1]
            print('ggggggggggggggggg')
            print('ggggggggggggggggg')
            print(careerDef,NPCexperience)
            print('ggggggggggggggggg')
            print('ggggggggggggggggg')            
            d=open("NPCGenerator/info/careerStats.txt","r")
            careerList=(d.readlines())    
            for item in careerList:                
                if careerDef[:-1] in item:
                    print('gong')
                    finalCareer = item
        oldCar = ''
        oldCar=carOld(finalCareer[0:28],NPCexperience)
       
        if '247Champion of Chaos' in finalCareer:
            oldCar.append(random.choice(['234Marauder','019Bailiff','026Bodyguard','029Bounty Hunter','031Cadet','039Cenobite','052Deepwatcher','065Exciseman','086Grave Warden','103Hunter','106Initiate','134Mercenary','145Noble','147Outlaw','149Outrider','156Pit Fighter','160Protagonist','166River Warden','167Road Warden','184Soldier','188Squire','198Temple Guardian','200Thug','225Wrecker','227Zealot']))
        elif '248Exalted Champion of Chaos' in finalCareer:
            oldCar.append('244Chaos Warrior')
            oldCar.append(random.choice(['234Marauder','019Bailiff','026Bodyguard','029Bounty Hunter','031Cadet','039Cenobite','052Deepwatcher','065Exciseman','086Grave Warden','103Hunter','106Initiate','134Mercenary','145Noble','147Outlaw','149Outrider','156Pit Fighter','160Protagonist','166River Warden','167Road Warden','184Soldier','188Squire','198Temple Guardian','200Thug','225Wrecker','227Zealot']))
            
        prevCareer=career3(NPCCareer,NPCexperience)
        NPCSkill=skill(finalCareer,1)
        oldSkill(oldCar,1,NPCSkill)
        NPCTalent=skill(finalCareer,0)
        
        #this chunk of code ensures races are corrected if we come across an
        #invalid combination (like human Slayer, for example)
        checkCareerRequirements = oldCar[:]
        checkCareerRequirements.append(finalCareer[:30])
        if (isNPCChaotic == 1 or isMagic ==1) and 'Halfling' in NPCRace:
            NPCRace = random.choice(['Elf','Elf','Human','Human','Human','Human','Human','Human','Dwarf','Dwarf','Dwarf'])
            NPCNation = nation(NPCRace)
        for item in checkCareerRequirements:
            if 'Slayer' in item or 'Runebearer' in item or 'Shieldbreaker' in item or 'Runesmith' in item or 'Runelord' in item:
                NPCRace = 'Dwarf'
                NPCNation = nation(NPCRace)
            elif 'Kithband' in item or 'Envoy' in item or 'Warhawk' in item or 'Wildkin' in item or 'Ghost Strider' in item or 'Wardancer' in item or 'Bladesinger' in item or 'Spellsinger' in item or 'Spellweaver' in item:
                NPCRace = 'Elf'
                NPCNation = nation(NPCRace)
            elif 'Handmaiden' in item:
                NPCRace = 'Elf'
                NPCNation = nation(NPCRace)
                NPCGender = 'female'
            elif "Hag" in item or "Ice" in item or "Wise Woman" in item:
                NPCRace = 'Human'
                NPCGender = 'female'
                NPCNation = 'Kislev'    
            elif "Grail Knight" in item:
                NPCRace = 'Human'
                NPCNation = 'Bretonnia'
                NPCGender = 'male'
            elif 'Frogwife' in item:
                NPCRace = 'Human'
                NPCNation = 'Bretonnia'
                NPCGender = 'female'        
            elif "Estalian Diestro" in item or "Knight of the Blazing Sun" in item:
                NPCRace = 'Human'
                NPCNation = 'Estalia'
            elif 'Strigany' in item or 'Knight of the Raven' in item or 'Knight of the Verdant Field' in item or 'Knight Panther' in item or 'Newssheet Vendor' in item or 'Sewer Jack' in item:
                NPCRace = 'Human'
                NPCNation = random.choice(['Averland','Hochland','Middenland','Nordland','Ostermark','Ostland','Reikland','Stirland','Talabecland'])
            elif 'Faceless' in item or 'Battle Pilgrim' in item or "Knight Errant" in item or "Knight of the Realm" in item or "Questing Knight" in item or 'Carcassone Shepherd' in item or 'Grail Pilgrim' in item or 'Herrimault' in item or 'Man at Arms' in item or 'Mediator' in item:
                NPCRace = 'Human'
                NPCNation = 'Bretonnia'
            elif 'Fieldwarden' in item:
                NPCRace = 'Halfling'
                NPCNation = nation(NPCRace)
            elif 'Ataman' in item or 'Horse Archer' in item or 'Horse Coper' in item or 'Horse Master' in item or 'Winged Lancer' in item or 'Kossar' in item or 'Bear Tamer' in item or 'Chekist' in item or 'Drover' in item or 'Streltsi' in item or 'Steppes Nomad' in item or 'Chekist' in item:
                NPCRace = 'Human'
                NPCNation = 'Kislev'
            elif '159Priest' in item or '106Initiate' in item or 'Anointed Priest' in item or 'High Priest' in item or 'Exorcist' in item or 'Warrior Priest' in item:
                NPCRace= 'Human'
                NPCNation = nation(NPCRace)
            elif ('Apprentice Wizard' in item or 'Hedge Wizard' in item or 'Hedgecraft Apprentice' in item or 'Wizard Lord' in item or 'Hedgewise' in item or 'Warlock' in item or 'Master Vigilant' in item or 'Master Wizard' in item or 'Hedge Master' in item or 'Journeyman Wizard' in item or 'Witch' in item) and 'Elf' not in NPCRace and 'Human' not in NPCRace:
                NPCRace = random.choice(['Elf','Human','Human'])
                NPCNation = nation(NPCRace)
                            
        raceSkill = raceSkills (NPCRace, NPCNation, NPCTalent, NPCSkill, NPCGender)
        NPCFaith=faith(NPCRace,NPCNation)
        if isNPCChaotic == 1:
            if 'Magic' in NPCCareer:
                NPCFaith = random.choice(["Nurgle", "Slaanesh", "Tzeentch"])
            else:
                NPCFaith = random.choice(["Khorne", "Nurgle", "Slaanesh", "Tzeentch"])    
        for item in checkCareerRequirements:
            if 'Khorne' in item:
                NPCFaith = 'Khorne'
            elif 'Nurgle' in item:
                NPCFaith = 'Nurgle'
            elif 'Slaanesh' in item:
                NPCFaith = 'Slaanesh'
            elif 'Tzeentch' in item:
                NPCFaith = 'Tzeentch'

        NPCTalent = raceSkill[1]

        NPCSkill = raceSkill[0]
        NPCSkill=sortSkill(NPCSkill,1)
        oldSkill(oldCar,0,NPCTalent)
        NPCTalent=sortSkill(NPCTalent,0)
        for talent in NPCTalent:
            if "Divine Lore (any one)" in talent:
                NPCTalent.remove(talent)
                if "Khorne" in NPCFaith:
                    NPCFaith = random.choice(["Nurgle", "Slaanesh", "Tzeentch"])
                if "Nurgle" in NPCFaith or "Slaanesh" in NPCFaith or "Tzeentch" in NPCFaith:
                    newTalent = "Dark Lore ("+NPCFaith.strip()+")"
                    NPCTalent.append(newTalent)
                elif "Nagash" in NPCFaith:
                    NPCTalent.append("Dark Lore (Necromancy)")
                else:
                    newTalent = "Divine Lore ("+NPCFaith.strip()+")"
                    NPCTalent.append(newTalent)
                NPCTalent.sort()
                
        avancAnt=oldStats(finalCareer,oldCar)
        NPCName = name(NPCRace,NPCNation, NPCGender)


        print("Name: ",NPCName) 
        print("Race: ",NPCRace)
        print("Gender: ", NPCGender.capitalize())
        print("Nation:", NPCNation)
        print("Faith: ",NPCFaith)
        print("Eye Color:", raceSkill[2])
        NPCEyeColor = raceSkill[2]
        print("Hair Color:", raceSkill[3])
        NPCHairColor = raceSkill[3]
        print("Height:", str(int(raceSkill[4]/12))+"'"+str(raceSkill[4]%12)+'"'+" ("+str(int(raceSkill[4]*2.54))+" cm.)")
        NPCHeight = str(int(raceSkill[4]/12))+"'"+str(raceSkill[4]%12)+'"'+" ("+str(int(raceSkill[4]*2.54))+" cm.)"
        print("Weight:", str(raceSkill[5])+ " ("+str(int(raceSkill[5]/2.205))+" kg.)")
        NPCWeight = str(raceSkill[5])+ " lb. ("+str(int(raceSkill[5]/2.205))+" kg.)"
        print("Age:", raceSkill[7])
        NPCAge = raceSkill[7]
        print("Distinguishing Mark:",raceSkill[6])
        NPCDistinguishingMark = raceSkill[6]
        print("Siblings:",raceSkill[8])
        NPCSiblings = raceSkill[8]
        print("Career: ",finalCareer[0:31])
        print("Old Careers: ",oldCar)
        NPCStats = stats(NPCRace,avancAnt,NPCTalent)        
        print("WS=",NPCStats[0])
        print("BS=",NPCStats[1])
        print("Strength=",NPCStats[2])
        print("Toughness=",NPCStats[3])
        print("Agility=",NPCStats[4])
        print("Intelligence=",NPCStats[5])
        print("Willpower=",NPCStats[6])
        print("Fellowship=",NPCStats[7])
        print("Attacks=",NPCStats[8])
        print("Wounds=",NPCStats[9])
        print("Movement=",NPCStats[10])
        print("Magic=",NPCStats[11])
        print("Fate Points=",NPCStats[12])
        NPCStats.append(int(NPCStats[2]/10))
        NPCStats.append(int(NPCStats[3]/10))
        print("\nSkills: ",*NPCSkill,sep='\n')
        print("\nTalents: ",*NPCTalent,sep='\n')
        self.npc.append(NPCStats)
        self.npc.append(NPCName)
        self.npc.append(NPCRace)
        self.npc.append(finalCareer[3:31])
        oldCarFinal = []
        if len(oldCar)==0:
            oldCarFinal.append("None")
        else:
            for item in oldCar:
                oldCarFinal.append(item[3:])
        self.npc.append(oldCarFinal)
        self.npc.append(NPCGender.capitalize())
        self.npc.append(NPCNation)
        self.npc.append(NPCFaith)
        self.npc.append(NPCHeight)
        self.npc.append(NPCWeight)
        self.npc.append(NPCEyeColor)
        self.npc.append(NPCHairColor)
        self.npc.append(NPCAge)
        self.npc.append(NPCDistinguishingMark)
        self.npc.append(NPCSiblings)
        self.npc.append(NPCSkill)
        self.npc.append(NPCTalent)
        #return NPCStats

        

    

##t = GenerateNPC("Bretonnia",0,0,0,0,1)
#t = GenerateNPC("Estalia",0,0,0,0,0)
#g=t.createNPC("Estalia",0,0,0,0,1)
#print('x',t.MPCStats)
#raceDef, gender, level, isMagic, careerDef, isChaos):
