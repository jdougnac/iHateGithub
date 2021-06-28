import random

class Chapter():
    def __init__(self):


        self.origin()
        self.date_of_origin()
        self.progenitor()
        self.purity()
        self.demeanour()
        self.deficiency()
        self.flaw()
        self.characteristic_modifier()
        self.figure_of_legend()
        self.deed_of_legend()
        self.home_world()
        self.chapter_organisation()
        self.combat_doctrine()
        self.solo_abilities()
        self.squad_mode_abilities()
        self.speciality_restrictions()
        self.special_equipment()
        self.chapter_beliefs()
        self.current_status()
        self.chapter_friends()
        self.chapter_enemies()
        self.chapter_advance()


    def origin(self):
        origin_roll = random.randint(1,10)
        counter = ["Orks", "Chaos", "Rebels", "Tyranids", "Tau", "Other Aliens"]
        if origin_roll <=4:
            origin = "Strategic Prognostication"
        elif origin_roll <=6:
            origin = "Counter"
        elif origin_roll <=8:
            origin = "Standing Force"
        elif origin_roll <=10:
            origin = "Crusade"
        if origin == "Counter":
            origin += ": "+random.choice(counter)
        self.origin=origin

    def date_of_origin(self):
        date_roll = random.randint(1,100)
        if date_roll ==1:
            date = "31st Millenium: Second Founding"
        elif date_roll <=5:
            date = "32nd Millenium: Age of Rebirth"
        elif date_roll <=10:
            date = "33rd Millenium: Time of the Beheading"
        elif date_roll <=20:
            date = "34th Millenium: Year of Ghosts"
        elif date_roll <=30:
            date = "35th Millenium: Just prior to the Howling"
        elif date_roll <=40:
            date = "36th Millenium: At the time of the Ur-council of Nova-Terra"
        elif date_roll <=50:
            date = "37th Millenium: After the culmination of the Reign of Blood"
        elif date_roll <=60:
            date = "38th Millenium: Just prior to the Great Cull of 020M37 "
        elif date_roll <=70:
            date = "39th Millenium: 500 years after the defeat of the Apostle of the Blind King"
        elif date_roll <=80:
            date = "40th Millenium: as the Imperium slides into the age of Waning"
        elif date_roll <=95:
            date = "41st Millenium: the 26th and last known Funding"
        elif date_roll <=100:
            date = "Unknown"
        self.date_of_origin= date

    def progenitor(self):
        roll = random.randint(1,100)
        if roll <=20:
            progenitor = "Ultramarines"
        elif roll <= 30:
            progenitor = "Blood Angels"
        elif roll <= 40:
            progenitor = "Dark Angels"
        elif roll <= 50:
            progenitor = "Imperial Fists"
        elif roll <= 60:
            progenitor = "White Scars"
        elif roll <= 70:
            progenitor = "Raven Guard"
        elif roll <= 80:
            progenitor = "Iron Hands"
        elif roll <= 90:
            progenitor = "Space Wolves"
        elif roll <= 100:
            progenitor = "Salamanders"
        #Chapter.progenitor=progenitor
        self.progenitor= progenitor

    #name, demeanour (0 = chapter, 1 = random, 2 = 50/50, deficiency, flaw
    def purity(self):
        roll = random.randint(1,10)
        if roll <=5:
            purity = ["Pure",0,0,0]
        elif roll <=7:
            purity = ["A New Generation",1,0,0]
        elif roll <=9:
            purity = ["Altered Stock",0,1,0]
        elif roll ==10:
            purity = ["Flawed",2,0,1]
        purity_shown=purity[0]
        self.purity_shown=purity_shown
        self.purity= purity

    def demeanour(self):
        other_demeanours = ["Swift as the Wind","Cleanse and Purify","No Mercy, No Respite","Purity Above All","Scions of Mars",
                            "See, But Don't be Seen","Suffer Not The Alien to Live","Suffer Not the Work of Heretics",
                            "Brothers in Battle","Uphold the Honour of the Emperor"]
        if self.purity[1] ==2:
            self.purity[1] = random.randint(0,1)
        if self.purity[1] == 0:
            if self.progenitor == "Ultramarines":
                demeanour = "Honour the Codex"
            elif self.progenitor == "Blood Angels":
                demeanour = "The Red Thirst"
            elif self.progenitor == "Dark Angels":
                demeanour = "Sons of the Lion"
            elif self.progenitor == "Imperial Fists":
                demeanour = "Sons of Dorn"
            elif self.progenitor == "White Scars":
                demeanour = "Son of the Steppes"
            elif self.progenitor == "Raven Guard":
                demeanour = "Son of the Night"
            elif self.progenitor == "Iron Hands":
                demeanour = "Iron and Hate"
            elif self.progenitor == "Space Wolves":
                demeanour = "The Sons of Russ"
            elif self.progenitor == "Salamanders":
                demeanour = "The Promethean Cult"
        elif self.purity[1] == 1:
            demeanour = random.choice(other_demeanours)
        self.demeanour= demeanour

    def deficiency(self):
        deficiency_roll = random.randint(1,100)
        if self.progenitor == "Ultramarines":
            deficiency_chance = 10
        elif self.progenitor == "Blood Angels":
            deficiency_chance = 50
        elif self.progenitor == "Dark Angels":
            deficiency_chance = 10
        elif self.progenitor == "Imperial Fists":
            deficiency_chance = 10
        elif self.progenitor == "White Scars":
            deficiency_chance = 20
        elif self.progenitor == "Raven Guard":
            deficiency_chance = 20
        elif self.progenitor == "Iron Hands":
            deficiency_chance = 20
        elif self.progenitor == "Space Wolves":
            deficiency_chance = 75
        elif self.progenitor == "Salamanders":
            deficiency_chance = 90
        if deficiency_roll <= deficiency_chance:
            specific_deficiency_roll = random.randint(1,100)
            if specific_deficiency_roll <=90:
                self.purity[2] = "Same as progenitor chapter\n"
            else:
                self.purity[2] = 1
        if self.purity[2] == 1:
            self.purity[2] = ""
            deficiency_amount = 1
            missing_zygotes = 0
            extra_deficiency_roll = random.randint(1,10)
            if extra_deficiency_roll == 10:
                deficiency_amount +=random.randint(1,3)
            deficiencies_taken = 0
            while deficiencies_taken < deficiency_amount:
                def_roll = random.randint(1,9)
                if def_roll ==1 and "Hyper-stimulated Omophagea\n" not in self.purity[2]:
                    self.purity[2] +="Hyper-stimulated Omophagea\n"
                    deficiencies_taken += 1
                elif def_roll<=2 and "Oversensitive Occulobe\n" not in self.purity[2]:
                    self.purity[2] +="Oversensitive Occulobe\n"
                    deficiencies_taken += 1
                elif def_roll<=3 and "Mutated Catalepsean Node\n" not in self.purity[2]:
                    self.purity[2] +="Mutated Catalepsean Node\n"
                    deficiencies_taken += 1
                elif def_roll<=4 and "Oolitic Secretions\n" not in self.purity[2]:
                    self.purity[2] +="Oolitic Secretions\n"
                    deficiencies_taken += 1
                elif def_roll<=5 and "Disturbing Voice\n" not in self.purity[2]:
                    self.purity[2] +="Disturbing Voice\n"
                    deficiencies_taken += 1
                elif def_roll<=8:
                    missing_zygotes+=1
                    deficiencies_taken += 1
                elif def_roll==9 and "Doomed\n" not in self.purity[2]:
                    self.purity[2] +="Doomed\n"
                    deficiencies_taken += 1
            for item in range(0,missing_zygotes):
                extra_missing_zygote_chance = random.randint(1,100)
                if extra_missing_zygote_chance >=99:
                    missing_zygotes+=1
            zygote_list = ["Catalepsean Node","Preomnor","Omophagea","Occulobe","Lyman's Ear","Sus-an Membrane",
                           "Oolitic Kidney","Neuroglottis","Mucranoid","Betcher's Gland","Melanchromic Organ"]
            inactive_list = random.sample(zygote_list, missing_zygotes)
            inactive_list.sort()
            if inactive_list != []:
                self.purity[2] += "Missing or Inactive Zygotes:\n"
                for item in inactive_list:
                    self.purity[2] +=item+"\n"
        deficiency = self.purity[2]
        if deficiency == 0:
            deficiency = "None"
        self.deficiency=deficiency

    def flaw(self):
        flaw_list = ["We Stand Alone","Pride in the Colours","Faith in Suspicion","Eye to Eye","Chapter Cult"]
        if self.purity[3] == 1:
            flaw = random.choice(flaw_list)
        else:
            flaw = "None"
        self.flaw= flaw

    def characteristic_modifier(self):
        characteristic_modifiers_list =[
            "+5 BS +5 WP",
            "+5 WP +5 Int",
            "+5 BS +5 WS",
            "+5 Per +5 S",
            "+2 W +5 one Characteristic of choice",
            "+5 T +5 WP",
            "+5 Agi +5 Fel",
            "+5 Per +5 Int",
            "+5 WS +5 Fel",
            "+5 two Characteristics of choice"]
        characteristic_modifier = random.choice(characteristic_modifiers_list)
        self.characteristic_modifier= characteristic_modifier

    def figure_of_legend(self):
        figure = ""
        figure_chance = random.randint(1,100)
        if figure_chance <=20:
            figure+= "A battle brother from a previous generation chapter or from its Founding Legion. Role:\n"
        figure_chance = random.randint(21,100)
        if figure_chance <=50:
            figure += "Chapter Master"
        elif figure_chance <=60:
            figure += "Chief Librarian"
        elif figure_chance <=70:
            figure += "Master of Sanctity"
        elif figure_chance <=73:
            figure += "Master of the Forge"
        elif figure_chance <=74:
            figure += "Master of the Fleet"
        elif figure_chance <=75:
            figure += "Chief Apothecary"
        elif figure_chance <=85:
            figure += "Company Captain, company No "+str(random.randint(1,10))
        elif figure_chance <=90:
            figure += "Squad Sergeant, company No "+str(random.randint(1,10)) + ", squad No " +str(random.randint(1,10))
        elif figure_chance <=99:
            figure +="Battle Brother, company No "+str(random.randint(1,10))
        elif figure_chance ==100:
            figure += random.choice(["Librarian", "Chaplain", "Techmarine", "Driver", "Pilot"])
        self.figure_of_legend= figure

    def deed_of_legend(self):
        deed_roll = random.randint(1,100)
        if deed_roll <=25:
            deed = "Bane of Orks, they remember him to this day"
        elif deed_roll <=50:
            deed = "Bane of Chaos, slew a Daemon Prince"
        elif deed_roll <=70:
            deed = "Led a campaign against rebels, bringing a whole sector back to the Imperium"
        elif deed_roll <=85:
            deed = "Bane of the Eldar, led an assault against one of their crafworlds"
        elif deed_roll <=90:
            deed = "Was lost in a warp accident, but the chapter believes he will return one day"
        elif deed_roll <=95:
            deed = "Discovered and ultimately annihilated a Xenos race, the name of which only the chapter remembers"
        elif deed_roll <=100:
            deed = "After many glorious campaigns, was slain by an Assassin. The chapter now hates the Officio Assassinorum"
        self.deed_of_legend= deed

    def home_world(self):
        home_world_roll = random.randint(1,100)
        if home_world_roll <=30:
            home_world_category = "Hive World"
        elif home_world_roll <=60:
            home_world_category = "Feral World"
        elif home_world_roll <=70:
            home_world_category = "Medieval World"
        elif home_world_roll <=80:
            home_world_category = "Civilised World"
        elif home_world_roll <=90:
            home_world_category = "Uninhabited World"
        elif home_world_roll <=100:
            home_world_category = "Fleet Based"

        if home_world_category == "Fleet Based":
            home_world_terrain = "Non-applicable"
            home_world_relationship = "Direct Rule"
        else:
            home_world_terrain_roll = random.randint(1,100)
            if home_world_terrain_roll <=25:
                home_world_terrain = "Jungle"
            elif home_world_terrain_roll <=50:
                home_world_terrain = "Desert"
            elif home_world_terrain_roll <=60:
                home_world_terrain = "Ice"
            elif home_world_terrain_roll <=65:
                home_world_terrain = "Ocean"
            elif home_world_terrain_roll <=75:
                home_world_terrain = "Wasteland"
            elif home_world_terrain_roll <=80:
                home_world_terrain = "Urban"
            elif home_world_terrain_roll <=85:
                home_world_terrain = "Dead"
            elif home_world_terrain_roll <=90:
                home_world_terrain = "Airless"
            elif home_world_terrain_roll <=100:
                home_world_terrain = "Temperate"

            home_world_relationship_roll = random.randint(1,10)
            if home_world_relationship_roll == 1:
                home_world_relationship = "Direct Rule"
            elif home_world_relationship_roll <=4:
                home_world_relationship = "Stewardship"
            elif home_world_relationship_roll <=10:
                home_world_relationship = "Distant Rule"
        home_world_string = "Home World Category:\n"+home_world_category+"\nPredominant Terrain:\n"+home_world_terrain+"\nRelationship to the World:\n"+home_world_relationship
        self.home_world= home_world_string

    def chapter_organisation(self):
        chapter_organisation_roll = random.randint(1,10)
        if Chapter.progenitor == "Ultramarines":
            if chapter_organisation_roll <=7:
                chapter_organisation = "Codex Chapter"
            elif chapter_organisation_roll <=9:
                chapter_organisation = "Divergent Chapter"
            elif chapter_organisation_roll ==10:
                chapter_organisation = "Unique Organisation"
        else:
            if chapter_organisation_roll <=5:
                chapter_organisation = "Codex Chapter"
            elif chapter_organisation_roll <=8:
                chapter_organisation = "Divergent Chapter"
            elif chapter_organisation_roll <=10:
                chapter_organisation = "Unique Organisation"
        self.chapter_organisation =chapter_organisation

    def combat_doctrine(self):
        combat_doctrine_roll = random.randint(1,10)
        if combat_doctrine_roll ==1:
            combat_doctrine ="Close Combat"
        elif combat_doctrine_roll ==2:
            combat_doctrine = "Ranged Combat"
        elif combat_doctrine_roll ==3:
            combat_doctrine = "Armoured Assault"
        elif combat_doctrine_roll ==4:
            combat_doctrine = "Stealth"
        elif combat_doctrine_roll ==5:
            combat_doctrine = "Lightning Strike"
        elif combat_doctrine_roll ==6:
            combat_doctrine = "Drop Pod"
        elif combat_doctrine_roll ==7:
            combat_doctrine = "Thunderhawk Assault"
        elif combat_doctrine_roll ==8:
            combat_doctrine = "Siege"
        elif combat_doctrine_roll ==9:
            combat_doctrine = "Shock and Awe"
        elif combat_doctrine_roll ==10:
            combat_doctrine = "Terror"
        self.combat_doctrine= combat_doctrine

    def solo_abilities(self):
        solo_ability_roll = random.randint(1,100)
        if solo_ability_roll <=30:
            solo_ability ="Pick a Solo Mode Ability from an existing Chapter"
        elif solo_ability_roll <=45:
            solo_ability = "Choose two skills. \nAt rank 1, may re-roll failed tests with them. \nAt rank 4, gaing +10 to all rolls of those Skills. \nAt rank 8, gain a bonus Success Degree on those tests."
        elif solo_ability_roll <=60:
            solo_ability = "Choose one characteristic.\nAt rank 1, may re-roll failed tests using it.\nAt rank 4, +10 to all rolls using that characteristic.\nAt rank 8, gain a bonus Success Degree on those tests."
        elif solo_ability_roll <=85:
            solo_ability = "While in Solo Mode, counts as having the Lightning Reflexes talent.\nAt rank 3, +10 to all Dodge tests.\nAt rank 5, he's considered to have the Rapid Reaction talent.\nAt rank 7, once per session automatically pass an Agility test, or is considered to have rolled a 01 if it's opposed."
        elif solo_ability_roll <=100:
            solo_ability = "Gains Psyniscience as a Trained Skill.\nMay also reroll any failed WP test to resist a psychic power."
        self.solo_abilities= solo_ability

    def squad_mode_abilities(self):
        squad_attack_pattern_roll = random.randint(1,100)
        squad_defensive_stance_roll = random.randint(1,100)
        if squad_attack_pattern_roll <=30:
            squad_attack_pattern ="Choose a Squad Attack Pattern from an existing chapter"
        elif squad_attack_pattern_roll <=45:
            squad_attack_pattern = "Siege-Breaker"
        elif squad_attack_pattern_roll <=60:
            squad_attack_pattern = "Tactical Finesse"
        elif squad_attack_pattern_roll <=85:
            squad_attack_pattern = "Storm of Hell"
        elif squad_attack_pattern_roll <=100:
            squad_attack_pattern = "Oath of Vengeance"

        if squad_defensive_stance_roll <=30:
            squad_defensive_stance ="Choose a Defensive Stance Ability from an existing chapter"
        elif squad_defensive_stance_roll <=45:
            squad_defensive_stance = "Courage Under Fire"
        elif squad_defensive_stance_roll <=60:
            squad_defensive_stance = "Only in Death..."
        elif squad_defensive_stance_roll <=85:
            squad_defensive_stance = "Swift Advance"
        elif squad_defensive_stance_roll <=100:
            squad_defensive_stance = "Knowledge is Power"
        squad_mode_abilities = "Attack Pattern:\n"+squad_attack_pattern+"\nDefensive Stance:\n"+squad_defensive_stance
        self.squad_mode_abilities= squad_mode_abilities

    def speciality_restrictions(self): #should only occur if organisation is unique
        if self.chapter_organisation=="Unique Organisation":
            restriction_list = ["Apothecary","Assault Marine","Devastator Marine","Techmarine","Librarian"]
            restriction_roll = random.randint(1,100)
            if restriction_roll>=98:
                restrictions = random.sample(restriction_list, 2)
                restrictions = str(restrictions[0]+", "+restrictions[1])
            else:
                restrictions = random.sample(restriction_list, 1)
                restrictions = str(restrictions)
                restrictions = restrictions.replace("'","")
                restrictions = restrictions.replace("[","")
                restrictions = restrictions.replace("]","")
        else:
            restrictions="None"
        self.speciality_restrictions= restrictions

    def special_equipment(self): #should only occur if organisation is Divergent or Unique
        if self.chapter_organisation=="Unique Organisation" or self.chapter_organisation== "Divergent Chapter":
            special_equipment_list = [
            "Traditional Weapon",
            "Totemic Charm",
            "Modified Jump-Pack",
            "Beastial Companion",
            "Rare Weaponry",
            "Blessed Wargear",
            "Special Mount",
            "Special Vehicle",
            "Preferred Fighting Style",
            "Modified Weaponry"]
            special_equipment = random.choice(special_equipment_list)
        else:
            special_equipment="None"
        self.special_equipment= special_equipment

    def chapter_beliefs(self):
        chapter_beliefs_roll = random.randint(1,100)
        if chapter_beliefs_roll <=40:
            chapter_beliefs = "Revere the Primarch"
        elif chapter_beliefs_roll <=65:
            chapter_beliefs = "The Emperor Above All"
        elif chapter_beliefs_roll <=75:
            chapter_beliefs = "Honour the Ancestors"
        elif chapter_beliefs_roll <=80:
            chapter_beliefs = "Death Cult"
        elif chapter_beliefs_roll <=85:
            chapter_beliefs = "Totem Creature"
        elif chapter_beliefs_roll <=90:
            chapter_beliefs = "Purity of Man"
        elif chapter_beliefs_roll <=95:
            chapter_beliefs = "Steel Over Flesh"
        elif chapter_beliefs_roll <=100:
            chapter_beliefs = "Esoteric Beliefs"
        self.chapter_beliefs= chapter_beliefs

    def current_status(self):
        current_status_roll = random.randint(1,10)
        if current_status_roll ==1:
            current_status = "Endangered"
        elif current_status_roll <=4:
            current_status = "Under Strength"
        elif current_status_roll <=9:
            current_status = "Nominal"
        elif current_status_roll ==10:
            current_status = "Over Strength"
        return current_status

    def chapter_friends(self):
        chapter_friends_roll = random.randint(1,100)
        if chapter_friends_roll <=5:
            chapter_friends = "Administratum"
        elif chapter_friends_roll <=15:
            chapter_friends = "Adeptus Arbites"
        elif chapter_friends_roll <=30:
            chapter_friends = "Choose other Adeptus Astartes chapter"
        elif chapter_friends_roll <=35:
            chapter_friends = "Adeptus Astra Telepathica"
        elif chapter_friends_roll <=45:
            chapter_friends = "Adeptus Mechanicus"
        elif chapter_friends_roll <=50:
            chapter_friends = "Adepta Sororitas"
        elif chapter_friends_roll <=55:
            chapter_friends = "Adeptus Titanicus"
        elif chapter_friends_roll <=58:
            chapter_friends = "Astropaths"
        elif chapter_friends_roll <=60:
            chapter_friends = "Chartist Captains"
        elif chapter_friends_roll <=65:
            chapter_friends = "Ecclesiarchy"
        elif chapter_friends_roll <=75:
            chapter_friends = "Imperial Guard of a world of your choice"
        elif chapter_friends_roll <=79:
            chapter_friends = "Imperial Navy"
        elif chapter_friends_roll <=85:
            chapter_friends = "Inquisition"
        elif chapter_friends_roll <=88:
            chapter_friends = "Navigators"
        elif chapter_friends_roll <=91:
            chapter_friends = "Officio Assassinorum"
        elif chapter_friends_roll <=93:
            chapter_friends = "PDF of a world of your choice"
        elif chapter_friends_roll <=98:
            chapter_friends = "A Rogue Trader Dynasty of your choice"
        elif chapter_friends_roll ==99:
            chapter_friends = "Schola Progenium"
        elif chapter_friends_roll ==100:
            chapter_friends = "Scholastica Psykana"
        return chapter_friends

    def chapter_enemies(self):
        chapter_enemies_roll = random.randint(1,100)
        if chapter_enemies_roll <=2:
            chapter_enemies = self.chapter_friends()
        elif chapter_enemies_roll <=31:
            chapter_enemies = "Orks, in general or a particular Waaagh! or Warboss."
        elif chapter_enemies_roll <=42:
            chapter_enemies = "The Eldar, in general or a particular Craftworld or leader."
        elif chapter_enemies_roll <=51:
            chapter_enemies = "The Tyranids, in general or a particular Hive Fleet."
        elif chapter_enemies_roll <=68:
            chapter_enemies = "A particular warband, Chapter or Traitor Legion of Chaos Space Marines."
        elif chapter_enemies_roll <=79:
            chapter_enemies = "A particular Daemon, Daemon Prince or Disciple of Chaos."
        elif chapter_enemies_roll <=87:
            chapter_enemies = "A particular Chaos-aligned group, like Traitor Titan Legions, renegade Imperial Guard, etc."
        elif chapter_enemies_roll <=97:
            chapter_enemies = "The Dark Eldar, in general or a particular Kabal or leader."
        elif chapter_enemies_roll <=98:
            chapter_enemies = "The Tau, in general or a particular force or leader."
        elif chapter_enemies_roll <=100:
            chapter_enemies = "Other: choose one force or group, such as aliens or heretics or a specific cult."

        return chapter_enemies

    def chapter_advance(self):
        chapter_advance_list = [
        "Strength of Arms",
        "Death from Afar",
        "Knowledge is Power",
        "Command without Doubt",
        "Behold our Wrath",
        "Secret Lore",
        "No Respite to the Enemy",
        "Honoured Wargear",
        "Daemon Bane",
        "Xenos Bane"]
        chapter_advance = random.choice(chapter_advance_list)
        return chapter_advance
