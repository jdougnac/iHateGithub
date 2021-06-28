import random
from hammer.info.mutations import *



class Mutation:
    def __init__(self, mutation_type, amount):
        self.item_list=[] 
        self.mutation_type = mutation_type
        self.amount=amount
        self.pick_mutations(mutation_type, amount)
    
           
    def pick_mutations(self, mutation_type, amount):
        if mutation_type ==0:
            normal_amount=amount
            amount=0
        else:
            normal_amount=0
            for x in range(0, amount):
                normal_chance = random.randint(1,100)
                if normal_chance >= 93:
                    normal_amount +=1
                    amount-=1
        for z in range(0, normal_amount):
            extra_mutation_chance=random.randint(1,1000)
            if extra_mutation_chance <985:
                pass
            elif extra_mutation_chance<=990:
                normal_amount+=1
            elif extra_mutation_chance<=995:
                normal_amount+=2
        for item in range(0,amount):
            if mutation_type==1:
                mutation=random_mutation_khorne()            
            elif mutation_type==2:
                mutation=random_mutation_nurgle()            
            elif mutation_type==3:
                mutation=random_mutation_slaanesh()                
            elif mutation_type==4:
                mutation=random_mutation_tzeentch()
            self.item_list.append(mutation)
        for item in range(0, normal_amount):
            mutation = random_mutation()
            self.item_list.append(mutation)
        
            
        #print('ZZZZZZZZZZZZ',self.item_list)
            
            



