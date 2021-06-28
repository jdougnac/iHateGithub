from django.shortcuts import render
from .item import Item
from .mutation import Mutation
from .forms import createRandom
from .forms import randomMutation

# Create your views here.
def home(request):

    return render(request, 'hammer/main.html')

def createItem(request):
    form = createRandom(request.POST)
    if len(request.POST) != 0:
        item = Item(int(request.POST["item"]), int(request.POST["amount"]))
        context ={"item": item, "form": form}
        return render(request, 'hammer/itemCreator.html', context)#, context)
    else: context=""
    return render(request, 'hammer/itemCreator.html', {"form":form})

def createMutation(request):
    form = randomMutation(request.POST)
    if len(request.POST) != 0:
        item = Mutation(int(request.POST["item"]), int(request.POST["amount"]))
        context ={"item": item, "form": form}
        return render(request, 'hammer/mutationCreator.html', context)#, context)
    else: context=""
    return render(request, 'hammer/mutationCreator.html', {"form":form})

def runes(request):

    return render(request, 'hammer/runes.html')
