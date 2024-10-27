import pathlib
import os
from PIL import Image

pack = pathlib.Path("C:/Users/timot/AppData/Roaming/.minecraft/resourcepacks/Game Packs/Chorus Virus Rebudded/assets/minecraft")

allowed_values = [2**i for i in range(3,16)]

all_files = list(pack.rglob("*"))
for file in all_files:
    if str(file).endswith('.png'):
        im = Image.open(file)
        x,y = im.size
        if x in allowed_values:
            pass
        else:
            print(im.size)
            print(file)