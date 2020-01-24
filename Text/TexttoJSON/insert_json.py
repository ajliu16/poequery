import json
output = open("insert_uniques.sql", "w")



f = "INSERT INTO library_unique (name,base,catagory,catagory_type,info,implicit,description,flair,dps,phys_dps,elemental_dps,fire_dps,cold_dps,lightning_dps,chaos_dps,attack_speed,critical_chance,level_requirement,armour,evasion,energy_shield)"
with open("unique_json.json") as infile:
    all_data = json.load(infile)
    for i in all_data:
        output.write(f'{f} VALUES ("{i["name"]}","{i["base"]}","{i["catagory"]}","{i["catagory_type"]}","{i["info"]}","{i["implicit"]}","{i["description"]}","{i["flair"]}",{i["dps"]},{i["phys_dps"]},{i["elemental_dps"]},{i["fire_dps"]},{i["cold_dps"]},{i["lightning_dps"]},{i["chaos_dps"]},{i["attack_speed"]},{i["critical_chance"]},{i["level_requirement"]},{i["armour"]},{i["evasion"]},{i["energy_shield"]}; ')
        output.write("\n")

output.close()
