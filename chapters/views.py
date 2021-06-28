from django.shortcuts import render
#import sys
# insert at position 1 in the path, as 0 is the path of this file.
#sys.path.append('/code')
from .info import Chapter
from .forms import keepChapter
from .name import Name

# Create your views here.


def createChapter(request):
    print('ZZZZZZZZZZZZZZZZZZZZZZ',request)

    #form = createChapter(request.POST)

    
    if len(request.POST) != 0:
        #form = createChapter(request.POST)
        print('XXXXXXXXXXXXXXXXXXX',request.POST, 'XXXXXXXXXXXXXXXXXXX')
        chapter = Chapter()
        name=Name(chapter.progenitor)
    #    context ={"chapter": chapter}
        context={
        "name":name.name,
        "origin":chapter.origin,
        "date_of_origin":chapter.date_of_origin,
        "progenitor":chapter.progenitor,
        "purity":chapter.purity,
        "demeanour":chapter.demeanour,
        "deficiency":chapter.deficiency,
        "flaw":chapter.flaw,
        "characteristic_modifier":chapter.characteristic_modifier,
        "figure_of_legend":chapter.figure_of_legend,
        "deed_of_legend":chapter.deed_of_legend,
        "home_world":chapter.home_world,
        "chapter_organisation":chapter.chapter_organisation,
        "combat_doctrine":chapter.combat_doctrine,
        "solo_abilities":chapter.solo_abilities,
        "squad_mode_abilities":chapter.squad_mode_abilities,
        "speciality_restrictions":chapter.speciality_restrictions,
        "special_equipment":chapter.special_equipment,
        "chapter_beliefs":chapter.chapter_beliefs,
        "current_status":chapter.current_status,
        "chapter_friends":chapter.chapter_friends,
        "chapter_enemies":chapter.chapter_enemies,
        "chapter_advance":chapter.chapter_advance
        }
        return render(request, 'chapters/chapters.html', context)
    return render(request, 'chapters/chapters.html')
