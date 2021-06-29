from NPCGenerator.info.hammerAleat import aleatory
import random




def raceSkills(race, nation, talents, skills, gender):
    randomTalents = ["Night Vision", "Acute Hearing", "Ambidextrous", "Coolheaded", "Excellent Vision",
                     "Fleet Footed", "Hardy", "Lightning Reflexes", "Luck", "Marksman", "Mimic",
                     "Resistance to Disease", "Resistance to Magic", "Resistance to Poison", "Savvy",
                     "Sixth Sense", "Strong-minded", "Sturdy", "Suave", "Super Numerate", "Very Resilient",
                     "Very Strong", "Warrior Born"]
    
    dwarfSkills = ["Common Knowledge (Dwarfs)", "Speak Language (Khazalid)",
                   "Speak Language (Reikspiel)"]
    dwarfTalents = ["Dwarfcraft", "Grudge-born Fury", "Night Vision", "Resistance to Magic",
    "Stout-hearted", "Sturdy"]


    elfSkills = ["Common Knowledge (Elves)", "Speak Language (Eltharin)", "Speak Language (Reikspiel)"]
    elfTalents = ["Excellent Vision", "Night Vision"]


    halflingSkills = ["Academic Knowledge (Genealogy/Heraldry)", "Common Knowledge (Halflings)",
                      "Gossip", "Speak Language (Halfling)", "Speak Language (Reikspiel)"]
    halflingTalents = ["Night Vision", "Resistance to Chaos", "Specialist Weapon Group (Sling)"]


    humanSkills=["Common Knowledge (The Empire)", "Gossip", "Speak Language (Reikspiel)"]
    estaliaSkills=["Common Knowledge (Estalia)", "Gossip", "Speak Language (Estalian)"]
    bretonniaSkills = ["Common Knowledge (Bretonnia)", "Gossip", "Speak Language (Breton)"]
    kislevSkills = ["Common Knowledge (Kislev)", "Consume Alcohol", "Speak Language (Kislevite)"]
    norscaSkills = ["Common Knowledge (Norsca)", "Consume Alcohol", "Outdoor Survival", "Sail", "Speak Language (Norse)"]

    norscaTalents = ["Inured to Chaos"]



    distinguishingMarks = ["Pox Marks", "Ruddy Faced", "Scar", "Tattoo",
                                        "Earring", "Ragged Ear", "Nose Ring", "Wart",
                                        "Broken Nose", "Missing Tooth", "Snaggle Teeth",
                                        "Lazy Eye", "Missing Eyebrow(s)", "Missing Digit",
                                        "Missing Nail", "Distinctive Gait", "Curious Smell",
                                        "Huge Nose", "Large Mole", "Small Bald Patch",
                                        "Strange Coloured Eye(s)"]

        
    dwarfSkills.append(random.choice(["Trade (Miner)", "Trade (Smith)", "Trade (Stoneworker)"]))
    elfTalents.append(random.choice(["Aethyric Attunement", "Specialist Weapon Group (Longbow)"]))
    elfTalents.append(random.choice(["Coolheaded", "Savvy"]))
    halflingSkills.append(random.choice(["Trade (Cook)","Trade (Farmer)"]))
    halflingTalents.append(random.choice(randomTalents[1:]))
    humanTalents = random.sample(randomTalents,2)
    norscaTalents.append(random.choice(randomTalents))
    weightRoll = random.randint(1,100)
    distinguishingMark = random.choice(distinguishingMarks)
    height=random.randint(1,10)
    if 'male' in gender:
        height += 2
    if "Dwarf" in race:
        charSkills = dwarfSkills
        charTalents = dwarfTalents
        eye= random.choice(["Pale Grey", "Blue", "Copper", "Light Brown", "Light Brown", "Brown", "Brown", "Dark Brown", "Purple"])
        hair = random.choice(["Ash Blond", "Yellow", "Red", "Copper", "Light Brown", "Brown", "Brown", "Dark Brown", "Blue Black", "Black"])
        if weightRoll == 1:
            weight = 90
        elif weightRoll <= 3:
            weight = 95
        elif weightRoll <= 5:
            weight = 100
        elif weightRoll <= 8:
            weight = 105
        elif weightRoll <= 12:
            weight = 110
        elif weightRoll <= 17:
            weight = 115
        elif weightRoll <= 22:
            weight = 120
        elif weightRoll <= 29:
            weight = 125
        elif weightRoll <= 37:
            weight = 130
        elif weightRoll <= 49:
            weight = 135
        elif weightRoll <= 64:
            weight = 140
        elif weightRoll <= 71:
            weight = 145
        elif weightRoll <= 78:
            weight = 150
        elif weightRoll <= 83:
            weight = 155
        elif weightRoll <= 88:
            weight = 160
        elif weightRoll <= 92:
            weight = 165
        elif weightRoll <= 95:
            weight = 170
        elif weightRoll <= 97:
            weight = 175
        elif weightRoll <= 99:
            weight = 180
        elif weightRoll == 100:
            weight = 185
        height += 50
        age = 15 + (random.randint(1,20)*5)
        siblings = random.choice([0,0,0,1,1,1,1,2,2,3])
    elif "Elf" in race:
        charSkills = elfSkills
        charTalents = elfTalents
        eye= random.choice(["Grey Blue", "Blue", "Copper", "Green", "Light Brown", "Brown", "Dark Brown", "Purple", "Silver", "Black"])
        hair = random.choice(["Silver", "Ash Blond", "Corn", "Yellow", "Copper", "Light Brown", "Light Brown", "Brown", "Dark Brown", "Black"])
        if weightRoll == 1:
            weight = 80
        elif weightRoll <= 3:
            weight = 85
        elif weightRoll <= 5:
            weight = 90
        elif weightRoll <= 8:
            weight = 95
        elif weightRoll <= 12:
            weight = 100
        elif weightRoll <= 17:
            weight = 105
        elif weightRoll <= 22:
            weight = 110
        elif weightRoll <= 29:
            weight = 115
        elif weightRoll <= 37:
            weight = 120
        elif weightRoll <= 49:
            weight = 125
        elif weightRoll <= 64:
            weight = 130
        elif weightRoll <= 71:
            weight = 135
        elif weightRoll <= 78:
            weight = 140
        elif weightRoll <= 83:
            weight = 145
        elif weightRoll <= 88:
            weight = 150
        elif weightRoll <= 92:
            weight = 155
        elif weightRoll <= 95:
            weight = 160
        elif weightRoll <= 97:
            weight = 165
        elif weightRoll <= 99:
            weight = 170
        elif weightRoll == 100:
            weight = 175
        height += 64
        distinguishingMark="None"
        age = 25 + (random.randint(1,20)*5)
        siblings = random.choice([0,1,1,1,1,2,2,2,2,3])
    
    elif "Halfling" in race:
        charSkills = halflingSkills
        charTalents = halflingTalents
        eye= random.choice(["Blue", "Hazel", "Hazel", "Light Brown", "Light Brown", "Brown", "Brown", "Dark Brown",  "Dark Brown", "Dark Brown"])
        hair = random.choice(["Ash Blond", "Corn", "Yellow", "Yellow", "Copper", "Red", "Light Brown", "Brown", "Dark Brown", "Black"])
        if weightRoll == 1:
            weight = 75
        elif weightRoll <= 3:
            weight = 75
        elif weightRoll <= 5:
            weight = 80
        elif weightRoll <= 8:
            weight = 80
        elif weightRoll <= 12:
            weight = 85
        elif weightRoll <= 17:
            weight = 85
        elif weightRoll <= 22:
            weight = 90
        elif weightRoll <= 29:
            weight = 90
        elif weightRoll <= 37:
            weight = 95
        elif weightRoll <= 49:
            weight = 100
        elif weightRoll <= 64:
            weight = 100
        elif weightRoll <= 71:
            weight = 105
        elif weightRoll <= 78:
            weight = 110
        elif weightRoll <= 83:
            weight = 115
        elif weightRoll <= 88:
            weight = 120
        elif weightRoll <= 92:
            weight = 125
        elif weightRoll <= 95:
            weight = 130
        elif weightRoll <= 97:
            weight = 135
        elif weightRoll <= 99:
            weight = 140
        elif weightRoll == 100:
            weight = 145
        height += 38
        age = 18 + (random.randint(1,20)*2)
        siblings = random.choice([1,2,2,3,3,4,4,5,5,6])
        
    elif "Human" in race:
        if "Bretonnia" in nation:
            charSkills = bretonniaSkills
        elif "Kislev" in nation:
            charSkills = kislevSkills
        elif "Estalia" in nation:
            charSkills = estaliaSkills
        else:
            charSkills = humanSkills
        charTalents = humanTalents
        if "Norsca" in nation:
            charSkills = norscaSkills
            charTalents = norscaTalents
                    
        eye= random.choice(["Pale Grey", "Grey Blue", "Blue", "Green", "Copper", "Light Brown", "Brown", "Dark Brown", "Purple", "Black"])
        hair = random.choice(["Ash Blond", "Corn", "Yellow", "Copper", "Red", "Light Brown", "Brown", "Brown", "Dark Brown", "Black"])
        if weightRoll == 1:
            weight = 105
        elif weightRoll <= 3:
            weight = 110
        elif weightRoll <= 5:
            weight = 115
        elif weightRoll <= 8:
            weight = 120
        elif weightRoll <= 12:
            weight = 125
        elif weightRoll <= 17:
            weight = 130
        elif weightRoll <= 22:
            weight = 135
        elif weightRoll <= 29:
            weight = 140
        elif weightRoll <= 37:
            weight = 145
        elif weightRoll <= 49:
            weight = 150
        elif weightRoll <= 64:
            weight = 155
        elif weightRoll <= 71:
            weight = 160
        elif weightRoll <= 78:
            weight = 165
        elif weightRoll <= 83:
            weight = 170
        elif weightRoll <= 88:
            weight = 175
        elif weightRoll <= 92:
            weight = 180
        elif weightRoll <= 95:
            weight = 190
        elif weightRoll <= 97:
            weight = 200
        elif weightRoll <= 99:
            weight = 210
        elif weightRoll == 100:
            weight = 220
        height += 61
        if gender == "male":
            height += 1
        age = 15 + random.randint(1,20)
        siblings = random.choice([0,1,1,2,2,3,3,4,4,5])
            

    for raceSkill in charSkills:
        skills.append(raceSkill)
    for raceTalent in charTalents:
        talents.append(raceTalent)
    attributes = [skills, talents, eye, hair, height, weight, distinguishingMark, age, siblings]
    for element in attributes:
        if type(element) is list:
            element.sort()
    return attributes
