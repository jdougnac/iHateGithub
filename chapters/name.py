import random

#26
place = [
'Antaeus','Blood','Byzantium','Elthain','Iron','Mars',
'Night','Orar','Orpheus',"Planet",'Praesium','Protelus','Terra','Thanatos',
'the Covenant','the Kraken','the Phoenix','the Primarch','the Raven','the Rift','the Legion',
'Thunder','Ulixis','Wrath']


#62
adjective = [    'Azure','Black','Carmine','Countless','Crimson','Dark','Death','Defiant','Desert',
                  'Doom','Dusk',"Emperor's",'Flame','Flaming','Genesis','Golden',
                  'Grey','Halo','Helion','Honoured','Howling','Hundred','Imperial',
                  'Iron','Lunar','Nameless','Necropolis','Nemesis','Nova','Obsidian',
                  'Omega','Purple','Rainbow','Raven','Red','Redeeming','Resplendent',
                  'Rift','Sable','Scar','Shadow','Silver','Sky','Solar','Soul','Star',
                  'Storm','Tempest','Terror','Thousand','Timeless','Tome','Tormented',
                  'Ultima','Umbral','Unforgiven','Unyielding','Valiant','Vindictive',
                  'Viper','Void','War','White','Wrathful']

#142
noun = [
    'Absolution','Adepts','Adulators','Angels','Axes','Bearers','Bears','Blades','Brethren',
    'Bringers','Brotherhood','Brothers','Callers','Champions','Claws','Confessors','Consuls',
    'Crusaders','Daggers','Damnation','Defiance','Desolators','Destroyers','Dictators','Disciples',
    'Dragons','Drakes','Eagles','Execrators','Executioners','Exemplars','Exorcists','Exsanguinators',
    'Falcons','Fire','Fists','Fulminators','Furies','Fury','Gauntlets','Giants','Glaives','Gorgons',
    'Griffons','Guard','Guard','Guardians','Hammers','Hands','Haunters','Hawks','Hearts','Heralds',
    'Hounds','Hunters','Inculcators','Interceptors','Invaders','Invictors','Jaguars','Keepers',
    'Knights','Lamenters','Legion','Leopards','Light','Lions','Lords','Marines','Mentors',
    'Minotaurs','Nemesors','Oblators','Paladins','Panthers','Patriarchs','Penance','Penitents',
    'Phantoms','Praetors','Purgatory','Rampagers','Raptors','Ravagers','Ravens','Reapers','Reclaimers',
    'Redeemers','Redemption','Relictors','Reparators','Retractors','Retribution','Revenants','Revilers',
    'Scars','Scimitars','Scions','Scorpions','Scythes','Sentinels','Seraphs','Shades','Sharks','Shields',
    'Skulls','Slayers','Snakes','Sons','Spears','Spectres','Stalkers','Stars','Storm','Strike','Subjugators',
    'Supplicators','Swords','Talons','Tarantulas','Tempest','Tempestors','Templars','Tigers','Tormentors',
    'Tributors','Tridents','Valedictors','Venerators','Vengeance','Victors','Vigilance','Vindicators',
    'Vipers','Walkers','Wardens','Warriors','Watch','Watchers','Wings','Wolves','Wrath']
class Name:

    def __init__(self, predecessor):
        #self.name()
        self.predecessor=predecessor

        name_format = random.randint(1, 3)
        if name_format == 1:
            name = random.choice(adjective)+" "+random.choice(noun)
        elif name_format == 2:
            name = random.choice(noun) + " of "+random.choice(place)
        elif name_format == 3:
            name = random.choice(adjective)+" "+random.choice(noun)+ " of "+random.choice(place)
        if predecessor == 'Ultramarines':
            primarch = 'Guilliman'
            planet = 'Ultramar'
        elif predecessor == 'Blood Angels':
            primarch = 'Sanguinius'
            planet = 'Baal'
        elif predecessor == 'Dark Angels':
            primarch = 'the Lion'
            planet = 'Caliban'
        elif predecessor == 'Imperial Fists':
            primarch = 'Dorn'
            planet = 'Inwit'
        elif predecessor == 'White Scars':
            primarch = random.choice(['Jaghatai', 'the Khan'])
            planet = 'Chogoris'
        elif predecessor == 'Raven Guard':
            primarch = 'Corax'
            planet = 'Kiavahr'
        elif predecessor == 'Iron Hands':
            primarch = 'the Gorgon'
            planet = 'Medusa'
        elif predecessor == 'Space Wolves':
            primarch = 'Russ'
            planet = 'Fenris'
        elif predecessor == 'Salamanders':
            primarch = 'Vulkan'
            planet = 'Nocturne'
        else:
            primarch = 'the Primarch'
            planet = 'Holy Terra'
        if name [-12:] == "the Primarch":
            name = name[:-12]
            name = name +primarch
        if name [-6:] == "Planet":
            name = name[:-6]
            name = name +planet
        self.name = name
