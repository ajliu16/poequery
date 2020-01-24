# Task - Create JSON
# Add values for Armor, Energy Shield, Fire, Cold, Lightning, Chaos
# Create JSON file
import json
import codecs

class Unique:
    def __init__(self, u_name, u_base, u_type, u_basetype, u_info, u_implicit, u_description, u_flair):
        span_implicit = []
        div_description = []
        div_flair = []
        div_stat = []
        physdps = 0
        firedps = 0
        colddps = 0
        lightningdps = 0
        chaosdps = 0
        attackspeed = 0
        criticalchance = 0
        levelreq = 0
        armour = 0
        evasion = 0
        energy_shield = 0

        #calculates various stats
        x = ""
        xl = []
        xsum = 0
        for i in u_info:
            if "Armour:" in i:
                for f in i:
                    if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                        x+=f
                    elif f == "-" or f == "–" or f == ")" or f == "<":
                        if x != "":
                            xl.append(int(x))
                            x = ""
                if len(xl) == 2:
                    xsum = xl[1]
                elif len(xl) == 1:
                    xsum = xl[0]
                armour = xsum
                x = ""
                xsum = 0
                xl = []
        for i in u_info:
            if "Evasion:" in i:
                for f in i:
                    if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                        x+=f
                    elif f == "-" or f == "–" or f == ")" or f == "<":
                        if x != "":
                            xl.append(int(x))
                            x = ""
                if len(xl) == 2:
                    xsum = xl[1]
                elif len(xl) == 1:
                    xsum = xl[0]
                evasion = xsum
                x = ""
                xsum = 0
                xl = []
        for i in u_info:
            if "Energy Shield:" in i:
                for f in i:
                    if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                        x+=f
                    elif f == "-" or f == "–" or f == ")" or f == "<":
                        if x != "":
                            xl.append(int(x))
                            x = ""
                if len(xl) == 2:
                    xsum = xl[1]
                elif len(xl) == 1:
                    xsum = xl[0]
                energy_shield = xsum
                x = ""
                xsum = 0
                xl = []
        for i in u_info:
            if "Requires Level" in i:
                for f in i.split(",")[0]:
                    if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                        x += f
                levelreq = int(x)
                x = ""
        for i in u_info:
            if "Attacks per Second" in i:
                if "<" not in i or ">" not in i:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                            x += f
                    attackspeed = float(x)
                    x = ""
                else:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                            x += f
                        elif f == "-" or f == "–" or f == ")" or f == "<":
                            if x != "":
                                xl.append(float(x))
                            x = ""
                    if len(xl) == 2:
                        xsum = xl[1]
                    else:
                        xsum = xl[0]
                    attackspeed = round(xsum, 3)
                    x = ""
                    xsum = 0
                    xl = []
        for i in u_info:
            if "Critical Strike Chance" in i:
                if "<" not in i or ">" not in i:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                            x += f
                    criticalchance = float(x)
                    x = ""
                else:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                            x += f
                        elif f == "-" or f == "–" or f == ")" or f == "<":
                            if x != "":
                                xl.append(float(x))
                            x = ""
                    if len(xl) == 2:
                        xsum = xl[1]
                    else:
                        xsum = xl[0]
                    criticalchance = round(xsum, 3)
                    x = ""
                    xsum = 0
                    xl = []
        for i in u_info:
            if "Physical Damage" in i:
                if "(" in i:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == ".":
                            x = x + f
                        elif f == "-" or f == "–" or f == ")":
                            if x != "":
                                xl.append(float(x))
                            x = ""
                else:
                    for f in i:
                        if f == "0" or f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == "." or f == "–":
                            x = x + f
                    for g in x.split("–"):
                        xl.append(float(g))
                    x = ""
                if len(xl) == 4:
                    print(xl)
                    xsum = (xl[1] + xl[3])/2
                else:
                    xsum = (xl[0] + xl[1])/2
                physdps = round(xsum * attackspeed, 1)
                x = ""
                xsum = 0
                xl = []
        for i in u_info:
            if "Chaos Damage" in i:
                if "Chaos" in i:
                    for g in i:
                        if g == "0" or g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == ".":
                            x = x + g
                        elif g == "-" or g == "–" or g == ")" or g == "<":
                            if x != "":
                                xl.append(float(x))
                            x = ""
                    if len(xl) == 4:
                        xsum = (xl[1] + xl[3])/2
                    elif len(xl) == 3:
                        xsum = (xl[0] + xl[2])/2
                    elif len(xl) == 2:
                        xsum = (xl[0] + xl[1])/2
                    chaosdps = round(xsum * attackspeed, 1)
                    x = ""
                    xsum = 0
                    xl = []
        for i in u_info:
            if "Elemental Damage" in i:
                for f in i.split():
                    if "Fire" in f:
                        for g in f:
                            if g == "0" or g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == ".":
                                x = x + g
                            elif g == "-" or g == "–" or g == ")" or g == "<":
                                if x != "":
                                    xl.append(float(x))
                                x = ""
                        if len(xl) == 4:
                            xsum = (xl[1] + xl[3])/2
                        elif len(xl) == 3:
                            xsum = (xl[0] + xl[2])/2
                        elif len(xl) == 2:
                            xsum = (xl[0] + xl[1])/2
                        firedps = round(xsum * attackspeed, 1)
                        x = ""
                        xsum = 0
                        xl = []
                    elif "Cold" in f:
                        for g in f:
                            if g == "0" or g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == ".":
                                x = x + g
                            elif g == "-" or g == "–" or g == ")" or g == "<":
                                if x != "":
                                    xl.append(float(x))
                                x = ""
                        if len(xl) == 4:
                            xsum = (xl[1] + xl[3])/2
                        elif len(xl) == 3:
                            xsum = (xl[0] + xl[2])/2
                        elif len(xl) == 2:
                            xsum = (xl[0] + xl[1])/2
                        colddps = round(xsum * attackspeed, 1)
                        x = ""
                        xsum = 0
                        xl = []
                    elif "Lightning" in f:
                        for g in f:
                            if g == "0" or g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == ".":
                                x = x + g
                            elif g == "-" or g == "–" or g == ")" or g == "(" or g == "<":
                                if x != "":
                                    xl.append(float(x))
                                x = ""
                        if len(xl) == 4:
                            xsum = (xl[1] + xl[3])/2
                        elif len(xl) == 3:
                            xsum = (xl[0] + xl[2])/2
                        elif len(xl) == 2:
                            xsum = (xl[0] + xl[1])/2
                        lightningdps = round(xsum * attackspeed, 1)
                        x = ""
                        xsum = 0
                        xl = []

        #creates info, implicit, description, and flairs
        if u_info != []:
            for i in u_info:
                if i != "":
                    div_stat.append(i)
        if u_implicit != []:
            for i in u_implicit:
                span_implicit.append(i)
        if u_description != []:
            for i in u_description:
                if i != "":
                    div_description.append(i)
        if u_flair != []:
            for i in u_flair:
                if i != "":
                    div_flair.append(i)
        
        #creates image name
        c_name = u_name.split(' ')
        c2_name = ""
        u_img = ""
        for i in c_name:
            c2_name += i.capitalize()
        c3_name = c2_name.split("'")
        for i in c3_name:
            u_img += i
        try:
            image = open(f"C:/Users/liuaa/Desktop/master_poequery/images/{u_img}.png")
            self.img = u_img
        except:
            self.img = 0
        self.name = u_name
        self.base = u_base
        self.type = u_type
        self.basetype = u_basetype
        self.info = div_stat
        self.implicit = span_implicit
        self.description = div_description
        self.flair = div_flair

        self.Dps = round(physdps + firedps + colddps + lightningdps + chaosdps, 1)
        self.PhysDps = physdps
        self.ElementalDps = firedps + colddps + lightningdps
        self.FireDps = firedps
        self.ColdDps = colddps
        self.LightningDps = lightningdps
        self.ChaosDps = chaosdps
        self.Attack_Speed = attackspeed
        self.Critical_Chance = criticalchance
        self.Level_Requirement = levelreq

        self.Armour = armour
        self.Evasion = evasion
        self.Energy_Shield = energy_shield
        




