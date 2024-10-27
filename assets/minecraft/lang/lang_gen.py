#this code propagates modifications on "en_us" on to other language files.

import os
import json

os.chdir("C:/Users/timot/AppData/Roaming/.minecraft/resourcepacks/Game Packs/Chorus Virus Rebudded/assets/minecraft/lang")

all_languages = []

with open("all_languages.txt","r") as languages:
    languages = languages.readlines()
for language in languages:
    all_languages.append(language[:-1])

all_languages.remove('en_us')

with open('en_us.json') as base_file:
    base_content = json.load(base_file)

for language in all_languages:
    filename = language+".json"
    try:
        with open(filename,'r') as newfile:
            suppl_content = json.load(newfile)
    except:
        suppl_content = {}
    for key in base_content:
        if key not in suppl_content:
            suppl_content[key] = base_content[key]
    with open(filename,"w") as newfile:
        json.dump(suppl_content,newfile,indent=2,ensure_ascii=False)
