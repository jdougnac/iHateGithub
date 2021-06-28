from django import forms

item_choice= [
    (0, 'Random Item'),
    (1, 'Special'),
    (19, 'Amulet'),
    (32, 'Armour'),
    (37, 'Arrow'),
    (42, 'Boot'),
    (48, 'Bow'),
    (54, 'Grimoire'),
    (62, 'Potion'),
    (71, 'Ring'),
    (74, 'Robe'),
    (84, 'Scroll'),
    (86, 'Wand'),
    (100, 'Weapon')
    ]

mutation_choice= (
    (0, 'Random Mutation'),
    (1, 'Khorne'),
    (2, 'Nurgle'),
    (3, 'Slaanesh'),
    (4, 'Tzeentch')
    )

amount_choice= [tuple([x,x]) for x in range(1,11)]



class createRandom(forms.Form):
    item= forms.CharField(label='Object to generate:', widget=forms.RadioSelect(choices=item_choice))
    amount = forms.CharField(label='Amount: ', widget=forms.Select(choices=amount_choice))

class randomMutation(forms.Form):
    #item= forms.CharField(label='Generate Mutation:', widget=forms.RadioSelect(choices=mutation_choice))
    item= forms.ChoiceField(required=True, choices = mutation_choice, widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial=1)
    amount = forms.CharField(label='Amount: ', widget=forms.Select(choices=amount_choice), initial='2')
