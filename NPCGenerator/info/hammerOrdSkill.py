import random
from NPCGenerator.info.hammerAnySkill import anySkill
def ordSkill(x):
    variable=[]
    variableFinal=[]
    for var in x:
        if " or " in var:
            sequenceList = var.split(" or ")
            variable.append(random.choice(sequenceList))


        elif "(any" in var and "Divine Lore" not in var and "Lesser Rune (any two)" not in var:
            document=""
            if "Trade" in var:
                document = "trade.txt"
            elif "Speak Language" in var:
                document = "lang.txt"
            elif "Performer" in var:
                document = "performer.txt"                
            elif "Specialist Weapon Group" in var:
                document = "weapons.txt"
            elif "Arcane Language" in var:
                document = "arcLang.txt"
            elif "Academic Knowledge" in var:
                document = "acKnow.txt"
            elif "Common Knowledge" in var:
                document = "coKnow.txt"
            elif "Secret Signs" in var:
                document = "secSign.txt"
            elif "Lesser Magic" in var:
                document = "lesserMagic.txt"
            elif "Arcane Lore" in var:
                document = "arcLore.txt"
            elif "Dark Lore" in var:
                document = "darkLore.txt"
            elif "Secret Language" in var:
                document = "secLang.txt"
            elif "Master Rune" in var:
                document = "masterRune.txt"  
            elif "Rune" in var:
                document = "runes.txt"
            elif "Virtue of Knighthood" in var:
                document = "virtueKnighthood.txt"
            if "one" in var:
                number = 1
            elif "two" in var:
                number = 2
            elif "three" in var:
                number = 3
            elif "four" in var:
                number = 4
            elif "five" in var:
                number = 5
            elif "six" in var:
                number = 6
            elif "ten" in var:
                number = 10
            anyList = anySkill(document, number)
            for item in anyList:
                variable.append(item)
        elif "Lesser Rune (any two)" in var:
            anyList = anySkill("lesserRune.txt", 2)
            for item in anyList:
                variable.append(item)
        else:
            variable.append(var)
    for item in variable:
        variableFinal.append(item.strip())
            
            
    
    return variableFinal
