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

        #creates divs for info, implicit, description, and flairs
        if u_info != []:
            for i in u_info:
                if i != "":
                    div_stat.append('<div class="stat">' + i + '</div>')
        if u_implicit != []:
            for i in u_implicit:
                span_implicit.append('<span class="affix">' + i + '</span>')
        if u_description != []:
            for i in u_description:
                if i != "":
                    div_description.append('<div class="affix">' + i + '</div>')
        if u_flair != []:
            for i in u_flair:
                if i != "":
                    div_flair.append('<div class="flair">' + i + '</div>')
        
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
        self.base = '<div class="base">' + u_base + '</div>'
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

class CreateFields:
    def __init__(self, uniquelist):
        self.uniquelist = uniquelist

    def jewelry(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Jewelry":
                x.append(i)
        return x

    def weapons(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Weapons":
                x.append(i)
        return x
    def armour(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Armour":
                x.append(i)
        return x
    def flasks(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Flasks":
                x.append(i)
        return x
    def maps(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Maps":
                x.append(i)
        return x
    def jewels(self):
        x = []
        for i in self.uniquelist:
            if i.type == "Jewels":
                x.append(i)
        return x


    def swords(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Swords":
                x.append(i)
        return x

    def bows(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Bows":
                x.append(i)
        return x

    def claws(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Claws":
                x.append(i)
        return x

    def daggers(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Daggers":
                x.append(i)
        return x

    def maces(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Mace / Sceptre":
                x.append(i)
        return x

    def staves(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Staves":
                x.append(i)
        return x

    def wands(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Wands":
                x.append(i)
        return x

    def axes(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Axe":
                x.append(i)
        return x

    def rings(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Ring":
                x.append(i)
        return x
    
    def amulets(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Amulet":
                x.append(i)
        return x

    def belts(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Belt":
                x.append(i)
        return x
    
    def body_armours(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Body Armour":
                x.append(i)
        return x

    def boots(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Boots":
                x.append(i)
        return x

    def gloves(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Gloves":
                x.append(i)
        return x

    def helmets(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Helmets":
                x.append(i)
        return x

    def shields(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Shields":
                x.append(i)
        return x

    def quivers(self):
        x = []
        for i in self.uniquelist:
            if i.basetype == "Quiver":
                x.append(i)
        return x

    def markup(self):
        alldivs = ""
        divlist = []
        for i in self.uniquelist:
            alldivs = ""
            #Creates Name
            alldivs = alldivs + '<div class="item_info unique">' + '<div class="item_name">' + '<div class="name">' + i.name + '</div>' + '<div class="item_base">' + i.base + '</div>' + '</div>'
            #Creates Info
            c = 0
            if len(i.info) >= 1:
                alldivs = alldivs + '<div class="item_information">'
                for f in i.info:
                    if len(i.info) >= 2:
                        if "Requires" in i.info:
                            alldivs = alldivs + '<div class="split"></div>' + i.info[c]
                        else:
                            alldivs = alldivs + i.info[c]
                    else:
                        alldivs = alldivs + i.info[c]
                    c += 1
                alldivs = alldivs + '</div>'
            #Creates Implicit
            c = 0
            if len(i.info) >= 1 and len(i.implicit) >= 1:
                alldivs = alldivs + '<div class="split"></div>' 
            if len(i.implicit) >= 1:
                alldivs = alldivs + '<div class="implicit">'
                for f in i.implicit:
                    alldivs = alldivs + i.implicit[c]
                    c += 1
                alldivs = alldivs + '</div>'
            #Creates Affixes
            c = 0
            if len(i.info) >= 1 or len(i.implicit) >=1:
                alldivs = alldivs + '<div class="split">' + '</div>'
            alldivs = alldivs + '<div class="item_description">'
            for f in i.description:
                alldivs = alldivs + i.description[c]
                c += 1
            alldivs = alldivs + '</div>'
            #Creates Flair
            c = 0
            alldivs = alldivs + '<div class="split"></div>'
            for f in i.flair:
                alldivs = alldivs + i.flair[c]
                c += 1
            if i.img != 0:
                alldivs = alldivs +  f'<img class="lazy" src="images/placeholder.jpg" data-src="images/{i.img}.png" data-srcset="images/{i.img}.png" alt="An image of the Unique Item {i.name}">' 
            alldivs = alldivs + '</div>'
            if i.img != 0:
                divlist.append(alldivs)
        return divlist
    def sortDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Dps, reverse=True)
        return x
    def sortPhysDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.PhysDps, reverse=True)
        return x
    def sortElementalDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.ElementalDps, reverse=True)
        return x
    def sortFireDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.FireDps, reverse=True)
        return x
    def sortCritical_Chance(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Critical_Chance, reverse=True)
        return x
    def sortAttack_Speed(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Attack_Speed, reverse=True)
        return x
    def sortChaosDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.ChaosDps, reverse=True)
        return x
    def sortLevel_Requirement(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Level_Requirement, reverse=True)
        return x
    def sortColdDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.ColdDps, reverse=True)
        return x
    def sortLightningDps(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.LightningDps, reverse=True)
        return x
    def sortArmour(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Armour, reverse=True)
        return x
    def sortEvasion(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Evasion, reverse=True)
        return x
    def sortEnergy_Shield(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.Energy_Shield, reverse=True)
        return x
    def sortName(self):
        sortedDps = self.uniquelist
        x = sorted(sortedDps, key=lambda x: x.name)
        return x


    def create(self, u_name):
        print(u_name)
        ObjectList = {}
        name = ""
        if "_" in u_name:
            y = u_name.split("_")
            name = y[0]
        else:
            name = u_name
        x = 0
        jsondata = []
        create = CreateFields(self.uniquelist).markup()
        for i in create:
            ObjectList[str(x)] = i
            jsondata.append(ObjectList[str(x)])
            x = x + 1
        x = 0
        with open(f'C:/Users/liuaa/Desktop/master_poequery/JSON/{u_name}.json', 'w') as outfile:
            json.dump(jsondata, outfile, indent= 3)
        """
        what = open(f'C:/Users/liuaa/Desktop/master_poequery/Javascript/{u_name}.js', 'w', encoding='utf-8')
        what.write('"use strict"; let items = []; let div = ""; ')
        what.write(f'fetch("JSON/{u_name}.json")')
        what.write('.then(function(resp) {return resp.json(); })')
        what.write('.then(function(data) {items = data; items.forEach(function(item,index){if (item !== ",") {div = div + item; } }); document.getElementById("react_root").innerHTML =  div; div = "";}); ')
        what.write('function search() {let text = document.getElementById("query").value.toLowerCase(); text = text.replace("\'", ""); ')
        what.write('items.forEach(function(item,index){if (item !== ",") {let x = item.toLowerCase(); x = x.replace("\'", ""); ')
        what.write('let indexit = x.indexOf(text); if (indexit !== -1) {div = div + item; } } }); document.getElementById("react_root").innerHTML =  div; div = ""; }')
        what.close()

        write_html = open(f'C:/Users/liuaa/Desktop/master_poequery/{u_name}.html','w', encoding='utf-8')
        write_html.write('<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8"><title>PoeQuery</title><link rel="stylesheet" href="master_style.css"></head>')
        write_html.write('<body><header class="head"><nav><ul class="nav"><li class="topnav"><a href="index.html">PoeQuery (beta)</a></li><li class="topnav"><a href="index.html">Uniques</a></li><li class="topnav"><a>Gems</a></li><li class="topnav"><a href="about.html">About</a></li></ul></nav></header>')
        write_html.write('<header class="sort"><nav><ul id="sortnav">')
        if "Axe" in u_name or "Weapon" in u_name or "Bow" in u_name or "Claw" in u_name or "Dagger" in u_name or "Mace" in u_name or "Stave" in u_name or "Sword" in u_name or "Wand" in u_name:
            write_html.write('<li class="basetype"><a href="Swords.html">Swords</a></li><li class="basetype"><a href="Axes.html">Axes</a></li><li class="basetype"><a href="Maces.html">Maces</a></li><li class="basetype"><a href="Daggers.html">Daggers</a></li>')
            write_html.write('<li class="basetype"><a href="Claws.html">Claws</a></li><li class="basetype"><a href="Staves.html">Staves</a></li><li class="basetype"><a href="Wands.html">Wands</a></li><li class="basetype"><a href="Bows.html">Bows</a></li></ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav">')
            write_html.write(f'<li class="filter"><a href="{name}_Level_Requirement.html">Level Req</a></li>')
            write_html.write('<li class="filter expand">')
            write_html.write(f'<a href="{name}_Dps.html">Dps</a>')
            write_html.write(f'<div class="content">')
            write_html.write(f'<a href="{name}_Dps.html">Dps</a>')
            write_html.write(f'<a href="{name}_ElementalDps.html">Elemental Dps</a>')
            write_html.write(f'<a href="{name}_FireDps.html">Fire Dps</a>')
            write_html.write(f'<a href="{name}_ColdDps.html">Cold Dps</a>')
            write_html.write(f'<a href="{name}_LightningDps.html">Lightning Dps</a>')
            write_html.write(f'<a href="{name}_ChaosDps.html">Chaos Dps</a>')
            write_html.write(f'</div></li><li class="filter"><a href="{name}_Attack_Speed.html">Attack Speed</a></li>')
            write_html.write(f'<li class="filter"><a href="{name}_Critical_Chance.html">Crit Chance</a></li>')
            write_html.write(f'</ul>')
        elif "Jewelry" in u_name or "Ring" in u_name or "Amulet" in u_name or "Belt" in u_name:
            write_html.write('<li class="basetype"><a href="Amulets.html">Amulets</a></li>')
            write_html.write('<li class="basetype"><a href="Belts.html">Belts</a></li>')
            write_html.write('<li class="basetype"><a href="Rings.html">Rings</a></li></ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav">')
            write_html.write(f'<li class="filter"><a href="{name}_Level_Requirement.html">Level Req</a></li></ul>')
        elif "Armour" in u_name or "Boots" in u_name or "Helmet" in u_name or "Glove" in u_name or "Shield" in u_name or "Quiver" in u_name:
            write_html.write('<li class="basetype"><a href="BodyArmours.html">Body Armours</a></li>')
            write_html.write('<li class="basetype"><a href="Helmets.html">Helmets</a></li>')
            write_html.write('<li class="basetype"><a href="Gloves.html">Gloves</a></li>')
            write_html.write('<li class="basetype"><a href="Boots.html">Boots</a></li>')
            write_html.write('<li class="basetype"><a href="Shields.html">Shields</a></li>')
            write_html.write('<li class="basetype"><a href="Quivers.html">Quivers</a></li></ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav">')
            if "Quiver" not in u_name:
                write_html.write(f'<li class="filter"><a href="{name}_Level_Requirement.html">Level Req</a></li>')
                write_html.write(f'<li class="filter"><a href="{name}_Armour.html">Armour</a></li>')
                write_html.write(f'<li class="filter"><a href="{name}_Evasion.html">Evasion</a></li>')
                write_html.write(f'<li class="filter"><a href="{name}_Energy_Shield.html">Energy Shield</a></li></ul>')
            else:
                write_html.write(f'<li class="filter"><a href="{name}_Level_Requirement.html">Level Req</a></li></ul>')
        elif "Flask" in u_name:
            write_html.write('</ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav">')
            write_html.write(f'<li class="filter"><a href="{name}_Level_Requirement.html">Level Req</a></li></ul>')
        elif "Jewel" in u_name:
            write_html.write('</ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav"></nav>')
        elif "Map" in u_name:
            write_html.write('</ul>')
            write_html.write('</nav></header><header class="sortfilter"><nav><ul id="filternav"></nav>')


        write_html.write('</nav>')
        write_html.write('</header><div><main><div class="search"><div class="fields"><label for="query"></label><input class="links" type="text" id="query" placeholder="Search" aria-label="Search for anything" oninput="search()" autofocus>')
        write_html.write(f'<a><div class="links">Pinned</div></a><a href="Uniques.html"><div class="links">All</div></a><a href="Jewelry.html"><div class="links">Jewelry</div></a><a href="Weapons.html"><div class="links">Weapons</div></a><a href="AllArmours.html"><div class="links">Armours/Offhand</div></a><a href="Flasks.html"><div class="links">Flasks</div></a><a href="Maps.html"><div class="links">Maps</div></a><a href="Jewels.html"><div class="links">Jewels</div></a><a><div class="links">New</div></a>')
        write_html.write('<div id="like_button_container"></div>')
        write_html.write('</div></div><section class="queries"><div class="item_result" id="react_root">')
        write_html.write(f'</div></section></main></div><script src="Javascript/{u_name}.js"></script></body></html>')
        write_html.close()
        """





Uniques = CreateFields(Unique_List).markup()
Unique_Name = CreateFields(CreateFields(Unique_List).sortName()).markup()

Weapons = CreateFields(Unique_List).weapons()
Axes = CreateFields(Unique_List).axes()
Bows = CreateFields(Unique_List).bows()
Claws = CreateFields(Unique_List).claws()
Daggers = CreateFields(Unique_List).daggers()
Maces = CreateFields(Unique_List).maces()
Staves = CreateFields(Unique_List).staves()
Swords = CreateFields(Unique_List).swords()
Wands = CreateFields(Unique_List).wands()

AllArmours = CreateFields(Unique_List).armour()
Boots = CreateFields(Unique_List).boots()
BodyArmours = CreateFields(Unique_List).body_armours()
Helmets = CreateFields(Unique_List).helmets()
Gloves = CreateFields(Unique_List).gloves()
Quivers = CreateFields(Unique_List).quivers()
Shields = CreateFields(Unique_List).shields()

Jewelry = CreateFields(Unique_List).jewelry()
Rings = CreateFields(Unique_List).rings()
Amulets = CreateFields(Unique_List).amulets()
Belts = CreateFields(Unique_List).belts()

Flasks = CreateFields(Unique_List).flasks()

Maps = CreateFields(Unique_List).maps()

Jewels = CreateFields(Unique_List).jewels()

#Creates Unique Json
CreateFields(Unique_List).create('Uniques')
CreateFields(CreateFields(Unique_List).sortName()).create('Uniques_Name')

#Creates Weapon Json
CreateFields(CreateFields(Weapons).sortName()).create('Weapons')
CreateFields(CreateFields(Weapons).sortDps()).create('Weapons_Dps')
CreateFields(CreateFields(Weapons).sortElementalDps()).create('Weapons_ElementalDps')
CreateFields(CreateFields(Weapons).sortPhysDps()).create('Weapons_PhysDps')
CreateFields(CreateFields(Weapons).sortFireDps()).create('Weapons_FireDps')
CreateFields(CreateFields(Weapons).sortColdDps()).create('Weapons_ColdDps')
CreateFields(CreateFields(Weapons).sortLightningDps()).create('Weapons_LightningDps')
CreateFields(CreateFields(Weapons).sortChaosDps()).create('Weapons_ChaosDps')
CreateFields(CreateFields(Weapons).sortCritical_Chance()).create('Weapons_Critical_Chance')
CreateFields(CreateFields(Weapons).sortAttack_Speed()).create('Weapons_Attack_Speed')
CreateFields(CreateFields(Weapons).sortLevel_Requirement()).create('Weapons_Level_Requirement')

#Creates Sword Json
CreateFields(CreateFields(Swords).sortName()).create('Swords')
CreateFields(CreateFields(Swords).sortDps()).create('Swords_Dps')
CreateFields(CreateFields(Swords).sortElementalDps()).create('Swords_ElementalDps')
CreateFields(CreateFields(Swords).sortPhysDps()).create('Swords_PhysDps')
CreateFields(CreateFields(Swords).sortFireDps()).create('Swords_FireDps')
CreateFields(CreateFields(Swords).sortColdDps()).create('Swords_ColdDps')
CreateFields(CreateFields(Swords).sortLightningDps()).create('Swords_LightningDps')
CreateFields(CreateFields(Swords).sortChaosDps()).create('Swords_ChaosDps')
CreateFields(CreateFields(Swords).sortCritical_Chance()).create('Swords_Critical_Chance')
CreateFields(CreateFields(Swords).sortAttack_Speed()).create('Swords_Attack_Speed')
CreateFields(CreateFields(Swords).sortLevel_Requirement()).create('Swords_Level_Requirement')

#Creates Wand Json
CreateFields(CreateFields(Wands).sortName()).create('Wands')
CreateFields(CreateFields(Wands).sortDps()).create('Wands_Dps')
CreateFields(CreateFields(Wands).sortElementalDps()).create('Wands_ElementalDps')
CreateFields(CreateFields(Wands).sortPhysDps()).create('Wands_PhysDps')
CreateFields(CreateFields(Wands).sortFireDps()).create('Wands_FireDps')
CreateFields(CreateFields(Wands).sortColdDps()).create('Wands_ColdDps')
CreateFields(CreateFields(Wands).sortLightningDps()).create('Wands_LightningDps')
CreateFields(CreateFields(Wands).sortChaosDps()).create('Wands_ChaosDps')
CreateFields(CreateFields(Wands).sortCritical_Chance()).create('Wands_Critical_Chance')
CreateFields(CreateFields(Wands).sortAttack_Speed()).create('Wands_Attack_Speed')
CreateFields(CreateFields(Wands).sortLevel_Requirement()).create('Wands_Level_Requirement')

#Creates Stave Json
CreateFields(CreateFields(Staves).sortName()).create('Staves')
CreateFields(CreateFields(Staves).sortDps()).create('Staves_Dps')
CreateFields(CreateFields(Staves).sortElementalDps()).create('Staves_ElementalDps')
CreateFields(CreateFields(Staves).sortPhysDps()).create('Staves_PhysDps')
CreateFields(CreateFields(Staves).sortFireDps()).create('Staves_FireDps')
CreateFields(CreateFields(Staves).sortColdDps()).create('Staves_ColdDps')
CreateFields(CreateFields(Staves).sortLightningDps()).create('Staves_LightningDps')
CreateFields(CreateFields(Staves).sortChaosDps()).create('Staves_ChaosDps')
CreateFields(CreateFields(Staves).sortCritical_Chance()).create('Staves_Critical_Chance')
CreateFields(CreateFields(Staves).sortAttack_Speed()).create('Staves_Attack_Speed')
CreateFields(CreateFields(Staves).sortLevel_Requirement()).create('Staves_Level_Requirement')

#Creates Mace Json
CreateFields(CreateFields(Maces).sortName()).create('Maces')
CreateFields(CreateFields(Maces).sortDps()).create('Maces_Dps')
CreateFields(CreateFields(Maces).sortElementalDps()).create('Maces_ElementalDps')
CreateFields(CreateFields(Maces).sortPhysDps()).create('Maces_PhysDps')
CreateFields(CreateFields(Maces).sortFireDps()).create('Maces_FireDps')
CreateFields(CreateFields(Maces).sortColdDps()).create('Maces_ColdDps')
CreateFields(CreateFields(Maces).sortLightningDps()).create('Maces_LightningDps')
CreateFields(CreateFields(Maces).sortChaosDps()).create('Maces_ChaosDps')
CreateFields(CreateFields(Maces).sortCritical_Chance()).create('Maces_Critical_Chance')
CreateFields(CreateFields(Maces).sortAttack_Speed()).create('Maces_Attack_Speed')
CreateFields(CreateFields(Maces).sortLevel_Requirement()).create('Maces_Level_Requirement')

#Creates Dagger Json
CreateFields(CreateFields(Daggers).sortName()).create('Daggers')
CreateFields(CreateFields(Daggers).sortDps()).create('Daggers_Dps')
CreateFields(CreateFields(Daggers).sortElementalDps()).create('Daggers_ElementalDps')
CreateFields(CreateFields(Daggers).sortPhysDps()).create('Daggers_PhysDps')
CreateFields(CreateFields(Daggers).sortFireDps()).create('Daggers_FireDps')
CreateFields(CreateFields(Daggers).sortColdDps()).create('Daggers_ColdDps')
CreateFields(CreateFields(Daggers).sortLightningDps()).create('Daggers_LightningDps')
CreateFields(CreateFields(Daggers).sortChaosDps()).create('Daggers_ChaosDps')
CreateFields(CreateFields(Daggers).sortCritical_Chance()).create('Daggers_Critical_Chance')
CreateFields(CreateFields(Daggers).sortAttack_Speed()).create('Daggers_Attack_Speed')
CreateFields(CreateFields(Daggers).sortLevel_Requirement()).create('Daggers_Level_Requirement')

#Creates Claw Json
CreateFields(CreateFields(Claws).sortName()).create('Claws')
CreateFields(CreateFields(Claws).sortDps()).create('Claws_Dps')
CreateFields(CreateFields(Claws).sortElementalDps()).create('Claws_ElementalDps')
CreateFields(CreateFields(Claws).sortPhysDps()).create('Claws_PhysDps')
CreateFields(CreateFields(Claws).sortFireDps()).create('Claws_FireDps')
CreateFields(CreateFields(Claws).sortColdDps()).create('Claws_ColdDps')
CreateFields(CreateFields(Claws).sortLightningDps()).create('Claws_LightningDps')
CreateFields(CreateFields(Claws).sortChaosDps()).create('Claws_ChaosDps')
CreateFields(CreateFields(Claws).sortCritical_Chance()).create('Claws_Critical_Chance')
CreateFields(CreateFields(Claws).sortAttack_Speed()).create('Claws_Attack_Speed')
CreateFields(CreateFields(Claws).sortLevel_Requirement()).create('Claws_Level_Requirement')

#Creates Bow Json
CreateFields(CreateFields(Bows).sortName()).create('Bows')
CreateFields(CreateFields(Bows).sortDps()).create('Bows_Dps')
CreateFields(CreateFields(Bows).sortElementalDps()).create('Bows_ElementalDps')
CreateFields(CreateFields(Bows).sortPhysDps()).create('Bows_PhysDps')
CreateFields(CreateFields(Bows).sortFireDps()).create('Bows_FireDps')
CreateFields(CreateFields(Bows).sortColdDps()).create('Bows_ColdDps')
CreateFields(CreateFields(Bows).sortLightningDps()).create('Bows_LightningDps')
CreateFields(CreateFields(Bows).sortChaosDps()).create('Bows_ChaosDps')
CreateFields(CreateFields(Bows).sortCritical_Chance()).create('Bows_Critical_Chance')
CreateFields(CreateFields(Bows).sortAttack_Speed()).create('Bows_Attack_Speed')
CreateFields(CreateFields(Bows).sortLevel_Requirement()).create('Bows_Level_Requirement')

#Creates Axe Json
CreateFields(CreateFields(Axes).sortName()).create('Axes')
CreateFields(CreateFields(Axes).sortDps()).create('Axes_Dps')
CreateFields(CreateFields(Axes).sortElementalDps()).create('Axes_ElementalDps')
CreateFields(CreateFields(Axes).sortPhysDps()).create('Axes_PhysDps')
CreateFields(CreateFields(Axes).sortFireDps()).create('Axes_FireDps')
CreateFields(CreateFields(Axes).sortColdDps()).create('Axes_ColdDps')
CreateFields(CreateFields(Axes).sortLightningDps()).create('Axes_LightningDps')
CreateFields(CreateFields(Axes).sortChaosDps()).create('Axes_ChaosDps')
CreateFields(CreateFields(Axes).sortCritical_Chance()).create('Axes_Critical_Chance')
CreateFields(CreateFields(Axes).sortAttack_Speed()).create('Axes_Attack_Speed')
CreateFields(CreateFields(Axes).sortLevel_Requirement()).create('Axes_Level_Requirement')


#Creates Armour json
CreateFields(CreateFields(AllArmours).sortName()).create('AllArmours')
CreateFields(CreateFields(AllArmours).sortArmour()).create('AllArmours_Armour')
CreateFields(CreateFields(AllArmours).sortEvasion()).create('AllArmours_Evasion')
CreateFields(CreateFields(AllArmours).sortEnergy_Shield()).create('AllArmours_Energy_Shield')
CreateFields(CreateFields(AllArmours).sortLevel_Requirement()).create('AllArmours_Level_Requirement')

#Creates Boots json
CreateFields(CreateFields(Boots).sortName()).create('Boots')
CreateFields(CreateFields(Boots).sortArmour()).create('Boots_Armour')
CreateFields(CreateFields(Boots).sortEvasion()).create('Boots_Evasion')
CreateFields(CreateFields(Boots).sortEnergy_Shield()).create('Boots_Energy_Shield')
CreateFields(CreateFields(Boots).sortLevel_Requirement()).create('Boots_Level_Requirement')

#Creates BodyArmours json
CreateFields(CreateFields(BodyArmours).sortName()).create('BodyArmours')
CreateFields(CreateFields(BodyArmours).sortArmour()).create('BodyArmours_Armour')
CreateFields(CreateFields(BodyArmours).sortEvasion()).create('BodyArmours_Evasion')
CreateFields(CreateFields(BodyArmours).sortEnergy_Shield()).create('BodyArmours_Energy_Shield')
CreateFields(CreateFields(BodyArmours).sortLevel_Requirement()).create('BodyArmours_Level_Requirement')

#Creates Gloves json
CreateFields(CreateFields(Gloves).sortName()).create('Gloves')
CreateFields(CreateFields(Gloves).sortArmour()).create('Gloves_Armour')
CreateFields(CreateFields(Gloves).sortEvasion()).create('Gloves_Evasion')
CreateFields(CreateFields(Gloves).sortEnergy_Shield()).create('Gloves_Energy_Shield')
CreateFields(CreateFields(Gloves).sortLevel_Requirement()).create('Gloves_Level_Requirement')

#Creates Helmets json
CreateFields(CreateFields(Helmets).sortName()).create('Helmets')
CreateFields(CreateFields(Helmets).sortArmour()).create('Helmets_Armour')
CreateFields(CreateFields(Helmets).sortEvasion()).create('Helmets_Evasion')
CreateFields(CreateFields(Helmets).sortEnergy_Shield()).create('Helmets_Energy_Shield')
CreateFields(CreateFields(Helmets).sortLevel_Requirement()).create('Helmets_Level_Requirement')

#Creates Quivers json
CreateFields(CreateFields(Quivers).sortName()).create('Quivers')
CreateFields(CreateFields(Quivers).sortArmour()).create('Quivers_Armour')
CreateFields(CreateFields(Quivers).sortEvasion()).create('Quivers_Evasion')
CreateFields(CreateFields(Quivers).sortEnergy_Shield()).create('Quivers_Energy_Shield')
CreateFields(CreateFields(Quivers).sortLevel_Requirement()).create('Quivers_Level_Requirement')

#Creates Shields json
CreateFields(CreateFields(Shields).sortName()).create('Shields')
CreateFields(CreateFields(Shields).sortArmour()).create('Shields_Armour')
CreateFields(CreateFields(Shields).sortEvasion()).create('Shields_Evasion')
CreateFields(CreateFields(Shields).sortEnergy_Shield()).create('Shields_Energy_Shield')
CreateFields(CreateFields(Shields).sortLevel_Requirement()).create('Shields_Level_Requirement')

#Creates Jewelry json
CreateFields(CreateFields(Jewelry).sortName()).create('Jewelry')
CreateFields(CreateFields(Jewelry).sortLevel_Requirement()).create('Jewelry_Level_Requirement')

#Creates Ring Json
CreateFields(CreateFields(Jewelry).sortName()).create('Rings')
CreateFields(CreateFields(Jewelry).sortLevel_Requirement()).create('Rings_Level_Requirement')

#Creates Amulet Json
CreateFields(CreateFields(Amulets).sortName()).create('Amulets')
CreateFields(CreateFields(Amulets).sortLevel_Requirement()).create('Amulets_Level_Requirement')

#Creates Belt Json
CreateFields(CreateFields(Belts).sortName()).create('Belts')
CreateFields(CreateFields(Belts).sortLevel_Requirement()).create('Belts_Level_Requirement')

#Creates Flasks Json
CreateFields(CreateFields(Flasks).sortName()).create('Flasks')
CreateFields(CreateFields(Flasks).sortLevel_Requirement()).create('Flasks_Level_Requirement')

#Creates Jewels Json
CreateFields(CreateFields(Jewels).sortName()).create('Jewels')

#Creates Maps Json
CreateFields(CreateFields(Maps).sortName()).create('Maps')