Unique_Dictionary = {}
Unique_List = []
name_u = ""
base_u = []
info_u = []
implicit_u = []
description_u = []
flair_u = []
type_u = ""
basetype_u = ""
file_handler = open("C:/Users/liuaa/Desktop/master_poequery/Text/TexttoJSON/master_unique_plus_span.txt", encoding='utf-8').read().split("\n")

counter = 0
range_file = len(file_handler)
for i in file_handler:
    if i == "u_name":
        name_u = str(file_handler[counter + 1])
        counter += 1
    elif i == "u_base":
        base_u = str(file_handler[counter+1])
        counter += 1
    elif i == "u_type":
        type_u = str(file_handler[counter+1])
        counter += 1
    elif i == "u_basetype":
        basetype_u = str(file_handler[counter+1])
        counter += 1
    elif i == "u_info":
        r_counter = -1
        for f in file_handler[counter + 1: range_file]:
            if f == "u_implicit" or f == "u_description":
                counter -= r_counter
                break
            else:
                counter +=1
                r_counter +=1
                info_u.append(f)
    elif i == "u_implicit":
        r_counter = -1
        for f in file_handler[counter + 1: range_file]:
            if f == "u_description":
                counter -= r_counter
                break
            else:
                implicit_u.append(f)
                counter +=1
                r_counter +=1
    elif i == "u_description":
        r_counter = -1
        for f in file_handler[counter + 1: range_file]:
            if f == "u_flair":
                counter -= r_counter
                break
            else:
                description_u.append(f)
                counter+=1
                r_counter +=1
    elif i == "u_flair":
        r_counter = -1
        for f in file_handler[counter + 1: range_file]:
            if f == "u_name":
                counter -= r_counter
                Unique_Dictionary[name_u] = Unique(name_u,base_u,type_u,basetype_u,info_u,implicit_u,description_u,flair_u)
                Unique_List.append(Unique(name_u,base_u,type_u,basetype_u,info_u,implicit_u,description_u,flair_u))
                name_u = ""
                base_u = []
                type_u = ""
                basetype_u = ""
                info_u = []
                implicit_u = []
                description_u = []
                flair_u = []
                break
            else:
                flair_u.append(f)
                counter +=1
                r_counter +=1
    else:
        counter+=1

