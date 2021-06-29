import random
from NPCGenerator.info.hammerAleat import aleatory

def name(z,w, gender):
    if "Elf" in z:
        if gender=="male":
            return aleatory("nomElfMasc.txt")[:-1] + " " + aleatory("apeElf.txt")[:-1]
        elif gender=="female":
            return aleatory("nomElfFem.txt")[:-1] + " " + aleatory("apeElf.txt")[:-1]
    elif "Dwarf" in z:
        if gender=="male":
            return aleatory("nomEnaMasc.txt")[:-1] + " " + aleatory("apeDwarf.txt")[:-1]
        elif gender=="female":
            return aleatory("nomEnaFem.txt")[:-1] + " " + aleatory("apeDwarf.txt")[:-1]
    elif "Halfling" in z:
        if gender=="male":
            return aleatory("nomHalMasc.txt")[:-1] + " " + aleatory("apeHalf.txt")[:-1]
        elif gender=="female":
            return aleatory("nomHalFem.txt")[:-1] + " " + aleatory("apeHalf.txt")[:-1]           
    elif "Bretonnia" in w:
        if gender=="male":
            return aleatory("nomBretMasc.txt")[:-1] + " " + aleatory("apeBret.txt")[:-1]
        elif gender=="female":
            return aleatory("nomBretFem.txt")[:-1] + " " + aleatory("apeBret.txt")[:-1]
    elif "Estalia" in w:
        if gender=="male":
            return aleatory("nomEstaMasc.txt")[:-1] + " " + aleatory("apeEst.txt")[:-1]
        elif gender=="female":
            return aleatory("nomEstaFem.txt")[:-1] + " " + aleatory("apeEst.txt")[:-1]
    elif "Albion" in w:
        if gender=="male":
            return aleatory("nomAlbMasc.txt")[:-1] + " " + aleatory("apeAlb.txt")[:-1]
        elif gender=="female":
            return aleatory("nomAlbFem.txt")[:-1] + " " + aleatory("apeAlb.txt")[:-1]
    elif "Kislev" in w:
        if gender=="male":
            return aleatory("nomKisMasc.txt")[:-1] + " " + aleatory("apeKis.txt")[:-1]
        elif gender=="female":
            return aleatory("nomKisFem.txt")[:-1] + " " + aleatory("apeKis.txt")[:-1]
    elif "Norsca" in w:
        if gender == "male":
            return aleatory("nomNorscaMasc.txt")[:-1] + " " + aleatory("apeNorsca.txt")[:-1]
        elif gender == "female":
            return aleatory("nomNorscaFem.txt")[:-1] + " " + aleatory("apeNorsca.txt")[:-1]
        
    else:
        if gender=="male":
            return aleatory("nomImpMasc.txt")[:-1] + " " + aleatory("apeImp.txt")[:-1]
        elif gender=="female":
            return aleatory("nomImpFem.txt")[:-1] + " " + aleatory("apeImp.txt")[:-1]
        
