import random
from hammer.info.bag import pick_bag
from hammer.info.armour import pick_armour
from hammer.info.amulet import pick_amulet
from hammer.info.arrow import pick_arrow
from hammer.info.boot import pick_boot
from hammer.info.bow import pick_bow
from hammer.info.grimoire import pick_grimoire
from hammer.info.potion import pick_potion
from hammer.info.ring import pick_ring
from hammer.info.robe import pick_robe
from hammer.info.scroll import pick_scroll
from hammer.info.wand import pick_wand
from hammer.info.weapon import pick_weapon
from hammer.info.special import pick_special
from hammer.info.horn import pick_horn
from hammer.info.glove import pick_glove


class Item:
    def __init__(self, object_type, amount):
        self.item_list=[] 
        self.object_type = object_type
        self.amount=amount
        self.pick_objects(object_type, amount)
    
           
    def pick_objects(self, object_type, amount):
        for x in range(0, amount):
            if object_type == 0:
                object_roll = random.randint(1, 100)
            else:
                object_roll = object_type
            if object_roll <= 11:
                special_roll = random.randint(1, 100)
                if special_roll <= 70:
                    item=pick_special()
                elif special_roll <= 80:
                    item = pick_horn()
                elif special_roll <= 90:
                    item = pick_glove()
                elif special_roll <= 100:
                    item = pick_bag()
            elif object_roll <= 19:
                item = pick_amulet()
            elif object_roll <= 32:
                item = pick_armour()
            elif object_roll <= 37:
                item = pick_arrow()
            elif object_roll <= 42:
                item = pick_boot()
            elif object_roll <= 48:
                item = pick_bow()
            elif object_roll <= 54:
                item = pick_grimoire()
            elif object_roll <= 62:
                item = pick_potion()
            elif object_roll <= 71:
                item = pick_ring()
            elif object_roll <= 74:
                item = pick_robe()
            elif object_roll <= 84:
                item = pick_scroll()
            elif object_roll <= 86:
                item = pick_wand()
            elif object_roll <= 100:               
               item = pick_weapon()               
            self.item_list.append(item)