"""
ObjectList = {}

jsonthankyou = ""
jsondata = []

for i in Unique_List:
    ObjectList['name'] = Unique_Dictionary[i.name].name
    ObjectList['base'] = Unique_Dictionary[i.name].base
    ObjectList['catagory'] = Unique_Dictionary[i.name].type
    ObjectList['catagory_type'] = Unique_Dictionary[i.name].basetype
    ObjectList['info'] = Unique_Dictionary[i.name].info
    ObjectList['implicit'] = Unique_Dictionary[i.name].implicit
    ObjectList['description'] = Unique_Dictionary[i.name].description
    ObjectList['flair'] = Unique_Dictionary[i.name].flair
    ObjectList['dps'] = Unique_Dictionary[i.name].Dps
    ObjectList['phys_dps'] = Unique_Dictionary[i.name].PhysDps
    ObjectList['elemental_dps'] = Unique_Dictionary[i.name].ElementalDps
    ObjectList['fire_dps'] = Unique_Dictionary[i.name].FireDps
    ObjectList['cold_dps'] = Unique_Dictionary[i.name].ColdDps
    ObjectList['lightning_dps'] = Unique_Dictionary[i.name].LightningDps
    ObjectList['chaos_dps'] = Unique_Dictionary[i.name].ChaosDps
    ObjectList['attack_speed'] = Unique_Dictionary[i.name].Attack_Speed
    ObjectList['critical_chance'] = Unique_Dictionary[i.name].Critical_Chance
    ObjectList['level_requirement'] = Unique_Dictionary[i.name].Level_Requirement
    ObjectList['armour'] = Unique_Dictionary[i.name].Armour
    ObjectList['evasion'] = Unique_Dictionary[i.name].Evasion
    ObjectList['energy_shield'] = Unique_Dictionary[i.name].Energy_Shield
    jsondata.append(ObjectList.copy())




with open('./unique_json.json', 'w') as outfile:
    json.dump(jsondata, outfile, indent= 2)

"""