from django.shortcuts import render
from .hammerNPC import GenerateNPC
#from .forms import createNPC
from .forms import NPCGenerator
# Create your views here.
def home(request):

    return render(request, 'NPCGenerator/main.html')

def creeateNPC(request):
    form = NPCGenerator(initial = {'gender':0, 'level':0, 'magic':0,'chaos':0})
    if len(request.POST) != 0:
        npc = GenerateNPC(request.POST["race"],request.POST["gender"], request.POST["level"],
                          request.POST["magic"], request.POST["chaos"], request.POST["career"])
        context ={"npc": npc, "form": form}
        return render(request, 'NPCGenerator/NPCCreator.html', context)#, context)
    else:
        context=""
    return render(request, 'NPCGenerator/NPCCreator.html', {"form":form})
